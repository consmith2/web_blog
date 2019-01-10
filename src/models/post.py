import uuid
from src.common.database import Database
import datetime

__author__ = 'cjs'


class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data) # for each of the elements in post_data get the name of the element from the db
                #   blog_id=post_data['blog_id'],
                #   title=post_data['title'],
                #   content=post_data['content'],
                #   author=post_data['author'],
                #   created_date=post_data['created_date'],
                #   id=post_data['_id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]


