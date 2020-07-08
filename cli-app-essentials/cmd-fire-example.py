import fire


def add(a: int, b: int):
    """
    Returns sum of a and b
    :param a: first argument 
    :param b: second argument (default: 2)
    :return: sum of a and b
    """
    return a+b


if __name__ == "__main__":
    fire.Fire({
        "sum": add
    })