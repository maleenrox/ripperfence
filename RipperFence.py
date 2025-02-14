# Greetings... Another program inspector, huh?

# Welcome to Ripper Fence 1.0 by MS Rox - The Ultimate Password Fortress!
# License: MIT License (see LICENSE file for details)

# This script is so secure, even the NSA might take notes!
# I haven't commented on some places... keep them a secret! ok? ;)

import secrets  # Secure random number generator for cryptographic use
import string  # String manipulation for password characters
import os  # OS-related functions
import sys  # System functions for program control
import gc  # Garbage collection for memory management
import platform  # Detect operating system
import subprocess  # Run system commands
from pathlib import Path  # File and folder path management
from datetime import datetime  # Date and time management

# ASCII Art and Program Banner
print(
    '''
        
                      ...                            
                     ;::::;                           
                   ;::::; :;                          
                 ;:::::'   :;                         
                ;:::::;     ;.                        
               ,:::::'       ;           OOO        
               ::::::;       ;          OOOOO        
               ;:::::;       ;         OOOOOOOO       
              ,;::::::;     ;'         / OOOOOOO      
            ;:::::::::`. ,,,;.        /  / DOOOOOO    
          .';:::::::::::::::::;,     /  /     DOOOO   
         ,::::::;::::::;;;;::::;,   /  /        DOOO  
        ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
        :`:::::::`;::::::;;::: ;::#  /            DOOO
        ::`:::::::`;:::::::: ;::::# /              DOO
        `:`:::::::`;:::::: ;::::::#/               DOO
         :::`:::::::`;; ;:::::::::##                OO
         ::::`:::::::`;::::::::;:::#                OO
         `:::::`::::::::::::;'`:;::#                1 
          `:::::`::::::::;' /  / `:#                  
           ::::::`:::::;'  /  /   `#               

    RRRR  III PPPP  PPPP  EEEE RRRR      FFFF EEEE N   N  CCC EEEE      11      000  
    R   R  I  P   P P   P E    R   R     F    E    NN  N C    E        111     0  00 
    RRRR   I  PPPP  PPPP  EEE  RRRR      FFF  EEE  N N N C    EEE       11     0 0 0 
    R R    I  P     P     E    R R       F    E    N  NN C    E         11  .. 00  0 
    R  RR III P     P     EEEE R  RR     F    EEEE N   N  CCC EEEE     11l1 ..  000 
----------------------------------------------------------------------------------------
                              Ripper Fence 1.0 by MS Rox
----------------------------------------------------------------------------------------
    ''')

program = str("start")  # Main program control variable

def rangePicker(start: int, end: int) -> int:
    return secrets.choice(range(start, end + 1))

def choiceCharacter(limiter, type):
    loop = 0
    passChar = ""

    while loop < limiter:
        character = secrets.choice(type)
        print(f"Choose '{character}' to Password")
        passChar += character
        loop += 1
    return passChar

def shuffle_array(arr):
    shuffled = arr[:]
    for x in range(0, 3):
        for y in range(len(shuffled) - 1, 0, -1):
            z = secrets.randbelow(y + 1)
            shuffled[y], shuffled[z] = shuffled[z], shuffled[y]
        return shuffled

