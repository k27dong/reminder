# Reminder

An auto reminder that checks if you have commited anything on Github today and sends you a notification on your phone if you haven't.

## Tech Stacks
```
Python
GitHub Actions
```

## How it works
1. Download [SimplePush](https://simplepush.io/)
2. Create a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
3. Add your SimplePush Private Key and your PAT to your Github Secrets
4. The action is scheduled to run everyday at 8:00 PM via [cron](https://en.wikipedia.org/wiki/Cron).
5. The action will uses the two Python scripts in the repo: `check_gh.py` checks if there's any commits made today after 3 AM, if not then `push.py` will run and send a notification to your phone.