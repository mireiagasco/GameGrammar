# Generated from GameGrammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63\n")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("A\n\6\5\6C\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\6\bP\n\b\r\b\16\bQ\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\3\2\n\13\2[\2\27\3")
        buf.write("\2\2\2\4\32\3\2\2\2\6\'\3\2\2\2\b,\3\2\2\2\n\66\3\2\2")
        buf.write("\2\fF\3\2\2\2\16M\3\2\2\2\20U\3\2\2\2\22\26\5\4\3\2\23")
        buf.write("\26\5\b\5\2\24\26\5\n\6\2\25\22\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\3\3\2\2\2\31\27\3\2\2\2\32\33\7\5\2\2\33\34\7\n")
        buf.write("\2\2\34\35\7\17\2\2\35\36\7\3\2\2\36\"\7\13\2\2\37!\5")
        buf.write("\6\4\2 \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3")
        buf.write("\2\2\2$\"\3\2\2\2%&\7\20\2\2&\5\3\2\2\2\'(\7\n\2\2()\7")
        buf.write("\f\2\2)*\7\n\2\2*+\7\16\2\2+\7\3\2\2\2,-\7\6\2\2-.\7\n")
        buf.write("\2\2./\7\17\2\2/\60\7\3\2\2\60\62\7\13\2\2\61\63\5\n\6")
        buf.write("\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\65\7\20")
        buf.write("\2\2\65\t\3\2\2\2\66\67\7\7\2\2\678\7\n\2\28B\7\17\2\2")
        buf.write("9:\7\b\2\2:;\7\21\2\2;<\5\f\7\2<=\7\22\2\2=@\5\16\b\2")
        buf.write(">?\7\t\2\2?A\5\16\b\2@>\3\2\2\2@A\3\2\2\2AC\3\2\2\2B9")
        buf.write("\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\7\20\2\2E\13\3\2\2\2FG")
        buf.write("\7\n\2\2GH\7\23\2\2HI\7\n\2\2IJ\7\21\2\2JK\t\2\2\2KL\7")
        buf.write("\22\2\2L\r\3\2\2\2MO\7\17\2\2NP\5\20\t\2ON\3\2\2\2PQ\3")
        buf.write("\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\7\20\2\2T\17\3")
        buf.write("\2\2\2UV\7\24\2\2VW\7\21\2\2WX\7\13\2\2XY\7\22\2\2YZ\7")
        buf.write("\16\2\2Z\21\3\2\2\2\t\25\27\"\62@BQ")
        return buf.getvalue()


