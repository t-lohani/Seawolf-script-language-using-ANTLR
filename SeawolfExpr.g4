grammar SeawolfExpr;

prog:   stat ;

stat:   VAR('[' expr ']')* '=' expr ';'                     # AssignStat
    |   NEWLINE                                             # BlankStat
    |   block                                               # BlockStat
    |   'if' '(' expr ')' block ('else' block)?             # IfElseStat
    |   'while' '(' expr ')' block                          # WhileStat
    |   'print' '(' expr ')' ';'                            # PrintStat
    ;

block:  '{' stat* '}' ;

expr:   op=SUB expr                                         # NegNum
    |   '(' expr ')'                                        # Parens
    |   expr '[' expr ']'                                   # IndexList
    |   expr op=(MUL|DIV) expr                              # MulDiv
    |   expr op=MOD expr                                    # Modulus
    |   expr op=EXP expr                                    # Exponent
    |   expr op=FLRDIV expr                                 # FloorDivision
    |   expr op=(ADD|SUB) expr                              # AddSub
    |   expr op=IN expr                                     # Search
    |   expr op=(LESS|LESSEQ|GRT|GRTEQ|EQUAL|NOTEQ) expr    # Logical
    |   op=NOT expr                                         # BinaryNot
    |   expr op=AND expr                                    # BinaryAnd
    |   expr op=OR expr                                     # BinaryOr
    |   INT                                                 # Int
    |   VAR                                                 # Var
    |   REAL                                                # Real
    |   '[' list_expr ']'                                   # List
    |   STRING                                              # String
    ;

list_expr : expr ',' list_expr
          | expr
          ;

MUL     :   '*' ;                                   // Multiplication operator
DIV     :   '/' ;                                   // Division operator
ADD     :   '+' ;                                   // Addition operator
SUB     :   '-' ;                                   // Subtraction operator
MOD     :   '%' ;                                   // Modulus operator
EXP     :   '**' ;                                  // Exponential operator
FLRDIV  :   '//' ;                                  // Floor Division
LESS    :   '<' ;                                   // Less than
LESSEQ  :   '<=' ;                                  // Less than or equal
GRT     :   '>' ;                                   // Greater than
GRTEQ   :   '>=' ;                                  // Greater than or equal
EQUAL   :   '==' ;                                  // Equal to
NOTEQ   :   '<>' ;                                  // Not equal to
NOT     :   'not' ;                                 // Binary NOT
AND     :   'and' ;                                 // Binary AND
OR      :   'or' ;                                  // Binary OR
IN      :   'in' ;                                  // List 'in'
INT     :   [0-9]+ ;                                // match integers
REAL    :   [0-9]* ('.'[0-9] | [0-9]'.') [0-9]* ;   // match reals
STRING  :   '"' .*? '"' ;                           // match identifiers
VAR     :   [A-Za-z][A-Za-z0-9_]* ;                 // match variables
NEWLINE :   '\r'? '\n' ;                            // return newlines to parser (is end-statement signal)
WS      :   [ \t\r\n]+ -> skip ;                        // skip spaces, tabs, newlines