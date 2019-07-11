from tkinter import *
from tkinter import filedialog
import subprocess

window = Tk()
window.title('ChinaUnicom-APP')
window.geometry('450x300')
dir_config_path = 'D:\QYT-PythonLearning\App\Config_backup'
dir_device_path = 'D:\QYT-PythonLearning\App'

def open_folder(dir):
    # Launch a subprocess to execute the windows command to open a folder in explorer
    # subprocess.Popen(r'explorer /select,"{0}"'.format(dir)) # This command cannot open the last folder, use the method below
    subprocess.Popen(r'explorer.exe "{0}"'.format(dir))

label_device_info = Label(window, text='Device Login Information:', bg='grey', font=('Times New Roman',12) )
label_device_info.place(x=20, y=30, width=170, height=25)

label_backup_action = Label(window, text='Config Backup:', bg='green', font=('Times New Roman',12) )
label_backup_action.place(x=20, y=90, width=170, height=25)

btn_device_open_folder = Button(window, text = 'Open Device Folder', width = 35, height = 2, command=lambda: open_folder(dir_device_path))
btn_device_open_folder.place(x=250, y=30, width=120, height=25)

btn_config_open_folder = Button(window, text = 'Open Config Folder', width = 35, height = 2, command=lambda: open_folder(dir_config_path))
btn_config_open_folder.place(x=250, y=90, width=120, height=25)

btn_backup_config = Button(window, text = 'Backup Now!', width = 35, height = 2, command=backup_config)
btn_backup_config.place(x=250, y=120, width=60, height=25)


window.mainloop()


