#!/usr/bin/env python3
'''Task ten..
'''

def update_topics(mongo_collection, name, topics):

    '''Change for all topics of the collection's document based on the names
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
