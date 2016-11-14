from datetime import datetime

from hashids import Hashids


def generate_hashid():
    """ Generates a random 8+ character hash based
        on the current time in milleseconds
        NOTE: Only works when the RPS is << 1000,
              could be increased to microseconds,
              but at that point a different hashing
              library should probably be used
    """
    return Hashids(min_length=8).encode(int(datetime.now().timestamp()*1000))
