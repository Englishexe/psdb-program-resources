"""
Python Simple DataBase - PSDB
Copyright (C) 2023 Englishexe
GPL-3.0 License

Programmed by Englishexe

Main repository: https://github.com/Englishexe/psdb/
Resource repository: https://github.com/Englishexe/psdb-program-resources/
THIS PROGRAM: https://github.com/Englishexe/psdb-program-resources/DUMPDECODER.py
Refer to the main GitHub repository for the legal agreement, documentation and more.
"""
print("Python Simple DataBase - PSDB - DUMPDECODER.py")
print("Copyright (C) 2023 Englishexe")
print("GPL-3.0 License")
import base64
import sys
if not (sys.version_info.major == 3 and sys.version_info.minor >= 8):
    print(f"Python must be running 3.11 or above. ({sys.version_info.major}.{sys.version_info.minor})")
    exit()
Text = input("Enter B64:")
try:
    Text = Text.removeprefix("b'")
    Text = Text.removesuffix("'")
    print("Prefix / Suffix found <-- Thats okay!")
except:
    print("Prefix / Suffix not found <-- Thats okay!")
print("Decoding...")
try:
    Text = base64.b64decode(Text)
    Text = Text.decode("ascii")
except:
    print("Failed to decode, is the input B64?")
    exit()
print("Decoded text:")
print(Text)
print("=======")
Text = Text.split("|")
List = ["V       ", "RAWURL  ", "HideNet ", "Output  ", "#DB     ", "DBs     ", "Started ", "Debug   ", "Maindir ", "CWD     ", "error#  ", "Time    ", "Date    ", "Response"]
try:
    counter = 0
    print("Fancy Text:")
    for item in Text:
        if List[counter] == "Started " and item == "False":
            print(f"{List[counter]} : {item} <------ PSDB was not started")
        else:
            print(f"{List[counter]} : {item}")
        counter += 1
except:
    print("Failed to split, is the input B64?")
    exit()
exit() # Yes I know bit dumb but good practice