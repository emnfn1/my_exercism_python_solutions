def is_paired(input_string):
    stack = []
    opens = set("([{")
    closes = set(")]}")
    matches = {"(": ")", "[": "]", "{": "}"}
    for ch in input_string:
        if ch in opens:
            stack.append(ch)
        elif ch in closes:
            if not stack:
                return False
            last_open = stack.pop()
            if matches[last_open] != ch:
                return False
    return not stack