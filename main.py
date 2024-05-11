from antlr4 import FileStream, CommonTokenStream

from GameGrammarLexer import GameGrammarLexer
from GameGrammarParser import GameGrammarParser

def parse_script(script_file):
    input_stream = FileStream(script_file)
    lexer = GameGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GameGrammarParser(token_stream)
    tree = parser.gameScript()

    return tree

def visualize_parse_tree(tree, parser):
    # Get the tree string representation
    tree_str = tree.toStringTree(recog=parser)

    # Display the tree string representation
    print("Parse Tree Visualization:")
    print(tree_str)

# Example usage:
parser = GameGrammarParser(None)
script_tree = parse_script('game_script.txt')
visualize_parse_tree(script_tree, parser)

