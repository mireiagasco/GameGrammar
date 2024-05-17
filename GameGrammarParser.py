# Generated from GameGrammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4%\n\4\f\4\16")
        buf.write("\4(\13\4\3\4\5\4+\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\5\6>\n\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\7\bQ\n\b\f\b\16\bT\13\b\3\b\3\b\3\b\2\2\t")
        buf.write("\2\4\6\b\n\f\16\2\2\2X\2\20\3\2\2\2\4\22\3\2\2\2\6\36")
        buf.write("\3\2\2\2\b.\3\2\2\2\n\63\3\2\2\2\fA\3\2\2\2\16K\3\2\2")
        buf.write("\2\20\21\5\4\3\2\21\3\3\2\2\2\22\23\7\6\2\2\23\24\7\r")
        buf.write("\2\2\24\31\7\22\2\2\25\30\5\6\4\2\26\30\5\f\7\2\27\25")
        buf.write("\3\2\2\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\23\2\2")
        buf.write("\35\5\3\2\2\2\36\37\7\7\2\2\37 \7\r\2\2 !\7\22\2\2!\"")
        buf.write("\7\3\2\2\"&\7\16\2\2#%\5\b\5\2$#\3\2\2\2%(\3\2\2\2&$\3")
        buf.write("\2\2\2&\'\3\2\2\2\'*\3\2\2\2(&\3\2\2\2)+\5\n\6\2*)\3\2")
        buf.write("\2\2*+\3\2\2\2+,\3\2\2\2,-\7\23\2\2-\7\3\2\2\2./\7\r\2")
        buf.write("\2/\60\7\17\2\2\60\61\7\r\2\2\61\62\7\21\2\2\62\t\3\2")
        buf.write("\2\2\63\64\7\4\2\2\64=\7\24\2\2\65:\7\r\2\2\66\67\7\20")
        buf.write("\2\2\679\7\r\2\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2")
        buf.write("\2\2;>\3\2\2\2<:\3\2\2\2=\65\3\2\2\2=>\3\2\2\2>?\3\2\2")
        buf.write("\2?@\7\25\2\2@\13\3\2\2\2AB\7\b\2\2BC\7\r\2\2CD\7\22\2")
        buf.write("\2DE\7\3\2\2EG\7\16\2\2FH\5\16\b\2GF\3\2\2\2GH\3\2\2\2")
        buf.write("HI\3\2\2\2IJ\7\23\2\2J\r\3\2\2\2KL\7\t\2\2LM\7\17\2\2")
        buf.write("MR\7\r\2\2NO\7\20\2\2OQ\7\r\2\2PN\3\2\2\2QT\3\2\2\2RP")
        buf.write("\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7\21\2\2V\17")
        buf.write("\3\2\2\2\n\27\31&*:=GR")
        return buf.getvalue()


