# Generated from GameGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GameGrammarParser import GameGrammarParser
else:
    from GameGrammarParser import GameGrammarParser

# This class defines a complete listener for a parse tree produced by GameGrammarParser.
class GameGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GameGrammarParser#gameScript.
    def enterGameScript(self, ctx:GameGrammarParser.GameScriptContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#gameScript.
    def exitGameScript(self, ctx:GameGrammarParser.GameScriptContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#level.
    def enterLevel(self, ctx:GameGrammarParser.LevelContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#level.
    def exitLevel(self, ctx:GameGrammarParser.LevelContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#room.
    def enterRoom(self, ctx:GameGrammarParser.RoomContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#room.
    def exitRoom(self, ctx:GameGrammarParser.RoomContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#roomConnection.
    def enterRoomConnection(self, ctx:GameGrammarParser.RoomConnectionContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#roomConnection.
    def exitRoomConnection(self, ctx:GameGrammarParser.RoomConnectionContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#items.
    def enterItems(self, ctx:GameGrammarParser.ItemsContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#items.
    def exitItems(self, ctx:GameGrammarParser.ItemsContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#item.
    def enterItem(self, ctx:GameGrammarParser.ItemContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#item.
    def exitItem(self, ctx:GameGrammarParser.ItemContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#secret_items.
    def enterSecret_items(self, ctx:GameGrammarParser.Secret_itemsContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#secret_items.
    def exitSecret_items(self, ctx:GameGrammarParser.Secret_itemsContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#actions.
    def enterActions(self, ctx:GameGrammarParser.ActionsContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#actions.
    def exitActions(self, ctx:GameGrammarParser.ActionsContext):
        pass


    # Enter a parse tree produced by GameGrammarParser#action.
    def enterAction(self, ctx:GameGrammarParser.ActionContext):
        pass

    # Exit a parse tree produced by GameGrammarParser#action.
    def exitAction(self, ctx:GameGrammarParser.ActionContext):
        pass


