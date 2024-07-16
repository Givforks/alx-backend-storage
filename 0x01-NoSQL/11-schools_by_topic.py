#!/usr/bin/env python3
'''Task eleven.
'''

def schools_by_topic(mongo_collection, topic):
    '''Return lists of schools having the specific topics
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
