from mongoengine import Document, StringField, EmbeddedDocument, EmbeddedDocumentField, BooleanField, URLField, ListField

class Commit(EmbeddedDocument):
    sha = StringField(required=True)
    url = URLField(required=True)

class RequiredStatusChecks(EmbeddedDocument):
    enforcement_level = StringField(default="off")
    contexts = ListField(StringField())
    checks = ListField(StringField())

class Protection(EmbeddedDocument):
    enabled = BooleanField(default=False)
    required_status_checks = EmbeddedDocumentField(RequiredStatusChecks)

class Branch(Document):
    name = StringField(required=True)
    commit = EmbeddedDocumentField(Commit, required=True)
    protected = BooleanField(default=False)
    protection = EmbeddedDocumentField(Protection)
    protection_url = URLField()
