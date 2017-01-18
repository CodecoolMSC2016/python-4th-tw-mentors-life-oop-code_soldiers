from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys

print("                       ______   ______    _______   _______                       ")
print("                      /      | /  __  \  |       \ |   ____|                      ")
print("                     |  ,----'|  |  |  | |  .--.  ||  |__                         ")
print("                     |  |     |  |  |  | |  |  |  ||   __|                        ")
print("                     |  `----.|  `--'  | |  '--'  ||  |____                       ")
print("                      \______| \______/  |_______/ |_______|                      ")
print("     _______.  ______    __       _______   __   _______ .______          _______.")
print("    /       | /  __  \  |  |     |       \ |  | |   ____||   _  \        /       |")
print("   |   (----`|  |  |  | |  |     |  .--.  ||  | |  |__   |  |_)  |      |   (----`")
print("    \   \    |  |  |  | |  |     |  |  |  ||  | |   __|  |      /        \   \    ")
print(".----)   |   |  `--'  | |  `----.|  '--'  ||  | |  |____ |  |\  \----.----)   |   ")
print("|_______/     \______/  |_______||_______/ |__| |_______|| _| `._____|_______/    ")
print("\n\n                          A Mentor's Life (in (n)OO way)")

error_message = 'Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n' \
                "FileNotFoundError: [Errno 2] No such file or directory: 'codecool_class.py'"

print(error_message)
sys.exit(0)
codecool_bp = CodecoolClass.create_local
