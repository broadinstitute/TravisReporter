from github import Github
import os

key = os.environ["GITHUB_TOKEN"]
g = Github(key)

ME=os.environ["GITHUB_USERNAME"]
MAGIC="Status:"



pull_number = os.environ["TRAVIS_PULL_REQUEST"]
repo_name = os.environ["TRAVIS_REPO_SLUG"]
repo = g.get_repo(repo_name)
pull = repo.get_pull(int(pull_number))
comments = pull.get_issue_comments()
for comment in comments:
    print(comment)
    print(comment.user)
    print(comment.user.login)
    if comment.user.login == ME:
        print(comment.body)




