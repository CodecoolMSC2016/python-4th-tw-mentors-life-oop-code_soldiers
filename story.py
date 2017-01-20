from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from ex_mentor import Ex_Mentor
import sys
import time
import os
import random


os.system("clear")
print("A long time ago in a galaxy far, far away...")
time.sleep(2)
os.system("clear")
print("\n" * 30)
text = ["A man from India, Humen Rajtnau was tired of mentorbots,",
        "so he got started to implement  some new extra features,",
        "but he became  so lazy  he gave his job  to codecoolers.",
        "",
        "Unfortunately   they  did  not  realise  a  deadly  bug,",
        "which  not  only  could  destroy  the  entire  Codecool,",
        "but the whole programmer community..."]
text += ["" for x in range(30)]


def print_starwars(lines, sleep=1):
    for line in lines:
        print(line)
        time.sleep(sleep)


def print_text_slowly(lines, sleep=0.33):
    for line in lines:
        line_chars = ""
        for char in line:
            line_chars += char
            print(line_chars, end='\r\r')
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
print(error_message)
sys.exit(0)
print("   |   (----`|  |  |  | |  |     |  .--.  ||  | |  |__   |  |_)  |      |   (----`")
print("    \   \    |  |  |  | |  |     |  |  |  ||  | |   __|  |      /        \   \    ")
print(".----)   |   |  `--'  | |  `----.|  '--'  ||  | |  |____ |  |\  \----.----)   |   ")
print("|_______/     \______/  |_______||_______/ |__| |_______|| _| `._____|_______/    ")
print("\n\n                          A MentorBot's Life (in (n)OO way)")
time.sleep(2)
main_story = ["One day when Humen Rajtnau went to Codecool Miskolc",
              "<< CODECOOL_MSC GENERATED >>",
              "he realised that the MentorBots needed an upgrade,",
              "because they became boring and lazy, and their knowledge",
              "has became outdated a long time ago.",
              "So he started to collect all the MentorBots...",
              "... after 5 hours he got so bored,",
              "he gave his task to codecoolers.",
              "",
              "Humen had some requirements for example:",
              "--> MentorBots should communicate with each other on a server",
              "--> MentorBots should learn from each other",
              "--> MentorBots should capabile of work just in Coodecool Miskolc (no other school)",
              "--> Codecoolers must use waterfall method - even if it causes intolerable pain (in the butt)",
              "The codecoolers started working on their laptops,",
              "<< CODECOOLERS GET LAPTOPS >>",
              "They started coding the bots...",
              "Everybody worked so hard, their energy level decreased",
              "<< CODECOOLERS ENERGY_LEVEL DECREASED >>",
              "According to Humen's requirements, they started testing the bots.",
              "To communicate with each other,",
              "every MentorBot got a first and last name, a birth date, a gender, and a nickname.",
              "<< MENTORBOTS NOW CAN COMMUNICATE WITH EACH OTHER ON A SERVER >>",
              "Because they are 'Mentors' they need a device,",
              "so Humen ordered some new Alienware laptops for them.",
              "<< MENTORBOTS GET DEVICES >>",
              "Atesz realised that the energy level of the class is very low,",
              "so he made coffee for everybody.",
              "<< CLASS ENERGY IS INCREASED >>",
              "Meanwhile Imicsanga system got an unknown error,",
              "so he made a horrible(?) decision...",
              "<< IMICSANGA SOLD HIS LAPTOP ON THE NET AND BOUGHT A HOMEBREWER >>",
              "Humen heard about it and became very upset.",
              "He just fired Imicsanga 😧 !",
              "He was so angry he forgot one rule of the new MentorBots:",
              "They should only capable of work in Codecools!",
              "<< IMICSANGA BECAME AN EX MENTOR >>",
              "The codecoolers have not writen a function what a MentorBot should do if he gets fired.",
              "So Imicsanga started crying and drinking because he do not what to do without Codecool.",
              "<< IMICSANGA ALCOHOL_LEVEL INCREASED >>",  # 39
              "Because every MentorBot are connected with Imicsanga, their system crashed...",
              "Their and codecoolers' laptops too!",
              "<< ALL LAPTOPS BROKEN! >>",
              "After destroying laptops, they started destroying Codecool and codecoolers.",
              "<< CODECOOL STUDENTS ELIMINATED >>",
              "<< CODECOOL_MSC DESTROYED >>",
              "Without Codecool and codecoolers, the MentorBots did not know what's next...",
              "So they just put themselves into sleep mode,",
              "until someone can make a stable firmware for them...",
              "Maybe there is somebody...",
              "Maybe?"]

