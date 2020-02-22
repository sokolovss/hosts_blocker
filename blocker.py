import time
from datetime import datetime as dt
import os

#hosts_tmp = 'hosts'
hosts_path = r'/etc/hosts'
redirect = '127.0.0.1'
websites_list = ["www.facebook.com", "facebook.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        print("Work hours")
        time.sleep(5)
        if os.path.exists(hosts_path):
            file = open(hosts_path, 'r+')
            content = file.read()
            for i in websites_list:
                if i in content:
                    pass
                else:
                    file.write('\n127.0.0.1        ' + i)

        else:
            pass
    else:
        print("Fun hours")
        time.sleep(1)
        if os.path.exists(hosts_path):
            file = open(hosts_path, 'r+')
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    print(line)
                    file.write(line)
            file.truncate()

