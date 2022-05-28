# Operations with dictionary

## MEMBERSHIP TESTING IN DICTIONARY

When we need to check wether a specific item in present dictionary there is two operators `in`
and `not in`. E.g.:
    'sofa' in catalog
    'table' not in catalog
Operators look only for keys, not values. Returns `True` if key exists, and `False` otherwise.

## ITERATING OVER KEYS

For iterating over keys in dictionary we can use `for` loop. E.g.:
    dict = {'a': 1, 'b': 2}
    for item in dict:
        print(item) -> 'a', 'b'
Second way to iterate over keys is `keys` method, which creates special iterable object - a collection of dictionary keys (dict_keys). E.g.:
    print(dict.keys())  ->  dict_keys(['a', 'b'])

## INCLUDING VALUES IN ITERATION

If we want to get value when iterating, we should use `values` method. E.g.:
    for value in dict.values():
        print(value)    ->  1, 2, 3

## KEYS AND VALUES

Also there is method `items` that provides complete iteration in case when we need both keys and values. It returns the collection of `(key, value)` pairs (tuples):
    for item in dict.items():
    print(item) ->  ('a', 1) ('b', 2)

## DICTIONARY COMPREHENSION

Dictionary comprehension is convenient and concise way to create a new dictionary.
    dictionary = {key: val for element in iterable}
    dictionary = {key + 5: 'val' for key in range(2)}   ->  {5: 'val', 6: 'val'}
    dictionary = {n+10: n+100 for n in range(2)}    ->  {10: 100, 11: 101}
Dictionary comprehension more often used to create new dictionary be changing values in another dictionary.
    dict1 = {1: 'val-1', 2: 'val-2'}
    dict2 = {key: 'new-' + val for (key, val) in dict1.items()} ->  {1: 'new-val-1', 2: 'new-val-2'}
We can implement condition to dictionary expression
