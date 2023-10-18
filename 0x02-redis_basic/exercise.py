#!/usr/bin/env python3
"""
Redis module that stores string
"""
import sys
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4

import redis

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    a system to count how many times methods 
    of cache class are called.
    Parameter method:
    return:
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrap
        Parameter self:
        Parameter args:
        parameter kwargs:
        return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    add its input parameters to one list
    In redis, and store its output into another list.
    parameter method:
    return:
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapp"""
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res
    
    return wrapper

class Cache:
    """Cache redis class"""

    def __init__(self):
        """constructor of the redis class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        generate a random key (e.g usin uuid),
        store the input data in Redis using the
        random key and return the key.
        parameter: data
        return:
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
                """Convert the data back to the desired format
                parameters: key, fn:
                return:
                """
                if fn:
                    return fn(self._redis.get(key))
                data = self._redis.get(key)
                return data

    def get_int(self: bytes) -> int:
        """Get a number"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """Get a string"""
        return self.decode("utf-8")
