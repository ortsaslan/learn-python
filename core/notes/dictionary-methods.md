# Dictionary methods

## CREATING

`dict.fromkeys(key, val)`

Create dictionary from passed arguments. Key-argument should be sequence, that will be used to create keys in new dictionary, i.e. ['a', 'b', 'c'] or 'abc' -> {'a':, 'b':, 'c':}. Val-argument is optional, if it not passed val for all keys will be None.
But if it passed, it will be a same value for all keys. Val-argument can be iterable or not.

## ADDING

`dict.update()`

This method add value that passed in into dictionary. We can pass in it another dictionary, or argument with assigned value:

    dict.update({'one': 1})
    dict.update(one=1)

In both cases we will receive a flat dictionary, not a dictionary of dictionaries.

## GETTING and REMOVING

**Get**. We can get value of item in dictionary by it's key in two ways - `dict[key]` or
dict.get(key). Both methods return a value, but have different behavior in case when
there is no such a key in dictionary. []-method return KeyError, get()-method return None.
And there is another difference - we can set the default value that will be return in such case:
`dict.get(key, default_value)`

**Remove**. There is two ways to remove an item - `dict.pop()` and `dict.popitem()`. Both methods remove item (key-val pair), but their return is different - `pop()` return only value,
`popitem()` return item entirely (key and value).
Second difference is `pop()` remove item by it's key, thus we must pass in it key-argument ->
`dict.pop(key)`. But `popitem()` method remove last item in dictionary, and we don't pass in it any argument at all.
Third difference is behavior when there is no a such key in dictionary. `popitem()` will return
KeyError. `pop()` return KeyError, but we can pass a default value -> `dict.pop(key, default_val)`

## CLEANING

There is two methods for cleaning a dictionary - `del` and `clear()`. With del method we can delete whole dictionary or only one of the items: del dict, del `dict[key]`.
Method `clear()` delete only items entirely, but not dictionary it self. After calling this method dictionary becomes empty. Also, `clear()` method remove all items not only in dictionary on which it called, but in all dictionaries referenced to same dict-object:

    dict1 = {'a': 1, 'b': 2}
    dict2 = dict1
    dict1.clear()  -> dict1 == {} and dict2 == {}

These methods do not return anything!