class GameGrammarParser ( Parser ):

    grammarFileName = "GameGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'description:'", "<INVALID>", "'room'", 
                     "'item'", "'action'", "'if'", "'else'", "<INVALID>", 
                     "<INVALID>", "':'", "','", "';'", "'{'", "'}'", "'('", 
                     "')'", "'.'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "ROOM", "ITEM", "ACTION", 
                      "IF", "ELSE", "IDENTIFIER", "STRING_LITERAL", "COLON", 
                      "COMMA", "SEMICOLON", "LEFT_BRACE", "RIGHT_BRACE", 
                      "LEFT_PAREN", "RIGHT_PAREN", "PERIOD", "PRINT" ]

    RULE_gameScript = 0
    RULE_room = 1
    RULE_roomConnection = 2
    RULE_item = 3
    RULE_action = 4
    RULE_condition = 5
    RULE_block = 6
    RULE_printStatement = 7

    ruleNames =  [ "gameScript", "room", "roomConnection", "item", "action", 
                   "condition", "block", "printStatement" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    ROOM=3
    ITEM=4
    ACTION=5
    IF=6
    ELSE=7
    IDENTIFIER=8
    STRING_LITERAL=9
    COLON=10
    COMMA=11
    SEMICOLON=12
    LEFT_BRACE=13
    RIGHT_BRACE=14
    LEFT_PAREN=15
    RIGHT_PAREN=16
    PERIOD=17
    PRINT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GameScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def room(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.RoomContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.RoomContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.ItemContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.ItemContext,i)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.ActionContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.ActionContext,i)


        def getRuleIndex(self):
            return GameGrammarParser.RULE_gameScript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameScript" ):
                listener.enterGameScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameScript" ):
                listener.exitGameScript(self)




    def gameScript(self):

        localctx = GameGrammarParser.GameScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gameScript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GameGrammarParser.ROOM) | (1 << GameGrammarParser.ITEM) | (1 << GameGrammarParser.ACTION))) != 0):
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GameGrammarParser.ROOM]:
                    self.state = 16
                    self.room()
                    pass
                elif token in [GameGrammarParser.ITEM]:
                    self.state = 17
                    self.item()
                    pass
                elif token in [GameGrammarParser.ACTION]:
                    self.state = 18
                    self.action()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RoomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOM(self):
            return self.getToken(GameGrammarParser.ROOM, 0)

        def IDENTIFIER(self):
            return self.getToken(GameGrammarParser.IDENTIFIER, 0)

        def LEFT_BRACE(self):
            return self.getToken(GameGrammarParser.LEFT_BRACE, 0)

        def STRING_LITERAL(self):
            return self.getToken(GameGrammarParser.STRING_LITERAL, 0)

        def RIGHT_BRACE(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACE, 0)

        def roomConnection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.RoomConnectionContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.RoomConnectionContext,i)


        def getRuleIndex(self):
            return GameGrammarParser.RULE_room

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom" ):
                listener.enterRoom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom" ):
                listener.exitRoom(self)




    def room(self):

        localctx = GameGrammarParser.RoomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_room)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GameGrammarParser.ROOM)
            self.state = 25
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 26
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 27
            self.match(GameGrammarParser.T__0)
            self.state = 28
            self.match(GameGrammarParser.STRING_LITERAL)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GameGrammarParser.IDENTIFIER:
                self.state = 29
                self.roomConnection()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(GameGrammarParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RoomConnectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.IDENTIFIER)
            else:
                return self.getToken(GameGrammarParser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(GameGrammarParser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(GameGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_roomConnection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoomConnection" ):
                listener.enterRoomConnection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoomConnection" ):
                listener.exitRoomConnection(self)




    def roomConnection(self):

        localctx = GameGrammarParser.RoomConnectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_roomConnection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 38
            self.match(GameGrammarParser.COLON)
            self.state = 39
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 40
            self.match(GameGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITEM(self):
            return self.getToken(GameGrammarParser.ITEM, 0)

        def IDENTIFIER(self):
            return self.getToken(GameGrammarParser.IDENTIFIER, 0)

        def LEFT_BRACE(self):
            return self.getToken(GameGrammarParser.LEFT_BRACE, 0)

        def STRING_LITERAL(self):
            return self.getToken(GameGrammarParser.STRING_LITERAL, 0)

        def RIGHT_BRACE(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACE, 0)

        def action(self):
            return self.getTypedRuleContext(GameGrammarParser.ActionContext,0)


        def getRuleIndex(self):
            return GameGrammarParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = GameGrammarParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GameGrammarParser.ITEM)
            self.state = 43
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 44
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 45
            self.match(GameGrammarParser.T__0)
            self.state = 46
            self.match(GameGrammarParser.STRING_LITERAL)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GameGrammarParser.ACTION:
                self.state = 47
                self.action()


            self.state = 50
            self.match(GameGrammarParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTION(self):
            return self.getToken(GameGrammarParser.ACTION, 0)

        def IDENTIFIER(self):
            return self.getToken(GameGrammarParser.IDENTIFIER, 0)

        def LEFT_BRACE(self):
            return self.getToken(GameGrammarParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACE, 0)

        def IF(self):
            return self.getToken(GameGrammarParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(GameGrammarParser.LEFT_PAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(GameGrammarParser.ConditionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(GameGrammarParser.RIGHT_PAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(GameGrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = GameGrammarParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(GameGrammarParser.ACTION)
            self.state = 53
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 54
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GameGrammarParser.IF:
                self.state = 55
                self.match(GameGrammarParser.IF)
                self.state = 56
                self.match(GameGrammarParser.LEFT_PAREN)
                self.state = 57
                self.condition()
                self.state = 58
                self.match(GameGrammarParser.RIGHT_PAREN)
                self.state = 59
                self.block()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GameGrammarParser.ELSE:
                    self.state = 60
                    self.match(GameGrammarParser.ELSE)
                    self.state = 61
                    self.block()




            self.state = 66
            self.match(GameGrammarParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.IDENTIFIER)
            else:
                return self.getToken(GameGrammarParser.IDENTIFIER, i)

        def PERIOD(self):
            return self.getToken(GameGrammarParser.PERIOD, 0)

        def LEFT_PAREN(self):
            return self.getToken(GameGrammarParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GameGrammarParser.RIGHT_PAREN, 0)

        def STRING_LITERAL(self):
            return self.getToken(GameGrammarParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = GameGrammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 69
            self.match(GameGrammarParser.PERIOD)
            self.state = 70
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 71
            self.match(GameGrammarParser.LEFT_PAREN)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==GameGrammarParser.IDENTIFIER or _la==GameGrammarParser.STRING_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.match(GameGrammarParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(GameGrammarParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACE, 0)

        def printStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameGrammarParser.PrintStatementContext)
            else:
                return self.getTypedRuleContext(GameGrammarParser.PrintStatementContext,i)


        def getRuleIndex(self):
            return GameGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GameGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.printStatement()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GameGrammarParser.PRINT):
                    break

            self.state = 81
            self.match(GameGrammarParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrintStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GameGrammarParser.PRINT, 0)

        def LEFT_PAREN(self):
            return self.getToken(GameGrammarParser.LEFT_PAREN, 0)

        def STRING_LITERAL(self):
            return self.getToken(GameGrammarParser.STRING_LITERAL, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GameGrammarParser.RIGHT_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(GameGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = GameGrammarParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(GameGrammarParser.PRINT)
            self.state = 84
            self.match(GameGrammarParser.LEFT_PAREN)
            self.state = 85
            self.match(GameGrammarParser.STRING_LITERAL)
            self.state = 86
            self.match(GameGrammarParser.RIGHT_PAREN)
            self.state = 87
            self.match(GameGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





