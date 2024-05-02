import requests
import logger
from datetime import timedelta
from prefect import task, flow
from prefect.tasks import task_input_hash
from etl.save_to_json import save_json
from etl.store_in_DB import store_data_in_database
from database.models.collaborator import Collaborator
from database.models.commit import CommitDocument
from database.models.commit_comment import CommitComment
from database.models.branch import Branch
from database.models.repos import Repository

# Use logger
logger = logger.logger

@task
def fetch_data(url, params=None, headers=None):
    """
    Fetches data from the GitHub API.

    Args:
    - url: The URL of the GitHub API endpoint.
    - params: Optional parameters for the API request.
    - headers: Optional headers for the API request.

    Returns:
    - JSON response data.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching data from {url}: {e}")
        raise

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=30))
def get_repositories(base_url, owner, headers):
    try:
        repos_url = f'{base_url}/users/{owner}/repos'
        repos_data = fetch_data(repos_url, headers=headers)
        store_data_in_database(repos_data, Repository)
        return [repo['name'] for repo in repos_data]
    except Exception as e:
        logger.error(f"Error getting repositories: {e}")
        raise

@task
def get_branches(base_url, owner, repo, headers):
    try:
        branches_url = f'{base_url}/repos/{owner}/{repo}/branches'
        branches_data = fetch_data(branches_url, headers=headers)
        # save_json(branches_data, 'branches.json')
        store_data_in_database(branches_data, Branch)
    except Exception as e:
        logger.error(f"Error getting branches: {e}")
        raise

@task
def get_commits(base_url, owner, repo, headers):
    try:
        commits_url = f'{base_url}/repos/{owner}/{repo}/commits'
        commits_data = fetch_data(commits_url, headers=headers)
        # save_json(commits_data, 'commits.json')
        store_data_in_database(commits_data, CommitDocument)
    except Exception as e:
        logger.error(f"Error getting commits: {e}")
        raise

@task
def get_commit_comments(base_url, owner, repo, headers):
    try:
        commit_comments_url = f'{base_url}/repos/{owner}/{repo}/comments'
        commit_comments_data = fetch_data(commit_comments_url, headers=headers)
        # save_json(commit_comments_data, 'commit_comments.json')
        store_data_in_database(commit_comments_data, CommitComment)
    except Exception as e:
        logger.error(f"Error getting commit comments: {e}")
        raise

@task
def get_collaborators(base_url, owner, repo, headers):
    try:
        collaborators_url = f'{base_url}/repos/{owner}/{repo}/collaborators'
        collaborators_data = fetch_data(collaborators_url, headers=headers)
        # save_json(collaborators_data, 'collaborators.json')
        store_data_in_database(collaborators_data, Collaborator)
    except Exception as e:
        logger.error(f"Error getting commit collaborators: {e}")
        raise
    
# Define flow
@flow
def github_data_extraction(owner, headers, base_url):        
    repos = get_repositories(base_url, owner, headers)
    for repo in repos:
        get_branches(base_url, owner, repo, headers)
        get_commit_comments(base_url, owner, repo, headers)
        get_collaborators(base_url, owner, repo, headers)
        get_commits(base_url, owner, repo, headers)