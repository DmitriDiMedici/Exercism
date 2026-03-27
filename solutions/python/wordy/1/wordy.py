def answer(question):
    operators = {
        "plus": "+",
        "minus": "-",
        "multiplied": "*",
        "divided": "/"
    }

    if not question.startswith("What is"):
        raise ValueError("syntax error")

    clean_q = question.removesuffix("?")

    clean_q = clean_q.removeprefix("What is")

    operation_str = clean_q.strip()

    if not operation_str:
        raise ValueError("syntax error")

    operation_str = operation_str.replace("multiplied by", "multiplied")
    operation_str = operation_str.replace("divided by", "divided")


    parts = operation_str.split()
    tokens = []

    for part in parts:
        if part in operators:
            tokens.append(operators[part])
        elif part.lstrip('-').isdigit():
            tokens.append(int(part))
        else:

            raise ValueError("unknown operation")

    if not tokens:
        raise ValueError("syntax error")

    if not isinstance(tokens[0], int):
        raise ValueError("syntax error")

    if len(tokens) == 1:
        return tokens[0]

    if not isinstance(tokens[-1], int):
        raise ValueError("syntax error")

    for i in range(len(tokens) - 1):
        if type(tokens[i]) == type(tokens[i + 1]):
            raise ValueError("syntax error")

    result = tokens[0]

    for i in range(1, len(tokens), 2):
        op = tokens[i]
        next_num = tokens[i + 1]

        if op == "+":
            result += next_num
        elif op == "-":
            result -= next_num
        elif op == "*":
            result *= next_num
        elif op == "/":

            if next_num == 0:
                raise ValueError("division by zero")
            result //= next_num

    return result