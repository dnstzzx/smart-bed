import app
import threading
import sys
import msg
import cap
import time


threading.Thread(target=app.run).start()
threading.Thread(target=cap.grasp_cap).start()
time.sleep(1)
threading.Thread(target=cap.deep_loop).start()

last_line = ''


while True:
    line = sys.stdin.readline().strip()
    if line == '\x1b[A':
        line = last_line
    last_line = line
    msg.add_msg("esp", line)
    
    

