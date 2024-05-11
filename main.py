from antlr4 import FileStream, CommonTokenStream
from GameGrammarLexer import GameGrammarLexer
from GameGrammarParser import GameGrammarParser


def parse_script(script_file):
    # Create a file stream from the input script file
    input_stream = FileStream(script_file)

    # Create a lexer
    lexer = GameGrammarLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Initialize the parser with the token stream
    parser = GameGrammarParser(token_stream)

    # Parse the script and return the parse tree
    tree = parser.gameScript()

    return tree


def visualize_parse_tree(tree, parser):
    # Get the tree string representation
    tree_str = tree.toStringTree(recog=parser)

    # Display the tree string representation
    print("Parse Tree Visualization:")
    print(tree_str)


# Example usage:
script_tree = parse_script('game_script.txt')
visualize_parse_tree(script_tree, GameGrammarParser)

