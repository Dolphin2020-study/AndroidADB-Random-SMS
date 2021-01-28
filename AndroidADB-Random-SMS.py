import os
import sys
import time  
import random
list = [
       "短信1" ,
       "短信2" ,
       "短信3" 
        ]
def main():
    for cishu in range(100):
        random.shuffle(list)
        os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:15724627660 --es sms_body  "+random.choice(list))
        time.sleep(1)
        for i in range(random.randint(5, 9), 0, -1):
            print("\r等待{}秒后发短信\n".format(i), end='')
            time.sleep(1)
        os.popen("adb shell input keyevent 22")
        time.sleep(1)
        os.popen("adb shell input keyevent 66")
        time.sleep(1)
if __name__ == '__main__':
    main()
