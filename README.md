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
 
For this assignment, we add support for variables, conditionals, looping, and output.

Variable names must begin with an ASCII letter, which may be followed by zero or more ASCII letters, digits and underscore. A regular expression that matches variable names is '[A-Za-z][A-Za-z0-9_]*'.

For now, our script has only a single scope for variables: a global static scope.

Our expressions from the previous assignment need to be extended in two ways: we need to add support for variables by extending the grammar so that variables can be used wherever a literal can be used. Evaluating a variable in an expression should have the following behavior: if the variable has had a value assigned to it, the value should be returned. Otherwise, a semantic error should be generated. When a variable is used as a location (on the left-hand side of an assignment), then a variable location is used.

There are 5 kinds of statements:

- Block: a block statement consists of zero-or-more statements enclosed in curly braces {...}. When the block executes, each of the statements in the block is executed in sequential order.

- Assignment: an assignment statement consists of a variable, an equals sign, an expression, and a semicolon. When the assignment statement executes, the right-expression is evaluated for the value and it is assigned to the left variable. Notice that this does not support multiple assignment equals as in python: a,b=1,2;

- If: an if statement consists of the keyword "if", a left-parenthesis, an expression, a right-parenthesis, and a block body statement. Optionally, there might be an "else block". When the if statement executes, the expression is evaluated. If that value is not zero, the "then block" is executed, else the "else block" is executed.

- While: a  while statement consists of the keyword "while", a left-parenthesis, an expression, a right-parenthesis, and a body statement. Executing the while statement begins by evaluating the condition for an value. If the value is 0, the while statement terminates. Otherwise, the while statement executes its body statement, and execution repeats.

- Print: a print statement consists of the "print" keyword, a left-parenthesis, an expression, a right-parenthesis, and a semicolon. When the print statement executes, the expression is evaluated for a value and printed using the python print statement.

A program consists of a single outermost statement, which may contain statements inside it. Usually, this is a block statement, but any statement is valid. Executing the program consists of executing this outermost statement. When the outermost statement finishes executing, the program terminates.

Your interpreter will be called with a single argument. This argument will be a file containing a program. If the program contains syntax error, your interpreter should print out: SYNTAX ERROR. Otherwise, you should execute the program. If the execution of the program causes a semantic error, then your interpreter should print out: SEMANTIC ERROR. Execution of the program may cause print statements to execute. Output from print statements should be sent to standard output. No other output should be produced. An example input script might look like:

Example 1:

{

  number = 100;

  isPrime = 1;

  i = 2;

  while(isPrime==1 and i) {

    if (number%i==0) {

      isPrime = 0;

    }

   i = i + 1;

  }

  if(isPrime==1){

    print("isPrime is true");

  } else {

    print("isPrime is false");

  }

}

Output: isPrime is false

Example 2:

{

  number1 = 125;

  number2 = 210;

  print("The minimum is: ");

  if (number1 < number2) {

    print(number1);

  } else {

    print(number2);

  }

}

Output: The minimum is: 125

Example 3: minIndex in an array

{

  data = [ 300, 125, 12, 65, 9943, 9000 ];

  min = data[0];

  minIndex = 0;

  i = 1;

  while (i < 6){

    if (data[i] < min){

       min = data[i];

       minIndex = i;

    }

   i = i + 1;

  }

  print(minIndex);

}

Output: 2

Example 4:

{

  number1 = 25;

  number2 = 10;

  while(number1 <> number2) {

    if (number1 > number2) {

      number1 = number1 - number2;

    } else {

      number2 = number2 - number1;

    }

  }

  print("The greatest common divider is: ");

  print(number1);

}

Output: The greatest common divider is: 5

Example 5:

{

    data = [ [ 100, 42 ], [ 100, 50 ], [ 123, 456 ], [ 300, 9000 ] ];

    result = [ 0, 0, 0, 0 ];

    i = 0;

    while (i < 4){

        a = data[i][0];

        b = data[i][1];

        if (a > 0){

            while (b > 0){

                if (a > b){

                    a = a - b;

                } else {

                    b = b - a;

                }

           }

        }

        result[i] = a;

        i = i + 1;

    }

    print(result);

}

Output: [2, 50, 3, 300]