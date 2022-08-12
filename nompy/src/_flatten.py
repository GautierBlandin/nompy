def flatten(data):
    """
    Flattens the given data.
    """
    if type(data) == list:
        child = []
        for d in data:
            child += flatten(d)
        return child
    return [data]
