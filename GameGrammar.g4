grammar GameGrammar;

// Lexer rules
WS              : [ \t\n\r]+ -> skip;  // Define whitespace rule to be skipped
LEVEL           : 'level';
ROOM            : 'room';
ITEM            : 'item';
ACTION          : 'action';
IF              : 'if';
ELSE            : 'else';
PRINT           : 'print';
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;  // Updated to allow underscores
STRING_LITERAL  : '"' (~["\r\n])* '"';      // Updated to allow strings with double quotes
COLON           : ':';
COMMA           : ',';
SEMICOLON       : ';';
LEFT_BRACE      : '{';
RIGHT_BRACE     : '}';
LEFT_BRACKET    : '[';
RIGHT_BRACKET   : ']';
LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
PERIOD          : '.';

// Parser rules
gameScript      : level;
level           : LEVEL IDENTIFIER LEFT_BRACE (room | item)* RIGHT_BRACE;
room            : ROOM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL (roomConnection)* (items)? RIGHT_BRACE;
roomConnection  : IDENTIFIER COLON IDENTIFIER SEMICOLON;
items           : 'items:' LEFT_BRACKET (IDENTIFIER (COMMA IDENTIFIER)*)? RIGHT_BRACKET;
item            : ITEM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL (action)? RIGHT_BRACE;
action          : ACTION COLON IDENTIFIER (COMMA IDENTIFIER)* SEMICOLON;








