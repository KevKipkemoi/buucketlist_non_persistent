from bucketlist import BucketList
import uuid

class Bucket(object):

    data = []

    # Create
    @staticmethod
    def create_bucketlist(description, goal, id=str(uuid.uuid1())):
        new_bucket = BucketList(id, description, goal)
        Bucket.data.append(new_bucket) 

    # Read
    @staticmethod
    def display_bucketlist():
        return Bucket.data

    # Update
    @staticmethod
    def update_bucketlist(goal):
        updated_bucket = BucketList(id, description, goal)
        Bucket.data.insert(0, updated_bucket)

    # Delete
    @staticmethod
    def rem_bucketlist(id):
        Bucket.data.pop(id)
