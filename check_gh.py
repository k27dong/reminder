import sys
from github import Github
from datetime import datetime, timedelta

pat = sys.argv[1]
latest_commit_time: datetime = None

for repo in Github(pat).get_user().get_repos():
    try:
        # For now there's an issue with the API (not sure if it's by GitHub or PyGitHub), where the
        # timezone it returned is correct, but the time itself is actually set in UTC.
        # On the current implementation this won't affect anything, however it's something to keep in mind.
        curr_last_commit_time = repo.get_commits()[0].commit.committer.date
        if latest_commit_time is None or curr_last_commit_time > latest_commit_time:
            latest_commit_time = curr_last_commit_time
    except:
        # edge case where one of the repo is deleted by GitHub for some reason (e.g. DMCA)
        # it won't be accessible but still shows up in the API
        continue

# This script would run everyday at 8pm, to avoid timezone issues we'll just check if the last commit
# is made within 17 hours of the current time. (3AM)
today = datetime.now()

if latest_commit_time is None or today - latest_commit_time > timedelta(hours=17):
    print("Hours since last commit: ", today - latest_commit_time)
    sys.exit(1)

print(f"Last commit today: {latest_commit_time}, {today - latest_commit_time} ago.")
