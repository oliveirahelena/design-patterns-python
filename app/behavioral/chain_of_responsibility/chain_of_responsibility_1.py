# Implementando com funções


def handler_abc(letter: str) -> str:
    letters = ["A", "B", "C"]

    if letter in letters:
        return f"handler_abc: conseguiu tratar o valor {letter}"
    return handler_def(letter)


def handler_def(letter: str) -> str:
    letters = ["D", "E", "F"]

    if letter in letters:
        return f"handler_def: conseguiu tratar o valor {letter}"
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f"handler_unsolved: não sei tratar {letter}"


if __name__ == "__main__":
    print(handler_abc("A"))
    print(handler_abc("B"))
    print(handler_abc("C"))
    print(handler_abc("D"))
    print(handler_abc("E"))
    print(handler_abc("F"))
    print(handler_abc("G"))
    print(handler_abc("H"))
    print(handler_abc("I"))
