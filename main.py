import sys
from antlr4 import *
from GameGrammarLexer import GameGrammarLexer
from GameGrammarParser import GameGrammarParser
from GameGrammarListener import GameGrammarListener
from GrammarError import CustomErrorListener, GrammarError

# Define constants
ROOM_HEIGHT = 7
ROOM_WIDTH = 11
SEPARATION = 3  # Separation between rooms


class IdentifierError(Exception):
    pass


class SymbolTable:
    def __init__(self):
        self.items = set()
        self.rooms = set()
        self.actions = set()

    def declare_item(self, name):
        self.items.add(name)

    def declare_room(self, name):
        self.rooms.add(name)

    def declare_action(self, name):
        self.actions.add(name)

    def is_item_declared(self, name):
        return name in self.items

    def is_room_declared(self, name):
        return name in self.rooms

    def is_action_declared(self, name):
        return name in self.actions


class GameVisualization(GameGrammarListener):
    def __init__(self, gameboard):
        self.symbol_table = SymbolTable()
        self.rooms, self.items = self.readmap(gameboard)
        self.current_room = self.rooms['start_room']
        self.player_items = []

    def readmap(self, gameboard):
        with open(gameboard, 'r') as file:
            script_lines = file.readlines()

        rooms = {}
        items = {}
        i = 0
        while i < len(script_lines):
            line = script_lines[i].strip()

            if line.startswith("room"):
                room_info = {}
                room_name = line.split()[1]
                room_info['name'] = room_name
                room_info['description'] = script_lines[i + 1].split(':', 1)[1].strip()
                room_info['items'] = []
                room_info['north'] = None
                room_info['south'] = None
                room_info['east'] = None
                room_info['west'] = None

                self.symbol_table.declare_room(room_name)  # Declare room

                while i + 1 < len(script_lines) and not script_lines[i + 1].strip().startswith('}'):
                    i += 1
                    if script_lines[i].strip().startswith('items'):
                        items_list = script_lines[i].split('[')[1].split(']')[0].split(',')
                        room_info['items'] = [item.strip() for item in items_list]
                    elif ':' in script_lines[i].strip() and script_lines[i].strip().split(':')[0].strip() in ['north',
                                                                                                              'south',
                                                                                                              'east',
                                                                                                              'west']:
                        direction, destination = map(str.strip, script_lines[i].strip().split(':'))
                        room_info[direction] = destination[:-1]  # Remove semicolon at the end

                rooms[room_name] = room_info

            elif line.startswith("item"):
                item_info = {}
                item_name = line.split()[1]
                item_info['name'] = item_name
                item_info['description'] = script_lines[i + 1].split(':', 1)[1].strip()
                actions = script_lines[i + 2].split(':', 1)[1].strip().split(',')
                item_info['actions'] = [action.strip() for action in actions]
                items[item_name] = item_info

                self.symbol_table.declare_item(item_name)  # Declare item

                # Collect actions
                if 'actions:' in script_lines[i + 2]:
                    actions = script_lines[i + 2].split(':', 1)[1].strip().split(',')
                    if actions:
                        actions[-1] = actions[-1].rstrip(';')
                    item_info['actions'] = []

                    for action in actions:
                        if '(' in action and ')' in action:
                            action_name, required_item = action.split('(')
                            required_item = required_item[:-1]  # Remove closing bracket
                            if not self.symbol_table.is_item_declared(required_item.strip()):
                                raise IdentifierError(
                                    f"Required item '{required_item.strip()}' for action '{action_name.strip()}' in item '{item_name}' is not declared.")
                            item_info['actions'].append(
                                {'name': action_name.strip(), 'required_item': required_item.strip()})
                        else:
                            item_info['actions'].append({'name': action.strip()})

                        if not self.symbol_table.is_action_declared(item_info['actions'][-1]['name']):
                            raise IdentifierError(
                                f"Action '{item_info['actions'][-1]['name']}' used in item '{item_name}' is not declared.")
                else:
                    item_info['actions'] = []

                # Collect secret items
                if 'secret_items:' in script_lines[i + 3]:
                    secret_items = script_lines[i + 3].split(':', 1)[1].strip().split(',')
                    item_info['secret_items'] = [item.strip() for item in secret_items]

                    if item_info['secret_items']:
                        item_info['secret_items'][-1] = item_info['secret_items'][-1].rstrip(';')

                    for secret_item in item_info['secret_items']:
                        if not self.symbol_table.is_item_declared(secret_item):
                            raise IdentifierError(
                            f"Secret item '{secret_item}' in item '{item_name}' is not declared.")
                else:
                    item_info['secret_items'] = []

            elif line.startswith("action"):
                action_name = line.split()[1]
                self.symbol_table.declare_action(action_name)  # Declare action

            i += 1

        return rooms, items

    def draw_map(self):
        print("/------------------------ Game map ---------------------------\\")
        positions = {}
        visited = set()
        self._place_room(self.current_room, 0, 0, positions, visited)

        min_x = min(pos[0] for pos in positions.values())
        max_x = max(pos[0] for pos in positions.values())
        min_y = min(pos[1] for pos in positions.values())
        max_y = max(pos[1] for pos in positions.values())

        map_width = (max_x - min_x + 1) * (ROOM_WIDTH + SEPARATION)
        map_height = (max_y - min_y + 1) * (ROOM_HEIGHT + SEPARATION)

        map_grid = [[' ' for _ in range(map_width)] for _ in range(map_height)]

        for room_name, (x, y) in positions.items():
            self._draw_room(map_grid, x - min_x, y - min_y, self.rooms[room_name])

        for row in map_grid:
            print(''.join(row))

    def _place_room(self, room, x, y, positions, visited):
        if room['name'] in visited:
            return

        visited.add(room['name'])
        positions[room['name']] = (x, y)

        if room['north'] and room['north'] not in visited:
            self._place_room(self.rooms[room['north']], x, y - 1, positions, visited)
        if room['south'] and room['south'] not in visited:
            self._place_room(self.rooms[room['south']], x, y + 1, positions, visited)
        if room['east'] and room['east'] not in visited:
            self._place_room(self.rooms[room['east']], x + 1, y, positions, visited)
        if room['west'] and room['west'] not in visited:
            self._place_room(self.rooms[room['west']], x - 1, y, positions, visited)

    def _draw_room(self, map_grid, x, y, room):
        grid_x = x * (ROOM_WIDTH + SEPARATION)
        grid_y = y * (ROOM_HEIGHT + SEPARATION)

        for i in range(ROOM_HEIGHT):
            for j in range(ROOM_WIDTH):
                map_grid[grid_y + i][grid_x + j] = ' '

        # Draw room boundaries
        for i in range(ROOM_WIDTH):
            map_grid[grid_y][grid_x + i] = '-'
            map_grid[grid_y + ROOM_HEIGHT - 1][grid_x + i] = '-'
        for i in range(ROOM_HEIGHT):
            map_grid[grid_y + i][grid_x] = '|'
            map_grid[grid_y + i][grid_x + ROOM_WIDTH - 1] = '|'

        # Draw doors
        if room['north']:
            map_grid[grid_y][grid_x + ROOM_WIDTH // 2 - 1] = ' '
            map_grid[grid_y][grid_x + ROOM_WIDTH // 2] = ' '
            map_grid[grid_y][grid_x + ROOM_WIDTH // 2 + 1] = ' '
        if room['south']:
            map_grid[grid_y + ROOM_HEIGHT - 1][grid_x + ROOM_WIDTH // 2 - 1] = ' '
            map_grid[grid_y + ROOM_HEIGHT - 1][grid_x + ROOM_WIDTH // 2] = ' '
            map_grid[grid_y + ROOM_HEIGHT - 1][grid_x + ROOM_WIDTH // 2 + 1] = ' '
        if room['east']:
            map_grid[grid_y + ROOM_HEIGHT // 2 - 1][grid_x + ROOM_WIDTH - 1] = ' '
            map_grid[grid_y + ROOM_HEIGHT // 2][grid_x + ROOM_WIDTH - 1] = ' '
            map_grid[grid_y + ROOM_HEIGHT // 2 + 1][grid_x + ROOM_WIDTH - 1] = ' '
        if room['west']:
            map_grid[grid_y + ROOM_HEIGHT // 2 - 1][grid_x] = ' '
            map_grid[grid_y + ROOM_HEIGHT // 2][grid_x] = ' '
            map_grid[grid_y + ROOM_HEIGHT // 2 + 1][grid_x] = ' '

        # Draw player only in the current room
        if room['name'] == self.current_room['name']:
            map_grid[grid_y + ROOM_HEIGHT // 2][grid_x + ROOM_WIDTH // 2] = 'X'

        # Draw items just above the center of the room
        for idx, item in enumerate(room['items']):
            map_grid[grid_y + ROOM_HEIGHT // 2 - 1 - idx][grid_x + ROOM_WIDTH // 2] = item[0].upper()

    def _show_item_menu(self, item_name, room):
        item = self.items[item_name]
        actions = item['actions']
        print(f"-------------- Inspect Item: {item_name} -------------")
        options = []

        for action in actions:
            if action['name'] == 'pickup':
                options.append(('Pick up', 'pickup'))
            elif action['name'] == 'open':
                options.append(('Open', 'open'))

        options.append(('Go back', 'back'))

        print("Choose an action:")
        for idx, (desc, _) in enumerate(options):
            print(f"{idx + 1}. {desc}")

        choice = int(input("Enter your choice: ")) - 1

        if choice == len(options) - 1:
            return  # Go back to the game menu
        elif choice >= len(actions):
            print("Invalid choice.")
            return
        else:
            action = options[choice][1]
            if action == 'pickup':
                self.player_items.append(item_name)
                room['items'].remove(item_name)
                print(f"You picked up the {item_name}.")
            elif action == 'open':
                required_item = None
                for action in self.items[item_name]['actions']:
                    if action['name'] == 'open' and 'required_item' in action:
                        required_item = action['required_item']
                if required_item is None or required_item in self.player_items:
                    self.player_items.extend(item['secret_items'])
                    print(f"You opened the {item_name} and obtained {item['secret_items']}.")
                elif required_item:
                    print(f"You need the {required_item[0]} to open this.")
                else:
                    print(f"You opened the {item_name}.")

    def game_loop(self):
        while True:
            self.draw_map()
            current_room = self.current_room
            room_connections = self.rooms[current_room['name']]
            num_connections = sum(
                1 for direction in ['north', 'south', 'east', 'west'] if room_connections[direction] is not None)
            room_items = self.rooms[current_room['name']]['items']
            options = []

            # Add movement options
            if current_room['north']:
                options.append(('Go north', current_room['north']))
            if current_room['south']:
                options.append(('Go south', current_room['south']))
            if current_room['east']:
                options.append(('Go east', current_room['east']))
            if current_room['west']:
                options.append(('Go west', current_room['west']))

            # Add pick up item option if current room has an item
            for item in room_items:
                options.append(('Inspect item: ' + item, current_room))

            # Add show item list option if player has items
            if self.player_items:
                options.append(('Show item list', 'show_items'))

            options.append(('End game', None))

            print("-------------- Pick an option -------------")
            for idx in range(len(options)):
                print(f"{idx + 1}. {options[idx][0]}")

            choice = int(input("Enter your choice: ")) - 1

            if choice == len(options) - 1:
                print("Game ended.")
                break
            elif (num_connections - 1) < choice <= (num_connections + len(room_items) - 1):
                selected_item = room_items[choice - num_connections]
                self._show_item_menu(item_name=selected_item, room=current_room)
            else:
                action = options[choice][1]
                if isinstance(action, str) and action == 'show_items':
                    print("Player items:", ', '.join(self.player_items))
                else:
                    self.current_room = self.rooms[action]

            # Check if player has final_prize
            if 'final_prize' in self.player_items:
                print("\n\n"
                      "-------------------------\n"
                      "         YOU WON         \n"
                      "-------------------------\n")
                break

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GameGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GameGrammarParser(stream)

    # Set up custom error listener
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse the game script
    tree = parser.gameScript()

    # Check for grammar errors
    if error_listener.has_errors():
        errors = error_listener.get_errors()
        raise GrammarError(f"Error detected in the game script: {errors}")

    # Validate the game script against the grammar
    game_visualization = GameVisualization(argv[1])
    walker = ParseTreeWalker()
    walker.walk(game_visualization, tree)

    # Run the game visualization loop
    game_visualization.game_loop()


if __name__ == '__main__':
    try:
        main(sys.argv)
    except GrammarError as e:
        print(str(e))
    except IdentifierError as e:
        print(f"Identifier error: {e}")
