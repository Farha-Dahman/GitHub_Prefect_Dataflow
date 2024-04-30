from mongoengine import Document, StringField, EmbeddedDocument, ListField, DateTimeField, BooleanField, EmbeddedDocumentField, URLField, IntField, DictField

class User(EmbeddedDocument):
    name = StringField()
    email = StringField()
    date = DateTimeField()

class Tree(EmbeddedDocument): 
    sha = StringField()
    url = URLField()

class Verification(EmbeddedDocument):
    verified = BooleanField()
    reason = StringField()
    signature = StringField()
    payload = StringField()

class Parent(EmbeddedDocument):
    sha = StringField()
    url = URLField()
    html_url = URLField()

class Commit(EmbeddedDocument):
    author = EmbeddedDocumentField(User)
    committer = EmbeddedDocumentField(User)
    message = StringField()
    tree = EmbeddedDocumentField(Tree) 
    url = URLField()
    comment_count = IntField()
    verification = EmbeddedDocumentField(Verification)

class CommitDocument(Document):
    sha = StringField()
    node_id = StringField()
    commit = EmbeddedDocumentField(Commit)
    url = URLField()
    html_url = URLField()
    comments_url = URLField()
    author = DictField()
    committer = DictField()
    parents = ListField(EmbeddedDocumentField(Parent))

    meta = {'collection': 'commit'}
