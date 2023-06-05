import random as r
import os

DEFAULT_PASS_LEN = 12
START_INDEX = 48    # starting index i for chr(i) = '0'
END_INDEX = 123     # ending index i for chr(i - 1) = 'z'
CLEAR = 'cls'
EXIT_OPTION = 'exit'
EFILE = "Error: Could not open file."
FILE_LOCATION = r'C:\Users\omidn\Documents\passtest.txt'
EMPTY_INPUT = ''
TITLE = "\n\n\nkXK00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000KXX\n0Nd:cccccccccllcc::ccccccccllcc:::cccccclcc::::cccc:::cccccccccc:::cccc::ccccccccccccccllc::ccccccccccllc:::ccccccclc::::ccccc:::cccccccccc:::cccc:ccccccccccccccllcc::ccccccccllc:::ccccccclcc::::c:c0M\n0Xc'::::::;;cll:;;;:ccc::;:ll:;,;::::::llc:;;ccc:::;;;::::ccc:::;:::::::;:::::::::::;:llc:;;::cc::;::clc;;;;:::::clc:;;:cc::::;;;::::cc:::;;::::::::::::::::::;:clc:;;;:cc::;;cll:;;;:::::cllc:;;ccc;,kM\nKXc';;;::;;;:c:;;;;clc:;;,:c:;,,;;;;;:clc;,;clc::;;;;;;;;:cc:;;;;:::;;;;;;;;;;;;;::;,;::;;;;:clc;;;;;:c;,,;;;;;;clc:,,:ccc:;;;;;;;;;:lc:;;;:::;;;;;;;;;;;;;::;;;:c:;;;:clc:;;,:c:;,,;;;;;:ll:;,;ccc:,'kM\nKXc';;;;:;,,,;;,,,;::;,,,';:;,',;:::ccc;,'',;;,,,,,,,,,,,;::;,,,,,,',,,,,,;:::;;;;:,,,;;,,,;:::;,,',;;;,',;;::ccc:;,',;;,,,,,,,,,,,;::;,,,,,,,',,,,,;;::;;;;:;,',;;,,,;::;,,,';:;,',;:::ccc;,'',;;,,''kM\nKXc.;;,;;;''',,''''''''''',;,'';:::;;;,'''''''''''''''''',;,''''''..''',,,,,,;;;;;;,''',''''',''''.',,,'',:::;;;,''.''''''''''''''',;;,'''''''''',,,,,,;;;,;;,''',,'''''''''.',;,',;::;;;,,'''''''''.'kM\n0X:..''','..''....'''.....','',,,''''''...''''',,,''....'','''.'''...',;,'''''''',,...''.'.'''.....''','',,'''''''..'''''',,''....'',,''.''''.''';;'''''''',,'...''..''''.....','',,,'''.''...''''',''kM\nKX:........'''............'''................',,,'........,,,'..'''...''..',,'.......'.............'',,'................',,'..............''.....''...........................'''...............',;,''kM\nKX:..............'..oOOOOOOxo;.........ckOOOOc.........,d0KXXKOl.......'lOKXXK0d,.....'dOOk;..:kOOo'.....cOOOo.....,xOOOOOOOc.....ckOk:..oOOOk:..lOOo.....:kOOOOOOk;.''..:kOOOOOko:............','....kM\nKX: .............'.'OMMMWNWMMXc........kMMMMMk'.......,0MMWKXWMNl......xWMWXKWMWk.... 'OMMWo..dWMMx.  ...dWMMO'... :XMMWKOOkc.....oWMWd.,KMMMWx.,0MMk.....oWMMN0OOx;.....dWMMNKNMMNo..................kM\nKX: . ............ .OMMWxc0MMMd...... ,0MMMMMK;....   cNMM0;lWMMx.... ,0MMNc;KMM0, ....xWMWx..kMMWo.  . .dWMMO' .  :XMMNl...    . :XMMk.cNMMMMO':XMWo. . .oWMM0;....... .oWMM0:dWMMO'.....   ....... .kM\nKX:    .........   .OMMWo'kMMMx...    cNMMMMMNc.      cNMMK;cNMMx.    ,KMMNc;KMM0, ....lNMMO.'0MMNc......dWMMO'    :XMMNc..       ,0MM0:dWMMMMK:oWMNc    .oWMM0,...     .oWMM0;oWMMO'.          .... .kM\nKX:.........       .OMMWo'kMMMx. ..  .oWMWNWMWd.      :XMMWkclll,   . 'OMMM0lcll:..... :XMM0,;XMMK,   ...dWMM0'    :XMMNc         .OMMXdOMMMMMXdOMMK; ....oWMM0,        .oWMM0;dWMWk. .      .....   .kM\n0X:              . 'OMMWo'kMMMx.     .kMMX0XMMO.      .lXMMW0:.       .;0MMMXo.        '0MMX:cNMMO.     .dWMMO' ...:XMMW0xxo'     .dWMNKNMMMMMWKXMMO'... .oWMMNOxxc. .. .oWMMN0XMXd'     .......     .kM\n0X:            ... .OMMM0kXMMWo.     ,KMM0d0MMK,        ;OWMMNx'        'xNMMW0;.      .kMMNodWMWd.     .dWMMO'    :XMMWNKKO,      lNMMMMMNXWMMMMMMx.     oWMMWXKKd...   oWMMWNWMXo.                 .kM\n0X:                .OMMMMMMWNk'      cNMMKd0MMNl        .'dXMMW0;     ....c0WMMXo.      oWMWkOWMNl      .dWMM0'    :XMMNl...       :XMMMMMOkNMMMMMWo      oWMMK;..       oWMM0cdWMWx.                .kM\n0X:                .OMMMOc:;'.      .dWMMWWWMMWd.     ;k00oc0MMMO.  ..'d00xckWMMX:      cNMMXXMMX: .... .dWMM0'    ;XMMNc          ,0MMMMWdcKMMMMMN:      oWMM0,         oWMM0,lNMM0'                .kM\nKX: .              .OMMWo.          .OMMWOoOWMMO' .   cNMMx.oWMM0, .. ,KMM0,;XMMNc      ;KMMWMMM0,      .dWMM0'    :XMMNc   .      .kMMMMNc,0MMMMMK,  .. .oWMM0'        .oWMM0;lWMMO.                .kM\nKX:                .OMMWo           ;KMMX: :XMMX:..   cNMMx.lWMMK;..  ,KMM0',KMMNc      .OMMMMMMk.      .dWMMO'    :XMMNc  ..      .dWMMMK;.xMMMMMO.      oWMM0'        .oWMM0;lWMMO'                .kM\nKX:    ...         .OMMWo.       ...lNMM0, ,0MMNl.    cXMMKoOWMMO'    '0MMXxxNMMX:      .xWMMMMWo.      .dWMMO'    :XMMWkccc,       lNMMMO'.oWMMMWx..... .oWMMXd:::.    .dWMM0,lNMM0, ....         ...kM\nKX: ......         .kWWNo.      ....dWWWk. .kWWWx.    .dXWMMMMW0:..   .cKWMMMMWKo.      .lNWWWWXc       .dWWWO' .  :XWWWWWWWx.      :KWWWx. :XWWWNl.......oWWWWWWWNl  ...oNWWO';KWWK:......  .... ....kM\n0X: . ..............'::;...... .....':::,...'::;'. ..  .':lllc;.........,:llll:'..........;::;:;. .......';::,. ...';::::::;'. . .. .,::;'. .,::::'...... .;::;:::;. ....':::,..,;;;................ .kM\n0X: ..................................................................................................................................................................................................kM\nKX:...','.........'.............................................................,'.........'..............................................................',..........'...............................kM\nKX:...,,........','.........','......','.......................................','.......'','..........''......','........................................,'........','.........',.......','..........kM\n0X:.'',,''',,;;;;,''',,;,,;;:;'...''',,''....'''..''''''''''',;,''....'''...'''',''',,;;;;;,.',,;;,,;;;;,...''',,'''...'''..''''''''''',;;,'.....''....''',,'',,;;;;;,'',,,;,,;;:;'..'''',,''....'''..kM\nKXc.''','',,;;,,,'';;,,,,;;;,''.''',,;;,''.'',,'',,;:;;,,;;;::;,'''''''''''''''',,',,;;;,,,',;;,,,,;;;;,'''''',;;,'''.',,''',;;:;,,;;;:::;,''''''''''''''',,,',,;;,,,'';;,,,,;;;,''.''',,;;,''.',,,'.'kM\nKNd;:::::::::::::::cc:::::::::::::::clc::::::::::::::::::::::::::::::::::::::::::::::::::::::c::::::::::::::::ccc::::::::::::::::::::::::::::::::::::::::::::::::::::::cc:::::::::::::::ccc:::::::::;c0M\n\n\n"

