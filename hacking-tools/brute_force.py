import hashlib
import tkinter as tk
from tkinter import filedialog

def get_md5_hash(word):
    return hashlib.md5(word.encode()).hexdigest()

def compare_hashes(word_hash, user_hash):
    return word_hash == user_hash

def read_word_list(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_word_hash_list(word_list):
    word_hash_list = {}
    for word in word_list:
        word_hash_list[get_md5_hash(word.strip())] = word.strip()
    return word_hash_list

def compare_word_hashes(word_hash_list, user_hash):
    for word_hash in word_hash_list:
        if compare_hashes(word_hash, user_hash):
            return word_hash_list[word_hash]
    return None

def open_file():
    filename = filedialog.askopenfilename(initialdir='.', title='Select file', filetypes=[('Text files', '*.txt')])
    word_list = read_word_list(filename)
    word_hash_list = get_word_hash_list(word_list)
    user_hash = user_hash_entry.get()
    match = compare_word_hashes(word_hash_list, user_hash)
    if match:
        result_label.config(text='Match found: ' + match)
    else:
        result_label.config(text='No match found.')

# Create the GUI
root = tk.Tk()
root.title('Hash Matcher')
root.geometry('300x150')

file_label = tk.Label(root, text='Select word list file:')
file_label.pack()

file_button = tk.Button(root, text='Open', command=open_file)
file_button.pack()

user_hash_label = tk.Label(root, text='Enter hash:')
user_hash_label.pack()

user_hash_entry = tk.Entry(root)
user_hash_entry.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()