# LIBS
from tkinter import messagebox
from tkinter.constants import RIGHT
import interface as iface
import checker
import os, sys
sys.path.append('..')
from pyodm import Node

# CONST
LEFT = '<Button-1>'

def get_files(dir):
    print(dir)
    for address, dirs, files in os.walk(dir):
        return files

def odm_start(files):
    n = Node('localhost', 3000)
    task = n.create_task(
        files, 
        {
            'build-overviews':iface.bo_v.get(),
            'dem-resolution':float(iface.dr_v.get()),
            'dsm':iface.dsm_v.get(),
            'dtm':iface.dtm_v.get(),
            'fast-orthophoto':iface.fo_v.get(),
            'feature-quality':iface.fq_f.get(),
            'max-concurrency':int(iface.mc_v.get()),
            'name':iface.name_v.get(),
            'skip-3dmodel':iface.s3d_v.get()
        },
    )
    task.wait_for_completion()
    task.download_assets(iface.output_folder.get())


def start_clicked(event):
    try:
        path = iface.input_folder.get()
        files = get_files(path)
        files = [path + '/' + file for file in files]
        valid, not_valid = checker.check(files)
        if len(not_valid) != 0:
            messagebox.showwarning('No data', '\n'.join(not_valid))
        odm_start(valid)

    except Exception as e:
        messagebox.showerror('Error', str(e))



# MAIN
def main():
    iface.prepare()
    iface.start_button.bind(LEFT, start_clicked)
    iface.loop()

if __name__ == '__main__':
    main()