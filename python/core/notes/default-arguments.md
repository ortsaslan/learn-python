# Default arguments

## DEFAULTS

Functions in Python can be defined with default parameters. This parameters is specified in function definition and contain default values. When parameter wich defined as default not specified at function call, it will be pass to function by default value. If default parameter specified at function call, specified value will be pass.

    def buy_fruits(name, weight=1):
        print(f"Give me {weight} kg of {name}")

    buy_fruits("apples")    ->  "Give me 1 kg of apples"
    buy_fruits("oranges", 2)    ->  "Give me 2 kg of oranges"

## MUTABLE OBJECTS AS DEFAULTS

There differences in behavior of function in which default parameters defined as mutable objects (e.g. list). When we call this function without specifying default parameter first time function creates mutable object by default and  uses it in all following calls, instead of creating new objects at every new call.

    def buy_fruits = (name, basket=[]):
        basket.append(name)
        return basket

    my_basket = buy_fruits("apples")    ->  ['apples']
    friends_basket = buy_fruits("coconuts") ->  ['apples', 'coconuts']

To avoid this behavior we assign `None` to default parameter wich should take mutable object as value.

    def buy_fruits(name, basket=None):
        if basket == None:
            basket = []
        basket.append(name)
        return basket

## PEP TIME

According to PEP 8, we don't use spaces around `=` when define default parameters.

    wrong: *parameter = value*
    correct: *parameter=value*
