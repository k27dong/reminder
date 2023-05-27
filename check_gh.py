import sys
from github import Github
from datetime import datetime, timezone

pat = sys.argv[1]
latest_commit_time: datetime = None

for repo in Github(pat).get_user().get_repos():
    try:
        curr_last_commit_time = repo.get_commits()[0].commit.committer.date
        if latest_commit_time is None or curr_last_commit_time > latest_commit_time:
            latest_commit_time = curr_last_commit_time
    except:
        # edge case where one of the repo is deleted by GitHub for some reason (e.g. DMCA)
        # it won't be accessible but still shows up in the API
        continue

# For now there's an issue with the API (not sure if it's by GitHub or PyGitHub), where the
# timezone it returned is correct, but the time is actually in UTC. So we need to correct it manually.
# Hopefully this will be fixed soon.

# get the correct timezone returned from the API
target_timezone = latest_commit_time.astimezone().tzinfo

# convert the time to UTC, then convert it to the correct timezone, then remove the offset stamp
latest_commit_time = (
    latest_commit_time.replace(tzinfo=timezone.utc)
    .astimezone(tz=target_timezone)
    .replace(tzinfo=None)
)

# Check if there's a push today after 3am
today = datetime.now()
today = today.replace(hour=3, minute=0, second=0, microsecond=0)

# if latest_commit_time is None or latest_commit_time < today:
if True:
    print("No commits found.")
    sys.exit(1)

print(f"Last commit today: {latest_commit_time}")
