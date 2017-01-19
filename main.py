from os import system
from time import sleep

system("python3 story.py")
sleep(2)
print("Ooooppppps 😣....\nThere was an error during running 'story.py' 😣 .")
sleep(5)
for count in range(3):
    for index in range(4):
        text = "Starting auto debugger module" + "." * index
        print(text, end='\r\r')
        sleep(0.5)
system("clear")
system("python3 debugger.py")
for count in range(3):
    system("clear")
    for index in range(4):
        text = "Starting 'story.py'" + "." * index
        print(text, end='\r\r')
        sleep(0.5)
system("clear")
system("python3 story.py")
with open("backup_story.py") as backup, open("story.py", 'w') as story:
    story.write(backup.read())
