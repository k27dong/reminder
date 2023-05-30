"""
GitHub Action uses Unix Cron syntax for scheduling, which couldn't handle
DST transitions. This script serves as a workaround for this issue.

This script would be run both at -0500 and -0400 from UTC,
"""

import sys
from datetime import datetime
from zoneinfo import ZoneInfo

if datetime.now(ZoneInfo("America/Toronto")).hour != 13:
    print("false")
else:
    print("true")
