import mongomock
import json


# modify starts here
query = {'name': 'John'}
# modify ends here


if __name__ == '__main__':
    client = mongomock.MongoClient()
    col = client['test']['collection']
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        col.insert_many(data)
    result = list(col.find(query))
    print(result)
    assert len(result) == 2
    assert result[0]['name'] == "John"
    print("PASSED 1")
    assert result[1]['name'] == "Jane"
    print("PASSED 2")