class GameGrammarParser ( Parser ):

    grammarFileName = "GameGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'description:'", "'items:'", "<INVALID>", 
                     "'level'", "'room'", "'item'", "'action'", "'if'", 
                     "'else'", "'print'", "<INVALID>", "<INVALID>", "':'", 
                     "','", "';'", "'{'", "'}'", "'['", "']'", "'('", "')'", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "LEVEL", 
                      "ROOM", "ITEM", "ACTION", "IF", "ELSE", "PRINT", "IDENTIFIER", 
                      "STRING_LITERAL", "COLON", "COMMA", "SEMICOLON", "LEFT_BRACE", 
                      "RIGHT_BRACE", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_PAREN", 
                      "RIGHT_PAREN", "PERIOD" ]

    RULE_gameScript = 0
    RULE_level = 1
    RULE_room = 2
    RULE_roomConnection = 3
    RULE_items = 4
    RULE_item = 5
    RULE_action = 6

    ruleNames =  [ "gameScript", "level", "room", "roomConnection", "items", 
                   "item", "action" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    LEVEL=4
    ROOM=5
    ITEM=6
    ACTION=7
    IF=8
    ELSE=9
    PRINT=10
    IDENTIFIER=11
    STRING_LITERAL=12
    COLON=13
    COMMA=14
    SEMICOLON=15
    LEFT_BRACE=16
    RIGHT_BRACE=17
    LEFT_BRACKET=18
    RIGHT_BRACKET=19
    LEFT_PAREN=20
    RIGHT_PAREN=21
    PERIOD=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GameScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def level(self):
            return self.getTypedRuleContext(GameGrammarParser.LevelContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.level()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LevelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEVEL(self):
            return self.getToken(GameGrammarParser.LEVEL, 0)

        def IDENTIFIER(self):
            return self.getToken(GameGrammarParser.IDENTIFIER, 0)

        def LEFT_BRACE(self):
            return self.getToken(GameGrammarParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACE, 0)

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


        def getRuleIndex(self):
            return GameGrammarParser.RULE_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLevel" ):
                listener.enterLevel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLevel" ):
                listener.exitLevel(self)




    def level(self):

        localctx = GameGrammarParser.LevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_level)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(GameGrammarParser.LEVEL)
            self.state = 17
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 18
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GameGrammarParser.ROOM or _la==GameGrammarParser.ITEM:
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GameGrammarParser.ROOM]:
                    self.state = 19
                    self.room()
                    pass
                elif token in [GameGrammarParser.ITEM]:
                    self.state = 20
                    self.item()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(GameGrammarParser.RIGHT_BRACE)
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


        def items(self):
            return self.getTypedRuleContext(GameGrammarParser.ItemsContext,0)


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
        self.enterRule(localctx, 4, self.RULE_room)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(GameGrammarParser.ROOM)
            self.state = 29
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 30
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 31
            self.match(GameGrammarParser.T__0)
            self.state = 32
            self.match(GameGrammarParser.STRING_LITERAL)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GameGrammarParser.IDENTIFIER:
                self.state = 33
                self.roomConnection()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GameGrammarParser.T__1:
                self.state = 39
                self.items()


            self.state = 42
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
        self.enterRule(localctx, 6, self.RULE_roomConnection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 45
            self.match(GameGrammarParser.COLON)
            self.state = 46
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 47
            self.match(GameGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(GameGrammarParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(GameGrammarParser.RIGHT_BRACKET, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.IDENTIFIER)
            else:
                return self.getToken(GameGrammarParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.COMMA)
            else:
                return self.getToken(GameGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GameGrammarParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)




    def items(self):

        localctx = GameGrammarParser.ItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_items)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GameGrammarParser.T__1)
            self.state = 50
            self.match(GameGrammarParser.LEFT_BRACKET)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GameGrammarParser.IDENTIFIER:
                self.state = 51
                self.match(GameGrammarParser.IDENTIFIER)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GameGrammarParser.COMMA:
                    self.state = 52
                    self.match(GameGrammarParser.COMMA)
                    self.state = 53
                    self.match(GameGrammarParser.IDENTIFIER)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 61
            self.match(GameGrammarParser.RIGHT_BRACKET)
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
        self.enterRule(localctx, 10, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(GameGrammarParser.ITEM)
            self.state = 64
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 65
            self.match(GameGrammarParser.LEFT_BRACE)
            self.state = 66
            self.match(GameGrammarParser.T__0)
            self.state = 67
            self.match(GameGrammarParser.STRING_LITERAL)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GameGrammarParser.ACTION:
                self.state = 68
                self.action()


            self.state = 71
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

        def COLON(self):
            return self.getToken(GameGrammarParser.COLON, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.IDENTIFIER)
            else:
                return self.getToken(GameGrammarParser.IDENTIFIER, i)

        def SEMICOLON(self):
            return self.getToken(GameGrammarParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GameGrammarParser.COMMA)
            else:
                return self.getToken(GameGrammarParser.COMMA, i)

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
        self.enterRule(localctx, 12, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(GameGrammarParser.ACTION)
            self.state = 74
            self.match(GameGrammarParser.COLON)
            self.state = 75
            self.match(GameGrammarParser.IDENTIFIER)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GameGrammarParser.COMMA:
                self.state = 76
                self.match(GameGrammarParser.COMMA)
                self.state = 77
                self.match(GameGrammarParser.IDENTIFIER)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(GameGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





