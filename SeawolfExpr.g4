grammar SeawolfExpr;

prog:   stat+ ;

stat:   expr NEWLINE                                        # PrintExpr
    |   NEWLINE                                             # Blank
    ;

expr:   op=SUB expr                                         # NegNum
    |   '(' expr ')'                                        # Parens
    |   expr op=(MUL|DIV) expr                              # MulDiv
    |   expr op=MOD expr                                    # Modulus
    |   <assoc=right>   expr op=EXP expr                    # Exponent
    |   expr op=FLRDIV expr                                 # FloorDivision
    |   expr op=(ADD|SUB) expr                              # AddSub
    |   expr op=(LESS|LESSEQ|GRT|GRTEQ|EQUAL|NOTEQ) expr    # Logical
    |   op=NOT expr                                         # BinaryNot
    |   expr op=AND expr                                    # BinaryAnd
    |   expr op=OR expr                                     # BinaryOr
    |   expr op=IN expr                                     # Search
    |   INT                                                 # Int
    |   REAL                                                # Real
    |   ID                                                  # String
    |   '[' list_expr ']'                                   # List
    |   expr '[' expr ']'                                   # IndexList
    ;

list_expr : expr ',' list_expr
          | expr
          |
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
ID      :   '"' [a-zA-Z]+ '"' ;                     // match identifiers
NEWLINE :'\r'? '\n' ;                               // return newlines to parser (is end-statement signal)
WS      : [ \t\r\n]+ -> skip ;                      // skip spaces, tabs, newlines