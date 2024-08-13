#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all tha topics of tha collection's document based on tha name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
