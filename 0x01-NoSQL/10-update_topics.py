#!/usr/bin/env python3
"""
A script that changes all topics of a document
based on a name. 
Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection - pymongo object
    name(string) - school name to update
    topics(list of strings) - list of topics in school
"""


def update_topics(mongo_collection, name, topics):
    """
    Prototype: def update_topics(mongo_collection, name, topics):
    change all topics of a school document
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
