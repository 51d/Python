# this python program reminds a user to take break while working
import time
import webbrowser
print "prog started at" + time.ctime
break_count = 5
for i in break_count:
  time.sleep(60)
  webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
