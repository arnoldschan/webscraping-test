# Web scraper technical test

Test overview:
- 30% Data structure & Algorithm understanding 
- 15% Object-oriented programming
- 15% MongoDB understanding
- 40% Web scraping basic project


## Data structure & Algorithm understanding (20%) time: 20 minutes

Generate all possible 2 pair of letters from inputted string, dropping any duplicates
result is in list, the order is up to you
Example:
``` python
input: "abc"
output: ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
```

Example 2:
``` python
input: "bba"
output: ['bb', 'ba', 'ab']
```
Example 3:
``` python
input: "bbbcd"
output: ['bb', 'bc', 'bd', 'cb', 'cd', 'db', 'dc']
```
Constraint:
input length > 1

Provide your answer in `answer_1.py`

## Object-oriented programming (10%) time: 10 minutes
open `answer_2.py`

extend class `Car` to have `Bike`'s `get_wheel` method but returns 4

Example:
``` python
bike = Bike()
bike.get_wheel()
>>> 2

car = Car()
car.get_wheel()
>>> 4
```

you may not add any method under `Car` class

## MongoDB understanding (10%): 10 minutes

do `pip install pymongo`

open `answer_3.py`


The data is looked like this:
```json
{
    "name" : "John",
    "age" : 33,
    "child" : [ 
        "bbb", 
        "ccc", 
        "ddd"
    ]
},
{
    "name" : "Rick",
    "age" : 31,
    "child" : [ 
        "bbb"
    ]
},
{
    "name" : "Jane",
    "age" : 43,
    "child" : [ 
        "bbb", 
        "ccc", 
        "ddd"
    ]
}
```
Query the data with the constraint:
```
number of child is greater than 3
```

## Web scraping basic project (20%) 30 minutes
scrape https://www.kaskus.co.id/channel/5/news

use anything with Python to get 5 pages of news data