# Help Section
def helpPrint():
    print('''
 ----------------------------------------------------------------------------------------
                                   Ripper Fence - HELP
 ----------------------------------------------------------------------------------------
   *** PURPOSE ***
 Generate uncrackable passwords to defend against brute-force tools like John the Ripper, 
 Hydra, and Medusa. Named to counter the infamous "JOHN THE RIPPER" password cracker!

   *** HOW TO USE ***
 1. Password Length:
    - Enter a number (e.g., "16"). 
    - >> STRONG TIP: Use ≥16 characters to exponentially increase cracking time!
    - Short passwords (<10) trigger warnings (easily hacked in seconds).

 2. Commands:
   
    - [1] Save Password in User Folder - Stores the password and note in a User Folder .txt file.
    - [2] Copy The Password to Clipboard - Copy Your Password to your own place.
    - [3] New Password - Regenerates a fresh password with new randomness
    - [4] Exit - Terminates the program safely
    - [h]elp: Show this menu.
    - [a]bout: Learn about the tool.
    - [s]kip: Skip the Error Folder Path Input Option.

   *** PASSWORD STRENGTH TIPS ***
 ☑ Length Matters: 
    - 16+ characters force brute-force tools to take YEARS to crack.
    - Example: A 12-character password with mixed types = 95¹⁶ possible combinations!
         (95¹⁶ = 44,012,666,865,176,569,775,543,212,890,625 = 44 nonillion)
 ☑ Mix Character Types: 
    - This tool guarantees uppercase, lowercase, digits, and symbols.
    - Avoid patterns like "Password123$" – use randomness!
 ☑ Avoid Personal Info:
    - No birthdays, pet names, or dictionary words. 
 ☑ Unique Passwords:
    - Never reuse passwords across accounts. Use a unique one for every service.

   *** BRUTE-FORCE RESISTANCE ***
 This tool defeats tools like:
    - John the Ripper: Uses advanced rules to guess passwords – long/complex passwords break its logic.
    - Hydra/Medusa: Network brute-force tools – strong passwords make attacks impractical.
 How it works:
    - Secure Randomness: Uses cryptographic algorithms (secrets module) – no predictable patterns.
    - Shuffle 7 Times: Guarantees entropy, making dictionary/rule-based attacks fail.
    - Symbols & Character Diversity: Increases keyspace (e.g., 'P@ssw0rd' -> weak vs 'gT8#mXq$Lz*v' -> unbreakable).

  *** SECURITY TIPS ***
    ☑ Never reuse passwords – use a unique one for every account.
    ☑ Store saved files in encrypted drives (e.g., VeraCrypt).
    ☑ Enable 2FA (Two-Factor Authentication) where possible.

  *** TROUBLESHOOTING ***
    - "Invalid input": Enter whole numbers (e.g., 12), not text/symbols.
    - File save issues: Check desktop write permissions or manually specify a folder.
    - Clipboard errors: Ensure clipboard tools (e.g., xclip on Linux) are installed.
   ----------------------------------------------------------------------------------------
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


''')

# About Section
def aboutPrint():
    print('''
 ----------------------------------------------------------------------------------------
                                   Ripper Fence - ABOUT
 ----------------------------------------------------------------------------------------
   *** PROGRAM OVERVIEW ***
 Ripper Fence 1.0 is a cryptographically secure password generator designed to create 
 uncrackable passwords. Built to counter brute-force tools like **John the Ripper**, 
 it ensures your accounts, networks, and data stay protected against modern hacking threats.

   *** OBJECTIVE ***
    - Generate Strong Passwords: Combine uppercase, lowercase, digits, and symbols for 
      maximum entropy.
    - Defend Against Attacks: Make brute-force/dictionary attacks (e.g. John the Ripper, Hydra, Medusa) 
      mathematically impractical.
    - Educate Users: Promote cybersecurity awareness through password strength tips.

   *** DEVELOPER BACKGROUND ***
 Created by **MS Rox**, a cybersecurity enthusiast and software developer, as their 
 **FIRST CYBERSECURITY TOOL**. This project reflects a passion for building practical 
 tools to combat digital threats. Key interests include:
    - Ethical hacking defense tools
    - Cryptographic algorithms
    - Open-source security initiatives

   *** CONTACT & LINKS ***
    - GitHub(Code & Updates) :- https://github.com/maleenrox/ripperfence    

   *** LICENSE ***
    - MIT LICENSE (https://github.com/maleenrox/ripperfence/blob/main/LICENSE)

 ----------------------------------------------------------------------------------------
 "Every expert was once a beginner. This is my first step toward securing the digital world."  
                                                                                  — MS Rox
 ----------------------------------------------------------------------------------------
                                 <-- Released in 1/31/2025 -->
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


''')

