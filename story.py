from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import time
import os

print("A long time ago in a galaxy far, far away...")
time.sleep(3)
os.system("clear")
print("\n"*50)
text = ["A man from India, Humen Rajtnau was tired of mentorbots,",
        "so he got started to implement some new extra features,",
        "but he did not realise a bug,",
        "which not only could destroy the entire CodeCool,",
        "but the whole programmer community..."
        ]


def print_text_slowly(lines, sleep):
    max_len = str(max(lines, key=len))

    for line in lines:
        print(line)
        time.sleep(sleep)

print_text_slowly(text, 1.33)

error_message = 'Traceback (most recent call last):\n  File "<stdin>", line 36, in <module>\n' \
                "IndentationError: expected an indented block"


print("                       ______   ______    _______   _______                       ")
print("                      /      | /  __  \  |       \ |   ____|                      ")
print("                     |  ,----'|  |  |  | |  .--.  ||  |__                         ")
print("                     |  |     |  |  |  | |  |  |  ||   __|                        ")
print("                     |  `----.|  `--'  | |  '--'  ||  |____                       ")
print("                      \______| \______/  |_______/ |_______|                      ")
print("     _______.  ______    __       _______   __   _______ .______          _______.")
print("    /       | /  __  \  |  |     |       \ |  | |   ____||   _  \        /       |")
print(error_message)
sys.exit(0)
print("   |   (----`|  |  |  | |  |     |  .--.  ||  | |  |__   |  |_)  |      |   (----`")
print("    \   \    |  |  |  | |  |     |  |  |  ||  | |   __|  |      /        \   \    ")
print(".----)   |   |  `--'  | |  `----.|  '--'  ||  | |  |____ |  |\  \----.----)   |   ")
print("|_______/     \______/  |_______||_______/ |__| |_______|| _| `._____|_______/    ")
print("\n\n                          A Mentor's Life (in (n)OO way)")

codecool_msc = CodecoolClass.generate_local()
