from time import sleep

print("Welcome to Code Soldiers' auto debugger! Let's get debug your freakin' awsome code 😁 !\n")


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    if iteration == total:
        print()

items = list(range(0, 57))
index = 0
width = len(items)

printProgressBar(index, width, prefix='Progress:', suffix='Complete', length=50)
for item in items:
    sleep(0.18)
    index += 1
    printProgressBar(index, width, prefix='Progress:', suffix='Complete', length=50)

print("\n1 Error found: FileNotFoundError\nDescription: [Errno 2] No such file or directory: 'codecool_class.py'\n")
print(input("Press enter to continue...\n"), end='\r')

index = 0
printProgressBar(index, width, prefix='Searching codecool_class.py:', suffix='Complete', length=50)
for item in items:
    sleep(0.2)
    index += 1
    printProgressBar(index, width, prefix='Searching codecool_class.py:', suffix='Complete', length=50)

print("\nFile was found!\n")
print(input("Press enter to continue...\n"), end='\r')

index = 0
printProgressBar(index, width, prefix='Debugging:', suffix='Complete', length=50)
for item in items:
    sleep(0.08)
    index += 1
    if index == 57:
        sleep(10)
    printProgressBar(index, width, prefix='Debugging:', suffix='Complete', length=50)

with open("story.py", "r+") as input_file:
    lines = input_file.readlines()
with open("story.py", "w+") as output_file:
    for line in lines:
        if line != "print(error_message)\n" and line != "sys.exit(0)\n":
            output_file.write(line)

print("\nDebugging was successfull!\n")
sleep(1)
for index in range(10, 0, -1):
    text = "Code Soldiers' auto debugger will exit in {}. Have fun and do not worry, I will be back 😉 !".format(index)
    print(text, end='\r\r')
    sleep(1)