# Main Program
while program == "start" :

    mainpass = str("")
    inputValid = str("Start")
    passLength = int()  # Initialize variable for password length

    # Input validation loop
    while inputValid != "Valid":
        print(''' Ripper Fence Generate uncrackable passwords to defend against brute-force tools like John the Ripper.  

  ** Steps **:  
    1. Enter password length (≥16 recommended).  
    2. Tool auto-generates a mix of UPPERCASE, lowercase, digits, and symbols.  
    3. Add Note
    4. Save to desktop or regenerate.  

  ** Why 16+ ? **:  
    - 16+ characters = 95¹⁶ combinations → Brute-force attacks take CENTURIES.
        (95¹⁶ = 44,012,666,865,176,569,775,543,212,890,625 = 44 nonillion)  

  ** Quick Commands **:  
    h - [h]elp: Security tips & tool mechanics.  
    a - [a]bout: Developer info & contact.  
        ''')

        print(" ----------------------------------------------------------------------------------------")
        passLengthIn = str(input("\tEnter the desired Number of password length (Integer or [h]elp / [a]bout): - "))
        print(" ----------------------------------------------------------------------------------------" + "\n")

        # Ensures correct password length input
        if (passLengthIn == "h") or (passLengthIn == "H") or (passLengthIn == "help"):
            helpPrint()
            print(" Re-enter the Password Length...")
            print(" ----------------------------------------------------------------------------------------" + "\n")
        elif (passLengthIn == "a") or (passLengthIn == "A") or (passLengthIn == "about"):
            aboutPrint()
            print(" Re-enter the Password Length or type 'h' for Help...")
            print(" ----------------------------------------------------------------------------------------" + "\n")
        else:
            try:
                passLength = int(passLengthIn)
                if passLength <= 0:
                    print(" !!! Invalid input. Re-enter the Length or type 'h' for Help...\n")
                    inputValid = "Invalid"
                elif (0 < passLength) and (passLength < 10):
                    print(" !!! Very Weak Length. Re-enter the Length or type 'h' for Help...\n")
                    inputValid = "weak"
                elif (10 < passLength) and (passLength < 16):
                    weekPassOp = "Start"
                    while weekPassOp != "Clear":
                        print(f''' !! Strong passwords require a minimum Length of 16 Characters...\n''')
                        weekPass = input(f" Are you sure you want to proceed with {passLength} Characters? "
                                         f"(Yes = 'y'/No = 'n'/Help = 'h'): - ")
                        if (weekPass == 'y') or (weekPass == 'Y'):
                            print(f'''\n ! Starting Generate with {passLength} Characters Length...''')
                            print("----------------------------------------------------------------------------------------\n")
                            inputValid = "Valid"
                            weekPassOp = "Clear"
                        elif (weekPass == 'n') or (weekPass == 'N'):
                            print('''\n Great Choice. Re-enter the Length or type 'h' for Help...''')
                            print("----------------------------------------------------------------------------------------\n")
                            inputValid = "Invalid"
                            weekPassOp = "Clear"
                        elif (weekPass == "h") or (weekPass == "H") or (weekPass == "help"):
                            helpPrint()
                            weekPassOp = "helpState"
                        else:
                            print('''\n !!! Invalid input. Re-enter the Option [y/n] or type 'h' for Help...''')
                            print("----------------------------------------------------------------------------------------\n")
                            weekPassOp = "Error"
                else:
                    print(f'''\n Starting Generated with {passLength} Characters Length...''')
                    inputValid = "Valid"
            except ValueError:
                print('''\n !!! Invalid input. Re-enter the Length or type 'h' for Help...''')
                inputValid = "Invalid"
            print("----------------------------------------------------------------------------------------\n")

    # Generating password components
    RanNum = [0,0,0,0]
    picLength = 0

    for i in range(0, 3):
        remLength = int(passLength) - picLength
        charNum = int(remLength / (4-i))
        RanNum[i] = rangePicker((charNum - 1), (charNum + 1))
        picLength += RanNum[i]
    RanNum[3] = passLength - picLength

    coLenNum = shuffle_array(RanNum)

    print("Starting Capital Letter Picking to Password core...")
    capitalPart = str(choiceCharacter(coLenNum[0], string.ascii_uppercase))
    print("Capital Letter Picking Finished...")

    print("Starting Number Picking to Password core...")
    numberPart = str(choiceCharacter(coLenNum[1], string.digits))
    print("Numbers Picking Finished...")

    print("Starting Symbol Picking to Password core...")
    allowedSymbols = "!@#$%^&*()_+-=[]:;,.?/"
    symbolPart = str(choiceCharacter(coLenNum[2], allowedSymbols))
    print("Symbol Picking Finished...")

    print("Starting Simple Letter Picking to Password core...")
    simplePart = str(choiceCharacter(coLenNum[3], string.ascii_lowercase))
    print("Simple Letter Picking Finished...")

    # Combining and randomizing password
    print("\nStarting Assembling Password core...")
    mainPass = str(numberPart + symbolPart + capitalPart + simplePart)
    print("Assembling Finished..." + "\n")

    # print(mainPass)

    print("Starting Randomizing Password Characters...")
    n = int(0)

    # Shuffle password 7 times to increase randomness
    while n < 7:
        randomList = list(mainPass)
        for i in range(len(randomList) - 1, 0, -1):
            j = secrets.randbelow(i + 1)    # Cryptographic shuffling
            randomList[i], randomList[j] = randomList[j], randomList[i]
        randomPass = ''.join(randomList)
        mainPass = randomPass
        # print(mainPass)
        n += 1
        print(f"Randomize {n} Round...")
    print("Finish the Randomizing...")
    print("Finish the Password Generation...")

    # Note Input Section
    print("\n----------------------------------------------------------------------------------------")
    print('''
  *** Password Note (Optional) ***  

 Enter a brief description of where this password will be used (e.g., associated service, account, or context).  
 This note will be saved **only in the desktop .txt file** to help you identify the password in the future.  

 *!* Avoid sensitive details like usernames or security questions.  
---------------------------------------------------------------------------------------- 
    ''')
    passNote = str(input("Password Repository Note (Optional): - "))

    if passNote == "":
        passNote = "No Note"

    now = datetime.now()
    dateTimeRec = now.strftime("%Y-%m-%d %H.%M.%S")

    finalPass = mainPass
    print(f'''
    
    
    
*******************************************************************************************
    -----------------------------------------------------------------------------------
            Created Password :- {finalPass}
            Note :- {passNote}
            Generated Time :- {dateTimeRec}
    -----------------------------------------------------------------------------------
*******************************************************************************************
''')

    # Options to save or copy password
    programOption = "start"

    while programOption == "start" :

        print('''  
  *** OPTION Commands ***  
 Use this commands below when prompted to proceed:
  
    - [1] Save Password in User Folder - Stores the password and note in a User Folder .txt file.
    - [2] Copy The Password to Clipboard - Copy Your Password to your own place.
    - [3] New Password - Regenerates a fresh password with new randomness.  
    - [4] Exit - Terminates the program safely. (This Option Safely Clear Your Memory) 
    - [h]elp - View security guidelines and tool mechanics.  
    - [a]bout - Learn about the developer and licensing.  
----------------------------------------------------------------------------------------
        ''')

        # Options to save or copy password
        programOption = str(input("\tYour Option [1/2/3/4/h/a]: - "))

        if programOption == "1":
            print("\nStart Saving Password to Your User Folder...")
            print("----------------------------------------------------------------------------------------" + "\n")
            programOption = "wow"
            program = "print"

                # Folder and file names
            folderName = f"RipperFence Key [{dateTimeRec}]"
            fileName = "Generated Key by RipperFence.txt"
            message = f'''
    
        ____  _                          ______                        ___ ______
       / __ |(_)___  ____  ___  _____   / ____/___ ____  ________     <  // __  /
      / /_/ / / __ |/ __ |/ _ |/ ___/  / /_  / _  / __ |/ ___/ _ |    / // / / /
     / _, _/ / /_/ / /_/ /  __/ /     / __/ /  __/ / / / /__/  __/   / // /_/ / 
    /_/ |_/_/ .___/ .___/|___/_/     /_/    |___/_/ /_/|___/|___/   /_(_)____/  
           /_/   /_/                                                             
-------------------------------------------------------------------------------------

    Password :- {finalPass}
    Note :- {passNote}
    Created Time :- {dateTimeRec}
    
    
-------------------------------------------------------------------------------------
                     Generated From Ripper Fence 1.0 By MS Rox
            '''

            # Detect the operating system
            system = platform.system()

            # Determine the Documents path based on OS
            if system == "Windows":
                one_drive = Path(os.getenv("OneDrive")) if os.getenv("OneDrive") else None
                if one_drive and (one_drive / "Ripper Fence 1.0").exists():
                    documentsPath = one_drive / "Ripper Fence 1.0"
                else:
                    documentsPath = Path.home() / "Ripper Fence 1.0"

            elif system in ["Linux", "Darwin"]:  # Darwin = macOS
                documentsPath = Path.home() / "Ripper Fence 1.0"

            else:
                documentsPath = None  # Mark as None to trigger manual input
                attempts = 3
                while attempts > 0:
                    userPath = input("Enter a valid folder path (s = Skip): ").strip()
                    if userPath.lower() == "s":
                        print("Skipping folder input...")
                        break
                    documentsPath = Path(userPath)
                    if documentsPath.exists():
                        break
                    else:
                        print("Invalid path! Try again.")
                    attempts -= 1
                if attempts == 0:
                    print("Too many invalid attempts. Exiting folder selection.")

            # Create the full path for the new folder
            folderPath = documentsPath / folderName

            # Create the folder if it doesn't exist
            folderPath.mkdir(parents=True, exist_ok=True)

            # Create the full path for the new file
            filePath = folderPath / fileName

            # Write the message to the file
            with filePath.open("w", encoding="utf-8") as file:
                file.write(message)

            print(f"File successfully created at: {filePath}")

            # Open the folder in File Explorer (Windows), Finder (macOS), or File Manager (Linux)
            if system == "Windows":
                subprocess.run(["explorer", str(folderPath)])
            elif system == "Darwin":  # macOS
                subprocess.run(["open", str(folderPath)])
            elif system == "Linux":
                subprocess.run(["xdg-open", str(folderPath)])
            else:
                print("Cannot open folder automatically on this OS.")

            # Example of program control variables
            programOption = "start"
            program = "exit"
        elif programOption == "2":
            # Copy password to clipboard
            system = platform.system()

            try:
                if system == "Windows":
                    subprocess.run("clip", input=finalPass.encode(), check=True)
                    print("Password copied to clipboard!")
                elif system == "Darwin":  # macOS
                    subprocess.run("pbcopy", input=finalPass.encode(), check=True)
                    print("Password copied to clipboard!")
                elif system == "Linux":
                    try:
                        subprocess.run("xclip -selection clipboard", input=finalPass.encode(), shell=True, check=True)
                        print("Password copied to clipboard!")
                    except subprocess.CalledProcessError:
                        subprocess.run("xsel --clipboard --input", input=finalPass.encode(), shell=True, check=True)
                        print("Password copied to clipboard!")
                else:
                    raise OSError("Unsupported operating system")
            except Exception as e:
                print(f"!!! Error copying to clipboard: {e}")
            programOption = "start"
            program = "exit"
        elif programOption == "3":
            # Restart Program to Create New Password
            print("\n Restart Program to Re Create New Password...")
            print("----------------------------------------------------------------------------------------" + "\n")
            programOption = "new"
            program = "start"
            mainpass = ""
            finalPass = ""
            randomPass = ""
            passLength = 0
            passNote = ""
            dateTimeRec = ""
            gc.collect()
        elif programOption == "4":
            # Terminate the program
            print("\n Safely Terminate Program...")
            print("----------------------------------------------------------------------------------------" + "\n")
            programOption = "bye"
            program = "exit"
        elif (programOption == "h") or (programOption == "H") or (programOption == "help"):
            helpPrint()
            programOption = "start"
            program = "start"
        elif (programOption == "a") or (programOption == "A") or (programOption == "about"):
            aboutPrint()
            programOption = "start"
            program = "start"
        else:
            print('''
 Invalid Input, Re Enter Option...
----------------------------------------------------------------------------------------''')
            programOption = "start"
            program = "start"

print("""
    Safely terminates the program and clears sensitive data from memory.
    """)
print("\n Clearing sensitive data from memory...")

# Explicitly delete sensitive variables
if 'finalPass' in globals():
    del globals()['finalPass']
if 'mainPass' in globals():
    del globals()['mainPass']
if 'randomPass' in globals():
    del globals()['randomPass']

print(" Sensitive data cleared. Exiting program safely...\n")
print('''
----------------------------------------------------------------------------------------  
                                  ⚠ SAFETY REMINDER ⚠  
----------------------------------------------------------------------------------------  
**TRUST & TRANSPARENCY**:  
     - This tool does **NOT** store, transmit, or access your password.  
     - Your password exists **only** in the generated .txt file (if saved) and your memory.  

BEFORE YOU GO:  
     - Securely store or delete the saved .txt file.  
     - Never share passwords via insecure channels (email, messaging).  

**Best Practices**:  
     - Use a password manager (e.g., Bitwarden) for encrypted storage.  
     - Enable 2FA (Two-Factor Authentication) on critical accounts.  

Thank you for using Ripper Fence – your security is our priority!  
----------------------------------------------------------------------------------------  
''')
# Force garbage collection to free up memory
gc.collect()

sys.exit(0)  # Exit with status code 0 (success)
