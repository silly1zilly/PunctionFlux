import os
import time
import subprocess

subprocess.Popen(["python", "color_loop.py"])

os.system("cls")

print("For an ASCII refrence sheet, visit https://www.ascii-code.com \n")
print("IMPORTANT! \nvisit code for values. Type exit to quit.\n")
print("Start Typing now.")

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


boo1 = True
while boo1 == True:         # Main loop for input and exiting.
    ans = input("\n")
    if ans.lower() == "exit":
        break
    run_dotcomma(ans)