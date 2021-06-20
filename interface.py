# LIBS
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# GLOBALS
window: Tk
input_folder: StringVar
output_folder: StringVar

bo_v: BooleanVar
dr_v: StringVar
dsm_v: BooleanVar
dtm_v: BooleanVar
fo_v: BooleanVar
mc_v: StringVar
name_v: StringVar
s3d_v: StringVar

fq_f: ttk.Combobox
start_button: Button

pgb: ttk.Progressbar
pgv: DoubleVar

# FUNCTIONS
def init():
    global window
    window = Tk()

def set_geometry():
    global window
    window.title('odmDesktop')
    window.iconbitmap(default='assets/icon.ico')
    window.geometry('450x250')
    window.minsize(450, 250)
    window.maxsize(450, 250)

def init_globals():
    global input_folder
    global output_folder
    input_folder, output_folder = StringVar(), StringVar()

    global bo_v
    global dr_v
    global dsm_v
    global dtm_v
    global fo_v
    global mc_v
    global name_v
    global s3d_v

    bo_v = BooleanVar(False)
    dr_v = StringVar()
    dr_v.set('5')
    dsm_v = BooleanVar(False)
    dtm_v = BooleanVar(False)
    fo_v = BooleanVar(False)
    mc_v = StringVar()
    mc_v.set('4')
    name_v = StringVar()
    name_v.set('code')
    s3d_v = BooleanVar(False)

def set_modules():
    global window
    global input_folder
    global output_folder
    global bo_v
    global dr_v
    global dsm_v
    global dtm_v
    global fo_v
    global mc_v
    global name_v
    global s3d_v
    global fq_f
    global start_button
    global pgb
    global pgv
    # TABS 
    tab_control = ttk.Notebook(window) # container
    tab_main = ttk.Frame(tab_control) # main tab
    tab_control.add(tab_main, text='Main')
    tab_settings = ttk.Frame(tab_control) # settings tab
    tab_control.add(tab_settings, text='Settings')
    tab_control.pack(expand=True, fill='both')

    # MAIN TAB
    input_frame = ttk.Frame(tab_main, width=400)
    input_frame.pack()
    # input folder
    if_label = ttk.Label(input_frame, text="Input folder") # if - input_folder
    if_label.grid(row=0, column=0, padx=5, pady=15)
    if_entry = Entry(input_frame, width=30, textvariable=input_folder)
    if_entry.grid(row=0, column=1, padx=5, pady=15)
    if_button = Button(input_frame, text='Choose folder', command=set_if)
    if_button.grid(row=0, column=2, padx=5, pady=15)
    # output folder
    of_label = ttk.Label(input_frame, text="Output folder") # of - output_folder
    of_label.grid(row=1, column=0, padx=5, pady=0)
    of_entry = Entry(input_frame, width=30, textvariable=output_folder)
    of_entry.grid(row=1, column=1, padx=5, pady=0)
    of_button = Button(input_frame, text='Choose folder', command=set_of)
    of_button.grid(row=1, column=2, padx=5, pady=0)
    # button
    control_frame = ttk.Frame(tab_main, width=400)
    control_frame.pack()
    start_button = Button(control_frame, text='Start', width=15)
    start_button.grid(row=0, column=0, padx=25, pady=35)
    
    pgv = DoubleVar()

    pgb = ttk.Progressbar(control_frame, variable=pgv,
                          orient=HORIZONTAL, length=400, mode = 'determinate')
    pgb.grid(row=1, column=0, padx=0, pady=0)
     
    # SETTINGS TAB
    settings_frame = ttk.Frame(tab_settings, width=400)
    settings_frame.pack()
    # --build-overviews || bo_v
    bo_l = ttk.Label(settings_frame, text='--build-overviews') 
    bo_l.grid(row=0, column=0, pady=3)
    bo_f = ttk.Checkbutton(settings_frame, variable=bo_v)
    bo_f.grid(row=0, column=1, pady=3)
    # --dem-resolution || dr_v
    demr_l = ttk.Label(settings_frame, text='--dem-resolution') 
    demr_l.grid(row=1, column=0)
    demr_f = Entry(settings_frame, width=6, textvariable=dr_v)
    demr_f.grid(row=1, column=1)
    # --dsm || dsm_v
    dsm_l = ttk.Label(settings_frame, text='--dsm') 
    dsm_l.grid(row=2, column=0, pady=3)
    dsm_f = ttk.Checkbutton(settings_frame, variable=dsm_v)
    dsm_f.grid(row=2, column=1, pady=3)
    # --dtm || dtm_v
    dtm_l = ttk.Label(settings_frame, text='--dtm') 
    dtm_l.grid(row=3, column=0)
    dtl_f = ttk.Checkbutton(settings_frame, variable=dtm_v)
    dtl_f.grid(row=3, column=1)
    # --fast-orthophoto || fo_v
    fo_l = ttk.Label(settings_frame, text='--fast-orthophoto') 
    fo_l.grid(row=4, column=0, pady=3)
    fo_f = ttk.Checkbutton(settings_frame, variable=fo_v)
    fo_f.grid(row=4, column=1, pady=3)
    # --feature-quality || NO_VARIABLE
    fq_l = ttk.Label(settings_frame, text='--feature-quality') 
    fq_l.grid(row=5, column=0)
    fq_f = ttk.Combobox(settings_frame, width=10)
    fq_f['values'] = ('ultra', 'high', 'medium', 'low', 'lowest')
    fq_f.current(1)
    fq_f.grid(row=5, column=1)
    # --max-concurrency || mc_v
    mc_l = ttk.Label(settings_frame, text='--max-concurrency') 
    mc_l.grid(row=6, column=0, pady=3)
    mc_f = Entry(settings_frame, width=6, textvariable=mc_v)
    mc_f.grid(row=6, column=1, pady=3)
    # --name || name_v
    name_l = ttk.Label(settings_frame, text='--name') 
    name_l.grid(row=7, column=0)
    demr_f = Entry(settings_frame, width=6, textvariable=name_v)
    demr_f.grid(row=7, column=1)
    # --skip-3dmodel || s3d_v
    s3d_l = ttk.Label(settings_frame, text='--skip-3dmodel') 
    s3d_l.grid(row=8, column=0, pady=3)
    s3d_f = ttk.Checkbutton(settings_frame, variable=s3d_v)
    s3d_f.grid(row=8, column=1, pady=3)

def loop():
    global window
    window.mainloop()

def prepare():
    init()
    set_geometry()
    init_globals()
    set_modules()

def set_if():
    global input_folder
    input_folder.set(filedialog.askdirectory())

def set_of():
    global output_folder
    output_folder.set(filedialog.askdirectory())
