from git import InvalidGitRepositoryError, NoSuchPathError, Repo

def is_git_repo(repo_path):
    try:
        Repo(repo_path)
        return True
    except (InvalidGitRepositoryError, NoSuchPathError):
        return False

def get_last_commit_message(repo_path):
    repo = Repo(repo_path)
    return repo.head.commit.message.strip()