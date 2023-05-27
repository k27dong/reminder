import simplepush, sys
from datetime import datetime

today = datetime.now().strftime("%B %d")

simplepush.send(
    key=sys.argv[1], title=f"Github Reminder {today}", message="c'mon do something"
)
