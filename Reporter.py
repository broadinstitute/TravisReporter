from github import Github
import os
import sys

key = os.environ["GITHUB_TOKEN"]
g = Github(key)

ME=os.environ["GITHUB_USERNAME"]
MAGIC="Travis Status:"



pull_number = os.environ["TRAVIS_PULL_REQUEST"]
repo_name = os.environ["TRAVIS_REPO_SLUG"]
job_number = os.environ["TRAVIS_JOB_NUMBER"]
job_id = os.environ["TRAVIS_JOB_ID"]
build_number = os.environ["TRAVIS_BUILD_NUMBER"]
build_id = os.environ["TRAVIS_BUILD_ID"]
repo = g.get_repo(repo_name)
pull = repo.get_pull(int(pull_number))
comments = pull.get_issue_comments()

"""
Status: 101
Job: 3.1 url 
Job: 3.2: url
"""


def matches_build_number(comment, build_number):
    body = comment.body
    lines = body.splitlines()
    comment_build_number = lines[0].split(":")[1].strip()
    return comment_build_number == build_number


def isMyComment(comment):
    return comment.user.login == ME

travis_page_url = "https://travis-ci.com/"+ repo_name + "/builds/" + build_id
job_page_url = "https://travis-ci.com/" + repo_name + "/jobs/" + job_id
report_path = os.environ["REPORT_PATH"]
logs_storage = os.environ["HELLBENDER_TEST_LOGS"]
log_url = "https://storage.googleapis.com" + logs_storage + report_path + "tests/test/index.html"

message = "[%s](%s) - [Logs](%s)" % (job_number, job_page_url, sys.argv[1])


def update(comment):
    comment.edit(comment.body +"\n" + message)

def newComment(pull):
    pull.create_issue_comment(MAGIC + " " + build_number +
                              "\nFailures in job [%s](%s)" % (build_number, travis_page_url)
                              +"\n" + message)


#Update the comment or create a new one
for comment in comments:
    if isMyComment(comment) and matches_build_number(comment, build_number):
        print("found matching comment")
        update(comment)
        break
else:
    newComment(pull)





