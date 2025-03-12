from cocommit.git_utils import get_last_commit_message

def main():
    print("Hello world")
    print(get_last_commit_message('.'))

if __name__ == "__main__":
    main()