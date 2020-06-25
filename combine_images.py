from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Image combinator")


def main():
    file_frame()
    list_frame()
    path_frame()
    option_frame()
    run_frame()

    root.resizable(False, False)
    root.mainloop()


def file_frame():
    file_frame = Frame(root)
    file_frame.pack(fill="x")

    btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File")
    btn_add_file.pack(side="left")
    btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File")
    btn_del_file.pack(side="right")


def list_frame():
    list_frame = Frame(root)
    list_frame.pack(fill="both")

    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side="right", fill='y')

    list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
    list_file.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=list_file.yview)


def path_frame():
    path_frame = LabelFrame(root, text="Save to")
    path_frame.pack(fill="x")

    txt_destination_path = Entry(path_frame)
    txt_destination_path.pack(side="left", fill="x", expand=True, ipady=4)

    btn_destination_path = Button(path_frame, text="Find", width=10)
    btn_destination_path.pack(side="right")


def option_frame():
    frame_option = LabelFrame(root, text="Option")
    frame_option.pack()

    # Width option
    label_width = Label(frame_option, text="Width", width=8)
    label_width.pack(side="left")

    # Width combo
    option_width = ["Original", "1024", "800", "640"]
    cmb_width = ttk.Combobox(frame_option, state="readonly", values=option_width, width=10)
    cmb_width.current(0)
    cmb_width.pack(side="left")

    # label space
    label_spacing = Label(frame_option, text="Spacing", width=8)
    label_spacing.pack(side="left")

    # label combo
    option_spacing = ["None", "Narrow", "Normal", "Wide"]
    cmb_spacing = ttk.Combobox(frame_option, state="readonly", values=option_spacing, width=10)
    cmb_spacing.current(0)
    cmb_spacing.pack(side="left")

    # File format
    label_format = Label(frame_option, text="Format", width=8)
    label_format.pack(side="left")

    # format combo
    option_spacing = ["PNG", "JPG", "BMP"]
    cmb_format = ttk.Combobox(frame_option, state="readonly", values=option_spacing, width=10)
    cmb_format.current(0)
    cmb_format.pack(side="left")

    # progress bar
    frame_progress = LabelFrame(root, text="Progress")
    frame_progress.pack(fill="x")

    p_var = DoubleVar()
    progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
    progress_bar.pack(fill="x")


def run_frame():
    frame_run = Frame(root)
    frame_run.pack(fill="x")

    btn_close = Button(frame_run, padx=5, pady=5, text="Quit", width=12, command=root.quit)
    btn_close.pack(side="right")

    btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
    btn_start.pack(side="right")


if __name__ == "__main__":
    main()
