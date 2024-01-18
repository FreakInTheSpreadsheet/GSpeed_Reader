import tkinter as tk

current_index = 0
is_running = False
dark_enabled = False

words = []

def dark_mode_toggle():
    global dark_enabled, widget_fg, widget_bg, window_bg
    if dark_enabled:
        dark_enabled = False
        widget_fg = 'black'
        widget_bg = 'white'
        window_bg = 'white'
    else:
        dark_enabled = True
        widget_fg = 'white'
        widget_bg = 'gray30'
        window_bg = 'gray20'
    update_colors()

def display_words(words, index=0):
    if index < len(words):
        word = words[index]
        word_label.config(text=word)
        index += 1
        root.after(1000, display_words, words, index)

#main window
root = tk.Tk()
root.title("Grant's Speed Reader")

#word display
word_label = tk.Label(root, font=('Helvetica', 36))
word_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky='ew')
is_running = False

input_text = tk.Text(root, height=10, width=50)
input_text.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

def submit_text():
    global words, current_index
    input_string = input_text.get("1.0", "end-1c")  #pull text from submit
    words = input_string.split()
    current_index = 0  #reset index
    if not is_running:
        toggle_start_pause()

submit_button = tk.Button(root, text="Submit", command=submit_text)
submit_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='ew')

def display_words(words):
    global current_index, is_running
    if current_index < len(words) and is_running:
        word_label.config(text=words[current_index])
        current_index += 1
        delay = speed_scale.get()  #pull delay from scale
        root.after(delay, display_words, words)

def toggle_start_pause():
    global is_running
    if is_running:
        is_running = False
    else:
        is_running = True
        display_words(words)

playButton = tk.Button(root, text="Start/Pause", command=toggle_start_pause)
playButton.grid(row=2, column=2, columnspan=1, pady=10, padx=10, sticky='ew')

speed_scale = tk.Scale(root, from_=25, to=450, orient='horizontal', label='Speed (ms)')
speed_scale.set(300)
speed_scale.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

dark_mode_button = tk.Button(root, text="Dark Mode", command=dark_mode_toggle)
dark_mode_button.grid(row=2, column=1, columnspan=1, pady=10, padx=10, sticky='ew')

#config update --dark toggle
def update_colors():
    global update_colors
    word_label.config(fg=widget_fg, bg=widget_bg)
    input_text.config(fg=widget_fg, bg=widget_bg)
    submit_button.config(fg=widget_fg, bg=widget_bg)
    playButton.config(fg=widget_fg, bg=widget_bg)
    speed_scale.config(fg=widget_fg, bg=widget_bg)
    dark_mode_button.config(fg=widget_fg, bg=widget_bg)
    root.config(bg=window_bg)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.mainloop()
