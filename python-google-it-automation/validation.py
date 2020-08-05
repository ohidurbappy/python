def validate_username(username,minlen):
    assert type(username)==str,"Username must be string"

    if minlen<1:
        raise ValueError("Min len must be 1")

    if not username.isalnum():
        return False

    if len(username)<minlen:
        return False

    return True

    