from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import time
import os


os.system("clear")
print("A long time ago in a galaxy far, far away...")
time.sleep(3)
os.system("clear")
print("\n" * 30)
text = ["A man from India, Humen Rajtnau was tired of mentorbots,",
        "so he got started to implement  some new extra features,",
        "but he became  so lazy  he gave his job  to codecoolers.",
        "",
        "Unfortunately   they  did  not  realise  a  deadly  bug,",
        "which  not  only  could  destroy  the  entire  CodeCool,",
        "but the whole programmer community..."]

text += ["" for x in range(30)]

def print_text_slowly(lines, sleep):
    max_len = str(max(lines, key=len))

    for line in lines:
        print(line)
        time.sleep(sleep)


print_text_slowly(text, 0.6)
os.system("clear")

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
# print(error_message)
# sys.exit(0)
print("   |   (----`|  |  |  | |  |     |  .--.  ||  | |  |__   |  |_)  |      |   (----`")
print("    \   \    |  |  |  | |  |     |  |  |  ||  | |   __|  |      /        \   \    ")
print(".----)   |   |  `--'  | |  `----.|  '--'  ||  | |  |____ |  |\  \----.----)   |   ")
print("|_______/     \______/  |_______||_______/ |__| |_______|| _| `._____|_______/    ")
print("\n\n                          A Mentor's Life (in (n)OO way)")
time.sleep(5)

codecool_msc = CodecoolClass.generate_local()
print("<< CODECOOL_MSC GENERATED >>")
print("One day when Humen Rajtnau went to Codecool Miskolc")

""" mindenki exmentor lesz, együtt elkezdenek inni,
annyira részegek lesznek, hogy elpusztítják a codecoolt és mindenkit aki tud programozni,
így pusztítják el a programozói közösséget.
kiprinteljen egy olyat, hogy a codecool bp is destroyed, codecool msc destroyed stb
a sírástól zárlatosak lesznek, és vészüzemmódba teszik magukat,
amíg a megfelelő emberek újra nem programozák őket

"""
