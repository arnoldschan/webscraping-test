import pymongo

# modify starts here
query = {'name': 'John'}
# modify ends here


if __name__ == '__main__':
    client = pymongo.MongoClient('localhost')
    col = client['test']['collection']
    result = list(col.find(query))
    assert len(result) == 2
    assert result[0]['name'] == "John"
    print("PASSED 1")
    assert result[1]['name'] == "Jane"
    print("PASSED 2")