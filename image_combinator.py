import os
import threading
import time
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from PIL import Image, ImageGrab


def add_file():
    files = filedialog.askopenfilenames(title="Select the image file(s)",
                                        filetypes=[("png", "*.png"), ("Any", "*.*")], \
                                        initialdir="C:/Users/heetaeyang/Documents")
    for file in files:
        list_file.insert(END, file)


def del_file():
    for i in reversed(list_file.curselection()):
        list_file.delete(i)


def browse_path():
    selected_folder = filedialog.askdirectory()
    if selected_folder == '':
        return
    txt_destination_path.delete(0, END)
    txt_destination_path.insert(0, selected_folder)


def merge_images():
    try:
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1
        else:
            img_width = int(img_width)

        # ["None", "Narrow", "Normal", "Wide"]
        img_space = cmb_spacing.get()
        if img_space == "Narrow":
            img_space = 10
        elif img_space == "Normal":
            img_space = 30
        elif img_space == "Wide":
            img_space = 60
        else:
            img_space = 0

        # ["PNG", "JPG", "BMP"]
        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]
        # [(width1, height1), (width2, height2), ...]
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))
        # set the widths and heights value depending on added pictures
        max_widths, total_heights = max(widths), sum(heights)

        # final image output
        if img_space > 0:
            total_heights + (img_space * (len(images) - 1))
        final_img = Image.new("RGB", (max_widths, total_heights), (255, 255, 255))
        y_offset = 0

        # Sets the progress bar reflecting the task completion
        for idx, img in enumerate(images):
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            final_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)  # height value + user selected space option

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        file_name = "image_comb." + img_format
        dest_path = os.path.join(txt_destination_path.get(), file_name)
        final_img.save(dest_path)
        msgbox.showinfo("Alert", "Task Completed")
    except Exception as err:
        msgbox.showerror("Error", err)


def start():
    if list_file.size() < 2:
        msgbox.showwarning("Warning", "Minimum 2 files are required to start the process")
        return

    if len(txt_destination_path.get()) == 0:
        msgbox.showwarning("Warning", "Select your save directory")
        return

    # combine images
    merge_images()


def screenshot():
    time.sleep(5)
    print("Starting now.")
    for i in range(1, 11):
        img = ImageGrab.grab()
        img.save("image{}.png".format(i))
        print("img" + str(i) + " complete.")
        time.sleep(2)
    msgbox.showinfo("Alert", "Screenshot Completed")


# Threading to avoid GUI hanging while screenshot capturing is running
def start_screenshot():
    t1 = threading.Thread(target=screenshot)
    t1.start()


root = Tk()
root.title("Image combinator")

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File", command=del_file)
btn_del_file.pack(side="right")

list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill='y')

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

path_frame = LabelFrame(root, text="Save To")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_destination_path = Entry(path_frame)
txt_destination_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_destination_path = Button(path_frame, text="Find", width=10, command=browse_path)
btn_destination_path.pack(side="right", padx=5, pady=5)

frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# Width option
label_width = Label(frame_option, text="Width", width=8)
label_width.pack(side="left", padx=5, pady=5)

# Width combo
option_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=option_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# label space
label_spacing = Label(frame_option, text="Spacing", width=8)
label_spacing.pack(side="left", padx=5, pady=5)

# label combo
option_spacing = ["None", "Narrow", "Normal", "Wide"]
cmb_spacing = ttk.Combobox(frame_option, state="readonly", values=option_spacing, width=10)
cmb_spacing.current(0)
cmb_spacing.pack(side="left", padx=5, pady=5)

# File format
label_format = Label(frame_option, text="Format", width=8)
label_format.pack(side="left", padx=5, pady=5)

# format combo
option_spacing = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=option_spacing, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_screenshot = Button(frame_run, padx=5, pady=5, text="Take Screenshot", width=12,
                        command=start_screenshot)
btn_screenshot.pack(side="left", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Quit", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
