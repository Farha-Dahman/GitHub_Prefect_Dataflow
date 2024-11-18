from mongoengine import Document, StringField, URLField, BooleanField, IntField, DateTimeField, ListField, DictField

class Repository(Document):
    id = IntField(primary_key=True)
    node_id = StringField()
    name = StringField()
    full_name = StringField()
    private = BooleanField()
    owner = DictField()
    html_url = URLField()
    description = StringField()
    fork = BooleanField()
    url = URLField()
    forks_url = URLField()
    keys_url = URLField()
    collaborators_url = URLField()
    teams_url = URLField()
    hooks_url = URLField()
    issue_events_url = URLField()
    events_url = URLField()
    assignees_url = URLField()
    branches_url = URLField()
    tags_url = URLField()
    blobs_url = URLField()
    git_tags_url = URLField()
    git_refs_url = URLField()
    trees_url = URLField()
    statuses_url = URLField()
    languages_url = URLField()
    stargazers_url = URLField()
    contributors_url = URLField()
    subscribers_url = URLField()
    subscription_url = URLField()
    commits_url = URLField()
    git_commits_url = URLField()
    comments_url = URLField()
    issue_comment_url = URLField()
    contents_url = URLField()
    compare_url = URLField()
    merges_url = URLField()
    archive_url = URLField()
    downloads_url = URLField()
    issues_url = URLField()
    pulls_url = URLField()
    milestones_url = URLField()
    notifications_url = URLField()
    labels_url = URLField()
    releases_url = URLField()
    deployments_url = URLField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    pushed_at = DateTimeField()
    git_url = StringField()
    ssh_url = StringField()
    clone_url = URLField()
    svn_url = URLField()
    homepage = StringField()
    size = IntField()
    stargazers_count = IntField()
    watchers_count = IntField()
    language = StringField()
    has_issues = BooleanField()
    has_projects = BooleanField()
    has_downloads = BooleanField()
    has_wiki = BooleanField()
    has_pages = BooleanField()
    has_discussions = BooleanField()
    forks_count = IntField()
    mirror_url = URLField()
    archived = BooleanField()
    disabled = BooleanField()
    open_issues_count = IntField()
    license = StringField()
    allow_forking = BooleanField()
    is_template = BooleanField()
    web_commit_signoff_required = BooleanField()
    topics = ListField(StringField())
    visibility = StringField()
    forks = IntField()
    open_issues = IntField()
    watchers = IntField()
    default_branch = StringField()
    permissions = DictField()
