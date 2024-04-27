grammar hm;

root : expr
     ;

expr : OPAR expr CPAR
    | (PLUS | MINUS) expr expr
    | ID FLEXA expr
    | NUM
    | ID
    ;


OPAR : '(' ;
CPAR : ')' ;
PLUS : '+' ;
MINUS : '-' ;
FLEXA: '->' ;
NUM : ('0'..'9')+ ;
ID : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;

WS : [ \t\r\n]+ -> skip;