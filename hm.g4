grammar hm;

root : expr
     ;

expr : OPAR expr CPAR               # parenthesis
    | (PLUS | MINUS) expr expr      # arithmetic
    | (PLUS | MINUS) expr           # unary
    | (PLUS | MINUS) PUNTS TIPUS FLEXA TIPUS FLEXA TIPUS #funTipus
    | NUM PUNTS TIPUS               # numTipus
    | expr FLEXA expr               # implication
    | NUM                           # value
    | BARRA ID                      # abstrac
    | ID                            # identification
    ;


OPAR : '(' ;
CPAR : ')' ;
PLUS : '(+)' ;
MINUS : '(-)' ;
BARRA : '\\' ;
FLEXA : '->' ;
PUNTS : '::' ;
NUM : ('0'..'9')+ ;
TIPUS : ('A'..'Z') ;
ID : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;

WS : [ \t\r\n]+ -> skip;