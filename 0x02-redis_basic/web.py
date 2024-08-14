#!/usr/bin/env python3
'''Module with tha tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''Tha module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches tha output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''Tha wrapper function for caching tha  output.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns tha content of  URL after caching tha requests response,
    and tracking tha request.
    '''
    return requests.get(url).text