def clear():
    os.system(CLEAR)

def getPassword(pass_len):
    passLst = []
    password = EMPTY_INPUT
    # Creates list of char containing all alphanumerical characters
    chars = [chr(i)
                 for i in range(START_INDEX, END_INDEX) if chr(i).isalnum()]
    for currCharIndex in range(pass_len):
        canAddChar = False
        while (not canAddChar):
            # Get a random aplhanumeric character
            i = 0
            j = len(chars) - 1
            randChar = chars[r.randint(i, j)]
            if (randChar not in passLst):
                passLst.append(randChar)
                canAddChar=True
    for c in passLst:
        password += c
    return password

def confirmOutput(output):
    isConfirmed = False
    isCorrectInput = False
    while not isCorrectInput:
        userInput = input("Output: " + output +
                          "\nWould you like to save this output(yes/no)?: ")
        if userInput == 'yes':
            isConfirmed = True
            isCorrectInput = True
        elif userInput == 'no':
            isCorrectInput = True
    return isConfirmed


def gen_pass(inputFileName, pass_len=DEFAULT_PASS_LEN):
    success=False
    try:
        f = open(inputFileName, 'a')
        while (True):
            clear()
            password = getPassword(pass_len)
            print("Generated password is: " + password)
            option = input("Would you like to save this password " +
                  "(type: 'yes', 'no', or 'exit' to exit)?: ")
            if (option == 'yes'):
                outputConfirmed = False
                while not outputConfirmed:                
                    prepend = input("Would you like to anything before?: ")
                    pre = EMPTY_INPUT
                    if (prepend == 'yes'):
                        pre = input("Enter: ")
                    appnd = input("Would you like to anything after?: ")
                    post = EMPTY_INPUT
                    if (appnd == 'yes'):
                        post = input("Enter: ")
                    output = pre + password + post
                    outputConfirmed = confirmOutput(output)
                    if outputConfirmed:
                        f.write('\n')
                        f.write(output)
                        success = True
                        break
                if outputConfirmed:
                    break
            elif (option == EXIT_OPTION):
                clear()
                success = True
                break
        f.close()
    except (FileNotFoundError):
        print(EFILE)
    if success:
        print("Operation preformed successfully.")
    else:
        print("Operation failed.")    

if __name__ == "__main__":
    success=False
    try:
        f = open(FILE_LOCATION, 'a')
        while (True):
            clear()
            password = getPassword()
            print(TITLE)
            print("Generated password is: " + password)
            option = input("Would you like to save this password " +
                  "(type: 'yes', 'no', or 'exit' to exit)?: ")
            if (option == 'yes'):
                outputConfirmed = False
                while not outputConfirmed:                
                    prepend = input("Would you like to anything before?: ")
                    pre = EMPTY_INPUT
                    if (prepend == 'yes'):
                        pre = input("Enter: ")
                    appnd = input("Would you like to anything after?: ")
                    post = EMPTY_INPUT
                    if (appnd == 'yes'):
                        post = input("Enter: ")
                    output = pre + password + post
                    outputConfirmed = confirmOutput(output)
                    if outputConfirmed:
                        f.write('\n')
                        f.write(output)
                        success = True
                        break
                if outputConfirmed:
                    break
            elif (option == EXIT_OPTION):
                clear()
                success = True
                break
        f.close()
    except (FileNotFoundError):
        print(EFILE)
    if success:
        print("Operation preformed successfully.")
    else:
        print("Operation failed.")
