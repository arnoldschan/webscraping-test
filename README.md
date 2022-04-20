# Web scraper technical test

Test overview:
- 30% Data structure & Algorithm understanding 
- 15% Object-oriented programming
- 15% MongoDB understanding
- 40% Web scraping basic project


## Data structure & Algorithm understanding (30%) time: 20 minutes

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

## Object-oriented programming (15%) time: 10 minutes
open `answer_2.py`

extend class `Car` to have `Vehicle`'s `get_wheel` method but returns 4
also `Car` now has additional input `engine` and additonal method `get_engine`

Example:
``` python
vehicle = Vehicle('jenny')
vehicle.get_wheel()
>>> 2
vehicle.get_owner()
>>> 'jenny'

car = Car('lucas', 'diesel')
car.get_wheel()
>>> 4
car.get_owner()
>>> 'lucas'
car.get_engine()
>>> 'diesel'
```

you may not override `get_wheel` in `Car` class

## MongoDB understanding (15%): 10 minutes

do `pip install mongomock`

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
number of child is greater than 2
```

## Web scraping basic project (40%) 30 minutes
scrape https://www.kaskus.co.id/channel/5/news

use anything with Python to get 5 pages of news data

Scraping without Selenium is a plus!
