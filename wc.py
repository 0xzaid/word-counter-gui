"""
A program that counts words and other stuff
"""

import re
import tkinter as tk
import nltk
import tkinter.filedialog as filedialog
import os
nltk.download('punkt')


def gui():
    # Create main frame
    frame = tk.Tk()
    frame.title("Word Counter")
    frame.geometry('700x700')
    frame.configure(bg='#3498db')
    frame.resizable(width=False, height=False)
    frame.iconbitmap("assets/mainicon.ico")

    # Create label at the top of the program
    title = tk.Label(frame, text="Input some text, then click on continue to see some stats about it", font=(
        "Arial", 12), bg='#3498db')
    title.pack(side='top', padx=18, pady=20, anchor="w")

    # Radio buttons for selecting input method
    input_method = tk.StringVar()
    input_method.set("text")  # default value

    text_radio = tk.Radiobutton(frame, text="Input text", variable=input_method, value="text",
                                command=lambda: file_select_button.place_forget())
    file_radio = tk.Radiobutton(frame, text="Upload file", variable=input_method, value="file",
                                command=lambda: file_select_button.place(x=220, y=60))

    text_radio.place(x=20, y=60)
    file_radio.place(x=120, y=60)

    # Label to display output
    output = tk.Label(frame, text="", font=(
        "Arial", 11), bg='#3498db')
    # output.pack(side='left', padx=20, pady=30)
    output.place(x=110, y=100)

    def process_data():
        inp = ""
        if input_method.get() == "text":
            inp = inputtxt.get(1.0, "end-1c")
        elif input_method.get() == "file":
            if not selected_file:  # no file selected
                messagebox.showerror(
                    "Error", "No file selected. Please select a file.")
                return
            inp = read_file(selected_file)
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert("1.0", inp)
        result = process_input(inp)
        output.config(text=result)

    # TextBox Creation
    inputtxt = tk.Text(frame, height=22, width=73, wrap='word', borderwidth=2, relief="groove", padx=1,
                       font=("Arial", 12), bg='white')
    inputtxt.place(x=20, y=200)

    # Button Creation
    continueButton = tk.Button(frame,
                               text="Continue",
                               command=process_data,
                               font=("Arial", 12, "bold"),
                               bg='#585858',
                               fg='white')
    continueButton.pack(pady=10, side='bottom')

    # File selection button
    file_select_button = tk.Button(
        frame, text="Select file", command=select_file)

    # Label Creation
    lbl = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg='#3498db')
    lbl.pack(side='bottom')
    frame.mainloop()


def select_file():
    global selected_file
    cwd = os.getcwd()  # get current working directory
    selected_file = filedialog.askopenfilename(initialdir=cwd)
    if not selected_file:  # user cancelled file selection
        return
    try:
        # check if file is valid (e.g. can be opened and read)
        with open(selected_file, 'r') as f:
            f.read()
    except Exception as e:
        # file is invalid
        messagebox.showerror(
            "Error", "Invalid file. Please select a valid file.")
        selected_file = None


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)


def count_characters(text):
    return len(text)


def count_sentences(input_string):
    # Tokenize the input string into sentences
    sentences = nltk.sent_tokenize(input_string)
    # Return the number of sentences
    return len(sentences)


def count_lines(input_string):
    # Split the input string into a list of lines
    lines = input_string.split("\n")
    # Filter out empty lines
    lines = [line for line in lines if line.strip() != ""]
    # Return the number of lines
    return len(lines)


def letter_count(input_string):
    # letter count
    regex = re.compile('[^a-zA-Z]')
    chars = regex.sub('', str(input_string.split()))
    letter_count = len(chars)

    return letter_count


def process_input(data):

    return "Word count: " + str(len(data.split())) + "\t" + \
           "Letter count: " + str(letter_count(data)) + "\t" + \
           "Character count: " + str(count_characters(data)) + "\n\n" + \
           "Most frequent word: " + str(most_frequent(data.split())) + "\t" + \
           "Line count: " + str(count_lines(data)) + "\t" + \
           "Sentence count: " + str(count_sentences(data))


if __name__ == '__main__':
    gui()
