def parse(jsonstr):
    return Parser().parse(jsonstr)

class _StringPiece(object):
    def __init__(self, string):
        self._string = string
        self._index = -1

    def peek(self):
        try:
            return self._string[self._index + 1]
        except IndexError:
            pass

    def next(self):
        try:
            self._index += 1

            return self._string[self._index]
        except IndexError:
            self._index -= 1

            return self._string[self._index]

    def prev(self):
        if self._index == 0:
            return self._string[0]

        return self._string[self._index - 1]

    def __str__(self):
        return self._string


class Parser(object):

    def parse(self, jsonstr):
        self._str = _StringPiece(jsonstr)
        self._parsing_boolean = False
        
        return self._parse_json()

    def _parse_json(self):
        self._parsing_boolean = False

        char = self._str.peek()
        if char == "[":
            return self._parse_list()
        elif char.isdigit() or char == "-":
            return self._parse_number()
        elif char == '"':
            return self._parse_string()
        elif char in ("f", "t", "n"):
            return self._parse_booleans()

    def _parse_list(self):
        response = []
        while self._str.next() != "]":
            if self._str.peek() != "]":
                token = self._parse_json()

                if token is not None or self._parsing_boolean:
                    response.append(token)

        return response

    def _parse_number(self):
        current = self._str.next()
        is_float = False
        is_exponencial = False
        modifiers = ("-", ".", "e", "E")
        number = ""

        while current.isdigit() or current in modifiers:
            is_float = is_float or current == "."
            is_exponencial = is_exponencial or current in ("e", "E")

            number += current

            current = self._str.next()

        return float(number) if is_float or is_exponencial else int(number)

    def _parse_booleans(self):
        self._parsing_boolean = True
        
        token = self._str.next()

        has_to_return = {"f": "false", "t": "true", "n": "null"}[token]
        
        while token != has_to_return:
            token += self._str.next()

        if token == "false":
            return False
        elif token == "true":
            return True
        elif token == "null":
            return None
        else:
            raise Exception("Invalid token, %s expected got %s" % (token,
                has_to_return))

    def _parse_string(self):
        string = ""

        _ = self._str.next() # Ignoring first quotes
        while True:
            string += self._str.next()

            if self._str.peek() == '"':
                string += self._str.next()

                if self._str.peek() in (",", "]", "}"):
                    string = string[:-1]

                    _ = self._str.prev()
                    break
                
        return string
