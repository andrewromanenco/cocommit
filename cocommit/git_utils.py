from git import Repo

def get_last_commit_message(repo_path):
    repo = Repo(repo_path)
    return repo.head.commit.message.strip()