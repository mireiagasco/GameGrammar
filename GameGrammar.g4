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
level           : LEVEL IDENTIFIER LEFT_BRACE (room | item | action)* RIGHT_BRACE;
room            : ROOM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL SEMICOLON (roomConnection)* (items)? RIGHT_BRACE;
roomConnection  : IDENTIFIER COLON IDENTIFIER SEMICOLON;
items           : 'items:' LEFT_BRACKET (IDENTIFIER (COMMA IDENTIFIER)*)? RIGHT_BRACKET;
item            : ITEM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL SEMICOLON (actions)? (secret_items)? RIGHT_BRACE;
secret_items    : 'secret_items:' IDENTIFIER (COMMA IDENTIFIER)* SEMICOLON;
actions         : 'actions:' IDENTIFIER (LEFT_PAREN IDENTIFIER (COMMA IDENTIFIER)* RIGHT_PAREN)? (COMMA IDENTIFIER (LEFT_PAREN IDENTIFIER (COMMA IDENTIFIER)* RIGHT_PAREN)?)* SEMICOLON;
action          : ACTION IDENTIFIER LEFT_BRACE RIGHT_BRACE;







