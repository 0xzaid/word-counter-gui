# Word Counter 

This script defines a graphical user interface (GUI) for a word counter tool using the `tkinter` library.

## GUI Components

The GUI has the following components:
- A text field where the user can input some text or select a file to be processed
- A button to continue with the processing
- A label to display the statistics about the input text or file
- Radio buttons to allow the user to select the input method (text or file)

## Functions

The script defines the following functions:

- `gui`: sets up the GUI and starts the event loop that listens for and handles user events
- `select_file`: allows the user to select a file using a file dialog and stores the `selected file` in the global selected_file variable
- `process_data`: processes the input text or file and displays the statistics in the GUI
- `process_input`: processes the input text or file and returns the statistics as a string
- `read_file`: reads the contents of the file stored in the `selected_file` variable

## Other imports

The script also imports the following modules and functions:
- `re` (regular expression): used to compile a regular expression pattern that matches any non-alphabetic characters
- `tkinter`: provides the GUI components
- `os`: used to get the current working directory (cwd) when opening the file dialog
- `nltk.download`: downloads the Punkt tokenizer, which is used to split the input text into individual words

## Installation

To install the required packages for this script, you can use `pip` and the provided `requirements.txt` file:
```
pip install -r requirements.txt
```

This will install the following packages:
- `nltk`: a library for natural language processing tasks such as tokenization, stemming, and lemmatization

Make sure you have `pip` installed on your system. If you don't have it installed, you can install it by running `pip install pip`.

Note that the `requirements.txt` file only lists the packages that are used in this script. If you want to use the Punkt tokenizer, you will need to download it separately using `nltk.download('punkt')`. This is done in the script by calling `nltk.download('punkt')` at the beginning of the script.
<<<<<<< HEAD

## PyInstaller

1. Install Pyinstaller using `pip install pyinstaller`
2. Run the following command to create a single executable file:
```
pyinstaller wc.py
```
This will create a `dist` folder in the same directory as `wc.py`, which will contain the compiled executable.
Note: If you want to specify a different name for the executable or the folder where it will be placed, you can use the `--name` and `--out` options, respectively. For example:
```
pyinstaller wc.py --name=my_executable --out=build
```
This will create a `build` folder in the same directory as `wc.py`, which will contain the compiled executable named `my_executable`.
```
pyinstaller wc.py --add-data "assets;assets" --icon=assets/mainicon.ico --name=my_executable
```
This will create a `dist` folder in the same directory as `wc.py`, which will contain the compiled executable named `my_executable`. The `--add-data` option is used to include the `assets` folder in the executable. The `--icon` option is used to specify the icon that will be used for the executable.
=======
>>>>>>> d8e92d00bb9548f71fa7859c3a87422f1941646e
