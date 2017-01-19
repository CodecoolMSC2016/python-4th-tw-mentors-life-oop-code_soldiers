from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import time

print("\n"*20)
text = ["A long time ago in a galaxy far, far away...",
        ""
        ]

error_message = 'Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n' \
                "FileNotFoundError: [Errno 2] No such file or directory: 'codecool_class.py'"


def print_text_slowly(lines, sleep):
    for line in text:
        print line
        time.sleep(sleep)

print_text_slowly(text, 40)





print("                       ______   ______    _______   _______                       ")
print("                      /      | /  __  \  |       \ |   ____|                      ")
print("                     |  ,----'|  |  |  | |  .--.  ||  |__                         ")
print("                     |  |     |  |  |  | |  |  |  ||   __|                        ")
print("                     |  `----.|  `--'  | |  '--'  ||  |____                       ")
print("                      \______| \______/  |_______/ |_______|                      ")
print("     _______.  ______    __       _______   __   _______ .______          _______.")
print("    /       | /  __  \  |  |     |       \ |  | |   ____||   _  \        /       |")
print("   |   (----`|  |  |  | |  |     |  .--.  ||  | |  |__   |  |_)  |      |   (----`")
print(error_message)
sys.exit(0)
print("    \   \    |  |  |  | |  |     |  |  |  ||  | |   __|  |      /        \   \    ")
print(".----)   |   |  `--'  | |  `----.|  '--'  ||  | |  |____ |  |\  \----.----)   |   ")
print("|_______/     \______/  |_______||_______/ |__| |_______|| _| `._____|_______/    ")
print("\n\n                          A Mentor's Life (in (n)OO way)")

codecool_msc = CodecoolClass.generate_local()
