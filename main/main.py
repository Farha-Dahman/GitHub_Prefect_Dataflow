import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
github_token   = os.getenv('github_token')
github_base_url = os.getenv('github_base_url')
username = os.getenv('username')
headers = {'Authorization': f'token {github_token }'}

def get_repositories_name(username, github_base_url="https://api.github.com/users", token=""):
    headers = {'Authorization': f'token {token}'} if token else {}
    repos_url = f"{github_base_url}/{username}/repos"
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status()
        return [repo['name'] for repo in response.json()]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving repository names: {e}")
        return []

def get_repository_general_data(repository):
    url = f"{github_base_url}/{username}/{repository}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving repository data: {e}")
        return None

def get_branches_name(repository):
    branches_url = f"{github_base_url}/{username}/{repository}/branches"
    try:
        response = requests.get(branches_url, headers=headers)
        response.raise_for_status()
        return [branch['name'] for branch in response.json()]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving branch names: {e}")
        return []

def get_commits(repository,branch_name):
    """Retrieve commits from a specific branch of the repository."""
    url = f"{github_base_url}/{username}/{repository}/commits?sha={branch_name}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving commits: {e}")
        return []

if __name__ == "__main__":
    repository_data = []
    data ={}
    repositories = get_repositories_name(username,token=github_token)    
    for repository in repositories:
        repo_details = get_repository_general_data(repository)
        branches = get_branches_name(repository)
        repo_data = {
            'details': repo_details,
            'branches': {}
        }
        for branch in branches:
            commits = get_commits(repository, branch)
            repo_data['branches'][branch] = commits
        data[repository] = repo_data

    json_string = json.dumps(data, indent=4)
    with open('my_dict.txt', 'w') as file:
        file.write(json_string)