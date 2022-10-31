# eu4 tinman repo
Cause time is money and I like achievements and have no time to play this game on anything but 5.

This script will back up your current <save_name>\_backup.eu4 file to a different folder.  It will also take a screenshot of the game state.

# usage
* You may need to change lines 13-20 to match your system.  I backup my games to an older 2TB platter drive, not my ssd.

Create a python venv (good practice)
>python -m pip install venv .venv

>.venv/scripts/activate

>(.venv)\> python cp.py \<save_name>

This will run in a loop indefinitely.  Every 3 mins will attempt to save the \<save_name>\_backup.eu4 if the file has changed since the last save.

You can restore ironman game states by copying the saved backfile to the eu4\/save games/ folder