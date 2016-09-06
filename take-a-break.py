import time
import webbrowser

time_in_seconds = float(raw_input("How between breaks? (in seconds)"))
url = raw_input("Which URL should I open?")

x = 0
while x < 3:
    time.sleep(time_in_seconds);
    webbrowser.open(url)
    x += 1
