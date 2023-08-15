#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    insert_result = mongo_collection.insert_one(kwargs)
    document_id = insert_result.inserted_id
    return document_id
