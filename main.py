import sys
from antlr4 import *
from GameGrammarLexer import GameGrammarLexer
from GameGrammarParser import GameGrammarParser
from GameGrammarListener import GameGrammarListener

# Define constants
ROOM_HEIGHT = 7
ROOM_WIDTH = 11
SEPARATION = 3  # Separation between rooms

class GameVisualization(GameGrammarListener):
    def __init__(self, gameboard):
        self.rooms, self.items = self.readmap(gameboard)
        self.current_room = self.rooms['start_room']

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

                while i + 1 < len(script_lines) and not script_lines[i + 1].strip().startswith('}'):
                    i += 1
                    if script_lines[i].strip().startswith('items'):
                        items_list = script_lines[i].split('[')[1].split(']')[0].split(',')
                        room_info['items'] = [item.strip() for item in items_list]
                    elif ':' in script_lines[i].strip() and script_lines[i].strip().split(':')[0].strip() in ['north', 'south', 'east', 'west']:
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
            i += 1

        return rooms, items

    def draw_map(self):
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

        # Draw items in the center of the room
        for idx, item in enumerate(room['items']):
            map_grid[grid_y + ROOM_HEIGHT // 2 + idx][grid_x + ROOM_WIDTH // 2] = item[0].upper()

    def game_loop(self):
        while True:
            self.draw_map()
            current_room = self.current_room
            options = []
            if current_room['north']:
                options.append(('Go north', current_room['north']))
            if current_room['south']:
                options.append(('Go south', current_room['south']))
            if current_room['east']:
                options.append(('Go east', current_room['east']))
            if current_room['west']:
                options.append(('Go west', current_room['west']))
            options.append(('End game', None))

            print("-------------- Pick an option -------------")
            for idx, (desc, _) in enumerate(options):
                print(f"{idx + 1}. {desc}")

            choice = int(input("Enter your choice: ")) - 1
            if choice == len(options) - 1:
                print("Game ended.")
                break
            else:
                self.current_room = self.rooms[options[choice][1]]

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GameGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GameGrammarParser(stream)
    tree = parser.gameScript()

    # Validate the game script against the grammar
    game_visualization = GameVisualization(argv[1])
    walker = ParseTreeWalker()
    walker.walk(game_visualization, tree)

    # Run the game visualization loop
    game_visualization.game_loop()

if __name__ == '__main__':
    main(sys.argv)
