from mongoengine import Document, StringField

class CommitComment(Document):
    commit_id = StringField(required=True)
    user = StringField(required=True)
    body = StringField(required=True)
