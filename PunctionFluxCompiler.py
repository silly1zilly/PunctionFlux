import os
import time
import subprocess
os.system("color 9")
subprocess.Popen(["python", "color_loop.py"])
boo1 = True

os.system("cls")

yes = ['y', 'yes']
no = ['n', 'no']

manual = input("Read File?\n")
if manual.lower() in yes:
    boo1 = False
    os.system("cls")

if manual.lower() in no:
    os.system("cls")
    print("For an ASCII refrence sheet, visit https://www.ascii-code.com \n")
    print("IMPORTANT! \nvisit code for values. Type exit to quit.\n")
    print("Start Typing now.")
    boo1 = True

def run_dotcomma(code):
    cells = [0] * 100
    ptr = 0

    for c in code:
        if c == ".":       # adds one to current cell.
            cells[ptr] += 1
        elif c == ",":     # adds five to current cell.
            cells[ptr] += 5
        elif c == ":":     # adds ten to current cell.
            cells[ptr] += 10
        elif c == ";":     # adds fifty to current cell.
            cells[ptr] += 50
        elif c == "n":     # Move pointer to the next cell.
            ptr += 1
            if ptr >= len(cells):
                cells.append(0)
        elif c == "b":     # Move pointer back one cell (can go negative).
            ptr -= 1
        elif c == "p":     # Print the value of the current cell.
            print(cells[ptr], end = ' ')
        elif c == "P":     # Print the ASCII character corresponding to the current cell’s value.
            print(chr(cells[ptr] % 256), end = ' ')
        elif c == "D":    # Print both ASCII and Value.
            print(chr(cells[ptr] % 256), end = ' ')
            print(cells[ptr], end = ' ')

while boo1 == True:         # Main loop for input and exiting.
    ans = input("\n")
    if ans.lower() == "exit":
        break
    run_dotcomma(ans)

while boo1 == False:
    try:
        filename = input("Please Enter your .txt file name down below. \n")
        os.system("cls")
        with open(filename, "r") as f:
            code = f.read()
        run_dotcomma(code)
        boo1 = True
    except FileNotFoundError:
        print("File not found.")
