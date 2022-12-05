import itertools


def make_chunks(lst, n):
    # TODO replace this with more_itertools
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
