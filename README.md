# Seawolf-script-language-using-ANTLR
Implementing a simple programming language Seawolf script. This is project for course Principle of Programming Languages.

I have used the parser generator ANTLR for python

ANTLR allows for two patterns `Listener` and `Visitor`. I am using the `Visitor` pattern for this project.

- Run the Seawolf interpreter with:
python seawolf.py test_01.expr

Language Definition:
 
* Data Types: this language has three data types:
** Numbers: Integer and Real = Python integer/real type.
** List = Python list.
** String = Python String type.
 
Each type has a literal representation:
- Integer (simplified: only decimals). An integer is represented by one or more digits (0-9). For example, 42 is an integer literal.
- Real  (simplified: no exponents). A real is represented by zero or more digits (0-9) followed by the decimal point "." and zero or more digits (0-9). For example, 3.14159 is a real literal.
- String. A string literal starts with a double quote. This may be followed by zero or more non-double-quote characters. The string ends with a double-quote. The value of the string literal should not include the starting and ending quotes. An example string literal is "Hello SeaWolf.".
- List. A list literal consists of a square bracket, followed by a comma-separated list of zero or more expressions. For example, [ 307, 130, 100+3 ] is a list literal.
 
* Operators: the following operators are listed in precedence order, from highest to lowest (all associative operators are left-associative):

Operator                                              Description

literal                                               The literals given above.
( expression )                                        A parenthesized expression.
a [ b ]                                               Indexing. B may be any expression.
a * b, a / b                                          Multiplication and division (integer and real).
a % b Modulus                                         (divides left hand operand by right hand operand and returns remainder).
a ** b                                                Exponent Performs exponential (power) calculation on operators = a to the power b.
a // b                                                Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
a + b, a - b                                          Addition and subtraction.
a in b                                                Evaluates to true if it finds a variable in the specified sequence and false otherwise.
a < b, a <= b, a == b, a <> b, a > b, a >= b          Comparison.
not a                                                 Boolean NOT.
a and b                                               Boolean AND.
a or b                                                Boolean OR.


The operators have the following semantics:

- Indexing: B must be an integer, a must be either a string or a list. If a is a string, returns the b-th character of the string as a string. If a is a list, returns the b-th element of the list (whatever type it has). The index is zero-based, so the first element is at index 0. If the index is out of bounds, it is a semantic error.
- Addition: A and B must be either both numbers, both strings or both lists. If they are integers or reals, then addition (with standard semantics) is performed. If they are both strings, than string concatenation is performed. If they are both lists, then concatenation of the lists is performed.
- Multiplication, Division and Subtraction: A and B must be integers or reals. For division only, B must not be 0. These are performed using standard multiplication semantics.
- Comparison: A and B must be integers. The two integers are compared, and the result is 1 if the comparison is true, and 0 if the comparison is false.
- Boolean AND, OR, NOT: A and, if present, B must be integers. If the integer is 0, then it is considered false. All other integers are true. The boolean operation is performed. If its true, the result of the expression is the integer 1, otherwise it is the integer 0.
 

Each expression prints one of three possible outputs:

- If the line contains a syntax error : SYNTAX ERROR.
- If one of the "must" conditions given above is violated when evaluating it : SEMANTIC ERROR.
- Otherwise evalute the expression and print the result.
 
An example input file (inputFile.expr) might look like:
1 - 2 + 3
1 2 3
42 + "Red"
1 - (2 + 3)
"Hello" + " " + "SeaWolf."
[1, 2, 3][0] + 40


The output from this file should look like:
2
SYNTAX ERROR
SEMANTIC ERROR
-4
'Hello SeaWolf'
41


The program can be run with a command like:
python3 seawolf.py inputFile.expr

or can be run in an IDE with command line inputs.
