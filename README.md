pyjson
======

A simple JSON parser/stringifier in Python made for study purposes. Tries to validate acording to [JSONLint](http://jsonlint.com/) rules.

## Usage

From Python to json

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

json = pyjson.stringify(my_data)

print json # {"this_is": null, "my_array": [[0, 0], [1, 2]], "is_something": true, "dict": {"another_list": ["my_string"], "name": "pedrochaves"}}
```
