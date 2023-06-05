import aes
import password_generator as pg
import os
from os import path

# =========================== CONSTANTS & GLOBAL VARIABLES ==========================================

MIN_PASS_LEN = 4
MAX_PASS_LEN = 100

SELECT_PROMPT_TXT = "\nSelect one of the options listed above and press Enter: "
SELECTION_PREFIX = "You selected "
CONTINUE_TXT = "Press Enter to continue"
CIPHER_FILE_EXT = '.txt'

# Constants for the config file
CONFIG_FILE_NAME = 'PassViewerConfig.txt'
CONFIG_SPLITTER = '='
CONFIG = {'FILE': '', 'PG_LEN': 12}     # Application settings

# Constants referring to errors in application
ERR_PREFIX = "\nERROR"
EFILE = "Could not open file"
EFILEEXT = f'File extension must end with "{CIPHER_FILE_EXT}" (e.g., example{CIPHER_FILE_EXT})'

# A list of all files in current directory
CURR_DIR_FILES = [f for f in os.listdir('.') if os.path.isfile(f) and (f.endswith(CIPHER_FILE_EXT) or f.endswith('.txt'))]

# Main menu options
OPTIONS = [('1', 'View passwords'),
           ('2', 'Generate password'),
           ('3', 'Encrypt file'),
           ('4', 'Open another file'),
           ('5', 'Settings'),
           ('E', 'Exit')]
# ===============================================================================================

# =========================== GENERAL HELPER FUNCTIONS ==========================================

'''(None) -> str
Return a string listing only cipher text files and regular text files in the
current directory this script is in
'''
def get_curr_dir_files():
    result = ''
    num_text_files = len(CURR_DIR_FILES)
    if(num_text_files > 0):
        result += f'There exists [{num_text_files}] file(s) in this directory:\n'
        for f in CURR_DIR_FILES:
            result += f'\n\t- {f}'
    else:
        result += "There aren't any text files in the current directory"

    return result + '\n'

'''(str) -> Exception
Checks if a file with the given name exists in the current directory. If there
is no such file or if the extension of the file is incorrect, then an error
ir raised
'''
def check_file(file_name):
    if (path.exists(file_name)):
            if not (file_name.endswith(CIPHER_FILE_EXT) or file_name.endswith('.txt')):
                raise Exception(EFILEEXT)
    else:
        raise FileNotFoundError

'''(None) -> str
Returns a string representing a list of options with the key to enter and its 
associated function.
'''
def get_options():
    opt_str = 'Options:'
    for i in range(len(OPTIONS)):
        key, func = OPTIONS[i]
        opt_str += f'\n\t[{key}] - {func}'
    return opt_str
# =========================== END OF GENERAL HELPER FUNCTIONS ===========================================

# =========================== HELPER FUNCTIONS FOR CONFIG FILE ==========================================
'''(None) -> None
Creates config file to store data by copying contents in config dictionary.
'''
def init_config_file():
    config_file = open(CONFIG_FILE_NAME, 'w')
    for key in CONFIG:
        config_file.write(f'{key}{CONFIG_SPLITTER}{CONFIG[key]}\n')
    config_file.close()


'''(None) -> None
Load the saved preferences by reading config file and storing values as a dictionary, 
then return the dictionary. If no previously saved data then initialize and create a 
new config file.
'''
def load_config():
    # Init config file if it doesn't exist
    if(not path.exists(CONFIG_FILE_NAME)):
        init_config_file()
    else:
        # Read and store data on file
        config_file = open(CONFIG_FILE_NAME, 'r')
        data = config_file.read()
        config_file.close()

        # Parse data into dictionary
        data_lst = list(map(lambda s: s.split(CONFIG_SPLITTER),
                            data.strip().split('\n')))
        for pair in data_lst:
            config_name, value = pair

            # Check whether integer value or string value
            if(value.isdigit()):
                CONFIG[config_name] = int(value)
            else:
                CONFIG[config_name] = value


'''(None) -> None
Gets the current values in config variable, converts to string,and writes to config file
'''
def save_config():
    init_config_file()

