#!/usr/bin/env python3
"""
Return all students sorted by average score
Prototype: def top_students(mongo_collection):
    Return top student ordered by average score
"""


def top_students(mongo_collection):
    """
    Prototype: def top_students(mongo_collection):
        return all students ordered by average score
    """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
