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

def get_amend_last_commit_message(repo_path, new_commit_message):
    repo = Repo(repo_path)
    current_message = repo.head.commit.message.strip()
    repo.git.commit("--amend", "-m", new_commit_message)
    return current_message