# =========================== END OF HELPER FUNCTIONS FOR CONFIG FILE ==========================================
'''(None) ->
Executes the main application
'''
def main():
     # Make a config file
    load_config()

    # TODO: Change yes and no to y and n

    if(CONFIG['FILE'] == ''):
        # List text files in current directory
        print(get_curr_dir_files())
        inputFileName = (input("Enter the file path: ")).strip()
    else:
        inputFileName = CONFIG['FILE']

    try:
        # Check that the file given is exists in the current directory
        check_file(inputFileName)

        is_option_selected = False
        is_error = False
        err_msg = ERR_PREFIX
        while (not is_option_selected):
            pg.clear()

            # Display the name of the file chosen
            print(f'CURRENT FILE OPEN: {inputFileName}')

            # Display the main menu options
            print(get_options())

            # Display any error(s) if any occurred before the refresh
            if(is_error):
                print( f'{err_msg}\n')
                is_error = False
                err_msg = ERR_PREFIX

            selected_option = input(SELECT_PROMPT_TXT)
            if(selected_option == '1'):
                print(SELECTION_PREFIX + selected_option)
                plaintext = aes.decrypt(inputFileName)

                pg.clear()
                print(str(plaintext, 'utf-8'))
                input(CONTINUE_TXT)

            elif(selected_option == '2'):
                # Decrypt file to append to plaintext
                print(SELECTION_PREFIX + selected_option)
                plaintext = aes.decrypt(inputFileName)  # Original key required

                # Create temporary file to place plaintext for appending
                outputFile = open('temp.txt', 'wb')
                outputFile.write(plaintext)
                outputFile.close()

                # Generate a password (if desired) with the saved password
                # then append the result and encrypt the file again
                pg.gen_pass('temp.txt', int(CONFIG['PG_LEN']))
                aes.encrypt('temp.txt', inputFileName)  # New key or orginal key can be used

                # Remove the the plaintext from the temporary file
                outputFile = open('temp.txt', 'w')
                outputFile.close()

            elif(selected_option == '3'):
                print(SELECTION_PREFIX + selected_option)
                outputFileName = input("Enter the name of the encypted file you want it saved as: ")
                ciphertext = aes.encrypt(inputFileName, outputFileName)
                print(ciphertext)
                print("File saved")
                input(CONTINUE_TXT)

            elif(selected_option == '4'):
                pg.clear()
                print(get_curr_dir_files())
                newInputFileName = (input("Enter the file path: ")).strip()
                check_file(newInputFileName)
                inputFileName = newInputFileName

            elif(selected_option == '5'):
                # A dictonary mapping options to the setting description
                SETTINGS = {
                    1: 'Default file',
                    2: 'Password generator length', 
                    3: 'Back'}

                # Have the settings displayed until user wants go back to the previous menu
                is_done = False
                while not is_done:
                    # Show the initial text for this menu
                    pg.clear()
                    display_txt = 'Application Settings\n'
                    display_txt += f'[{1}] - {SETTINGS[1]}: {CONFIG["FILE"]}\n'
                    display_txt += f'[{2}] - {SETTINGS[2]}: {CONFIG["PG_LEN"]}\n'
                    display_txt += f'[{3}] - {SETTINGS[3]}\n'
                    print(display_txt)
                    selected_setting = input(
                        '\nSelect a setting to change and save, or return to menu: ')

                    # Change the default file that opens when the application starts
                    if(selected_setting == '1'):
                        print(get_curr_dir_files())
                        new_file_name = (
                            input('Enter the name of the file to use as default: ')).strip()
                        check_file(new_file_name)
                        CONFIG['FILE'] = new_file_name
                        save_config()

                        # Check whether the user wants to open the default file now to replace
                        # the current opened file
                        isLoadSelected = False
                        while not isLoadSelected:
                            loadSelectionInput = input(
                                'Would you like to open this file as the current working file (Y/n)?: ')
                            if(loadSelectionInput.upper().strip() == 'Y'):
                                inputFileName = CONFIG['FILE']
                                isLoadSelected = True
                            elif(loadSelectionInput.upper().strip() == 'N'):
                                isLoadSelected = True
                            else:
                                print('Invalid input')

                    elif(selected_setting == '2'):
                        # Prompt the user to give a valid value for the password length until one is given
                        isdigit_given = False
                        while not isdigit_given:
                            new_pass_len = (
                                input('Enter the length of the passwords to be generated: ')).strip()
                            if new_pass_len.isdigit():
                                pass_len = int(new_pass_len)
                                if pass_len >= MIN_PASS_LEN and pass_len <= MAX_PASS_LEN:
                                    CONFIG['PG_LEN'] = pass_len
                                    save_config()
                                    isdigit_given = True
                                else:
                                    print(f'Password length must between {MIN_PASS_LEN}-{MAX_PASS_LEN}')
                            else:
                                print(
                                    'Length must be a numerical value with no decimals')

                    elif(selected_setting == '3'):
                        # User selected to go to the previous menu
                        is_done = True
                    else:
                        print('Invalid option. Please try again')

            elif(selected_option.upper() == 'E'):
                # User selected to exit the application
                print(SELECTION_PREFIX + selected_option)
                is_option_selected = True
            else:
                is_error = True
                err_msg += ': You did not select any of the available options. Try again'

    except (FileNotFoundError):
        print(f'{ERR_PREFIX}: {EFILE} "{inputFileName}"')
        input(CONTINUE_TXT)
        main()
    except Exception as e:
        print(f'{ERR_PREFIX}: {repr(e)}')
        input(CONTINUE_TXT)
        main()

if __name__ == "__main__":
   main()
