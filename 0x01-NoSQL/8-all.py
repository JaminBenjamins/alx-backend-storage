#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection using Python
    Args:
        mongo_collection - object containing documents
    return:
        List of objects nothing if empty
    """
    documents = mongo_collection.find()
    return documents
