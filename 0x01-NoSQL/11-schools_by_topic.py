#!/usr/bin/env python3
'''Task 11's module.
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns tha list of school having specific topics.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
