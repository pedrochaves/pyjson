pyjson
======

Edit
A simple JSON parser/stringifier in Python made for study purposes. Tries to validate according to [JSONLint](http://jsonlint.com/) rules.

## Usage and examples

Stringifying stuff to JSON

```python
import pyjson

my_data = {
    "my_array": [[0, 0], [1, 2]],
    "is_something": True,
    "this_is": None,
    "dict": {
        "name": "pedrochaves",
        "another_list": ["my_string"]
    }
}

# Returns a string representation of the data in JSON
json_string = pyjson.stringify(my_data)

# ...or you can save it to a file
pyjson.to_file("my_data.json", my_data)
```
