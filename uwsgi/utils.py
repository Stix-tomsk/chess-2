import hashlib


def hash(value):
    return hashlib.sha256(value.encode()).hexdigest()