print_text_slowly(main_story[:1])
codecool_msc = CodecoolClass.generate_local()
time.sleep(1)
print_text_slowly(main_story[1:15])
for student in codecool_msc.students:
    student.set_device("Fujitsu Laptop", 100)
print_text_slowly(main_story[15:17])
for index in range(3):
    rand = random.randint(0, len(codecool_msc.students) - 2)
    person1 = codecool_msc.students[rand]
    person2 = codecool_msc.students[rand + 1]
    person1_increase = random.randint(1, 20)
    person2_decrease = random.randint(1, 30)
    person1.knowledge_level += person1_increase
    person2.energy_level -= person2_decrease
    helping = ["'{}' asked for help from '{}'".format(person1.fullname, person2.fullname),
               "{}'s knowledge increased by {} while {}'s energy decreased by {}.".format(person1.first_name,
                                                                                          person1_increase,
                                                                                          person2.first_name,
                                                                                          person2_decrease)]
    print_text_slowly(helping)
for student in codecool_msc.students:
    student.energy_level -= random.randint(1, 10)
print_text_slowly(main_story[17:22])
for index in range(len(codecool_msc.mentors)):
    name = codecool_msc.mentors[index].fullname
    birth = codecool_msc.mentors[index].year_of_birth
    gender = codecool_msc.mentors[index].gender
    nickname = codecool_msc.mentors[index].nickname
    mentor = ["Name: {}, Birth date: {}, Genger: {}, Nickname: {}".format(name, birth, gender, nickname)]
    print_text_slowly(mentor)
print_text_slowly(main_story[22:25])
for mentor in codecool_msc.mentors:
    mentor.set_device("Alienware Laptop", 2000)
print_text_slowly(main_story[25:28])
for student in codecool_msc.students:
    random_energy = random.randint(1, 15)
    student.energy_level += random_energy
print_text_slowly(main_story[28:31])
for mentor in codecool_msc.mentors:
    if mentor.nickname.casefold() == "Imicsanga".casefold():
        mentor.device = ("Homebrewer 2000", 2000)
print_text_slowly(main_story[31:36])
for index in range(len(codecool_msc.mentors) - 1):
    if codecool_msc.mentors[index].nickname == "Imicsanga":
        first = codecool_msc.mentors[index].first_name
        last = codecool_msc.mentors[index].last_name
        year = codecool_msc.mentors[index].year_of_birth
        gender = codecool_msc.mentors[index].gender
        nick = codecool_msc.mentors[index].nickname
        dev = codecool_msc.mentors[index].device
        imicsanga = Ex_Mentor(first, last, year, gender, nick, dev)
        codecool_msc.mentors.remove(codecool_msc.mentors[index])
print_text_slowly(main_story[36:39])
for index in range(3):
    imicsanga.set_alcohol_level(1)
    print_text_slowly(imicsanga.cry())
    print_text_slowly(main_story[39:40])
print_text_slowly(main_story[40:42])
for mentor in codecool_msc.mentors:
    mentor.device.is_broken = True
for student in codecool_msc.students:
    student.laptop.is_broken = True
print_text_slowly(main_story[42:44])
del(codecool_msc)
print_text_slowly(main_story[44:50])
time.sleep(5)
os.system("clear")
print_text_slowly(main_story[50:], 1)
