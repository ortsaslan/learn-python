# Lambda functions

## DEFINING A LAMBDA FUNCTIONS

Lambda function is anonymous function that uses for quick calculations, as throwaway single-line function.

    lambda arguments: expression
    lambda x: x * 2

Lambda function defines only in single-line form. For implement condition in lambdas we use ternary operator.

    lambda x, y: x + y if x > 0 else x - y

## INVOKING LAMBDA FUNCTIONS

Lambda function can be assigned to variable, then called by it's name.

    doubler = lambda x: x * 2
    doubler(5)  ->  10

Also lamda function can be called right-away in place. To do that we need put into parentheses function itself and arguments too.

    (lambda y: y + y)(3, 5)

## WHEN IS IT USEFUL?

Lambdas can be usefull as key-functions that pass to filter, sort, map functions.

    lst = [...]
    lst.sort(lambda x: x[-1])

Also it handy in combination with another function.

    def greet(hello):
        return lambda name: hello + name

    say = greet('Hi, ')
    say('John')     -> 'Hi, John'
