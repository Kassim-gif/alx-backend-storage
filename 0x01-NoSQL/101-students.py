#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    '''Prints all tha students in tha collection sorted by tha average score.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    rtest commit
     return students
