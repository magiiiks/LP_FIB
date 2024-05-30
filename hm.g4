grammar hm;

root : expr
     ;

expr : OPAR expr CPAR               # parenthesis
    | expr expr                     # implication 
    | BARRA ID FLEXA expr           # abstrac
    | expr PUNTS (funtipus | TIPUS) # Tipus
    | (PLUS | MINUS)                # operator
    | NUM                           # value
    | ID                            # identification
    ;


funtipus : TIPUS FLEXA funtipus      #funTipus 
         | TIPUS FLEXA TIPUS         #finTipus
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