from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import time
import os
import random


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


def print_starwars(lines, sleep=1):
    for line in lines:
        print(line)
        time.sleep(sleep)


def print_text_slowly(lines, sleep=1):
    for line in lines:
        line_chars = ""
        for char in line:
            line_chars += char
            print(line_chars, end='\r')
            time.sleep(0.05)
        time.sleep(sleep)
        print()


print_starwars(text, 0.6)
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
print("\n\n                          A MentorBot's Life (in (n)OO way)")
time.sleep(5)
# TODO: bots wanna
main_story = ["One day when Humen Rajtnau went to Codecool Miskolc",
              "<< CODECOOL_MSC GENERATED >>",
              "he realised that the MentorBots needed an upgrade,",
              "because they got boring and lazy, and their knowledge",
              "has became outdated a long time ago.",
              "So he started to collect all the MentorBots...",
              "... after 5 hours he got so bored",
              "he gave his task to codecoolers.",
              "",
              "The codecoolers started working on their laptops,",
              "<< CODECOOLERS GET LAPTOPS >>",
              "They started coding the bots...",
              "Everybody worked hard, so their energy level decreased",
              "<< CODECOOLERS ENERGY_LEVEL DECREASED >>",
              "According to Waterfall model they started testing the bots.",
              "<< MENTORBOTS GET DEVICES >>",
              "<< CHANGING IMIBOT'S DEVICE TO A HOMEBREWER >>"]

print_text_slowly(main_story[:1])
codecool_msc = CodecoolClass.generate_local()
time.sleep(1)
print_text_slowly(main_story[1:6])
time.sleep(3)
print_text_slowly(main_story[6:10])
for student in codecool_msc.students:
    student.set_device("Fujitsu Laptop", 100)
print_text_slowly(main_story[10:12])
for index in range(5):
    rand = random.randint(0, len(codecool_msc.students))
    person1 = codecool_msc.students[rand]
    person2 = codecool_msc.students[rand + 1]
    person1_increase = random.randint(1, 20)
    person2_decrease = random.randint(1, 30)
    person1.knowledge_level += person1_increase
    person2.energy_level -= person2_decrease
    helping = ["'{}' asked for help from '{}'".format(person1.fullname, person2.fullname),
               "{}'s knowledge increased by {} while {}'s energy decreased by {}".format(person1.first_name,
                                                                                         person1_increase,
                                                                                         person2.first_name,
                                                                                         person2_decrease)]
    print_text_slowly(helping)
for student in codecool_msc.students:
    student.energy_level -= random.randint(1, 10)
print_text_slowly(main_story[12:14])
for mentor in codecool_msc.mentors:
    mentor.set_device("Alienware Laptop", 2000)
    if mentor.nickname.casefold() == "Imicsanga".casefold():
        mentor.set_device("Homebrewer 2000", 5000)
print_text_slowly(main_story[14:15])
print_text_slowly(main_story[15:16])


""" mindenki exmentor lesz, együtt elkezdenek inni,
annyira részegek lesznek, hogy elpusztítják a codecoolt és mindenkit aki tud programozni,
így pusztítják el a programozói közösséget.
kiprinteljen egy olyat, hogy a codecool bp is destroyed, codecool msc destroyed stb
a sírástól zárlatosak lesznek, és vészüzemmódba teszik magukat,
amíg a megfelelő emberek újra nem programozák őket

"""
