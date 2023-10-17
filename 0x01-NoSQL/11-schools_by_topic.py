#!/usr/bin/env python3
"""
Return list of schools having a specific topic
Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be a pymongo collection object
    topic (string) will be topic to be searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Prototype: def schools_by_topic(mongo_collection, topic):
        Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
