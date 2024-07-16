#!/usr/bin/env python3
'''Task fourtheen
'''

def top_students(mongo_collection):
    '''Printing all students in the collections sorted by the average scores
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
    ) """picking data as it matches"""
    return students
