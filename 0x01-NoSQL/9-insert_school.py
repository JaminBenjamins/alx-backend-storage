#!/usr/bn/env python3
"""
Insert a new document in a collection based on key/value pair
Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection - pymongo collection object
    Return _id of created object
"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that ads an object in a collection
    Return new _id
    """
    new_document = mongo_collection(insert_one(kwargs))
    return new_document.inserted_id
