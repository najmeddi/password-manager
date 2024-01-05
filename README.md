# Password Management Application

This Python script is a password management application that provides various functions for managing passwords, encrypting files, and customizing application settings. It uses the AES encryption algorithm for secure password storage and file encryption.

## Features

- View passwords: Decrypts and displays the stored passwords.
- Generate password: Generates a new password and appends it to the existing list of passwords.
- Encrypt file: Encrypts a file using the AES algorithm.
- Open another file: Allows the user to switch to a different encrypted file.
- Settings: Provides options to customize application settings, such as the default file and password generator length.
- Exit: Quits the application.

## Prerequisites

- Python 3.x
- AES library (aes.py)
- Password generator library (password_generator.py)
- PyCryptodome as cryptographic library (to install, run `pip install pycryptodome`)

## Usage

1. Clone the repository or download the script file.
2. Ensure that the required libraries (aes.py and password_generator.py) are present in the same directory.
3. Run the script using Python: `python password_manager.py`.
4. Follow the on-screen prompts and select the desired options from the menu.

## Configuration File

The application stores some settings in a configuration file (`PassViewerConfig.txt`). If the file does not exist, it will be created automatically with default values. The settings can be modified through the "Settings" option in the menu.

## File Structure

- `password_manager.py`: The main Python script containing the password management application.
- `aes.py`: The AES encryption library.
- `password_generator.py`: The password generator library.
- `PassViewerConfig.txt`: The configuration file for storing application settings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
