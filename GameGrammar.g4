grammar GameGrammar;

// Lexer rules
WS              : [ \t\n\r]+ -> skip;  // Define whitespace rule to be skipped
ROOM            : 'room';
ITEM            : 'item';
ACTION          : 'action';
IF              : 'if';
ELSE            : 'else';
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;  // Updated to allow underscores
STRING_LITERAL  : '"' (~["\r\n])* '"';      // Updated to allow strings with double quotes
COLON           : ':';
COMMA           : ',';
SEMICOLON       : ';';
LEFT_BRACE      : '{';
RIGHT_BRACE     : '}';
LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
PERIOD          : '.';
PRINT           : 'print';

// Parser rules
gameScript      : (room | item | action)*;

room            : ROOM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL (roomConnection)* RIGHT_BRACE;
roomConnection  : IDENTIFIER COLON IDENTIFIER SEMICOLON;

item            : ITEM IDENTIFIER LEFT_BRACE 'description:' STRING_LITERAL (action)? RIGHT_BRACE;
action          : ACTION IDENTIFIER LEFT_BRACE (IF LEFT_PAREN condition RIGHT_PAREN block (ELSE block)?)? RIGHT_BRACE;
condition       : IDENTIFIER PERIOD IDENTIFIER LEFT_PAREN (STRING_LITERAL | IDENTIFIER) RIGHT_PAREN;
block           : LEFT_BRACE (printStatement)+ RIGHT_BRACE;
printStatement  : PRINT LEFT_PAREN STRING_LITERAL RIGHT_PAREN SEMICOLON;
