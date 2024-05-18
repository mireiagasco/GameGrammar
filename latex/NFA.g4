grammar NFA;

automaton      : 'nfa' '{' (state | transition)* '}';

state          : 'state' IDENTIFIER '{' stateProperty* '}';
stateProperty  : 'initial' | 'final';

transition     : 'transition' IDENTIFIER '->' IDENTIFIER ':' SYMBOL ';';

SYMBOL         : [a-zA-Z];
IDENTIFIER     : [a-zA-Z][a-zA-Z0-9]* ;

WS             : [ \t\r\n]+ -> skip;

