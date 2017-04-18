import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=ME5M3dUKDz8&list=PLVMYdrGzjj9eBJ_DE28a713FOgwSiI5Be")
    break_count = break_count + 1
