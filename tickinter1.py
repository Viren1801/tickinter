import os
from tkinter import *
import shutil


#def file_source_counter():
#    global dir_path
#    count = len([item for item in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, item))])
#    myText.set(count)
    
def file_transfer():
    dir_path = e1.get()
    dir_path2 = e2.get()
    
    for file in os.listdir(dir_path):
        if file in os.listdir(dir_path2):
            print(file+"exists")
        elif file not in os.listdir(dir_path2):
            full_file_name = os.path.join(dir_path, file)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dir_path2)
        else:
            break
        
        
master = Tk()
myText=StringVar()

Label(master, text="Enter Source Directory Name").grid(row=0, sticky=W)
Label(master, text="Enter Destination Directory").grid(row=2, sticky=W)
Label(master, text="Result:").grid(row=4, sticky=W)

#result=Label(master, text="",textvariable=myText).grid(row=4,column=1, sticky=W)


e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=2, column=1)

#source_get = Button(master, text="Enter", command=file_source_counter).grid(row=0, column=2,sticky=W+E+N+S, pady=4)
#source_quit = Button(master, text="Quit", command=master.quit).grid(row=0, column=6,sticky=W+E+N+S, pady=4)
#destination_get = Button(master, text="Enter", command=file_source_counter).grid(row=2, column=2,sticky=W+E+N+S, pady=4)
#destination_quit = Button(master, text="Quit", command=master.quit).grid(row=2, column=6,sticky=W+E+N+S, pady=4)

Transfer = Button(master, text="Copy", command=file_transfer).grid(row=4,column=2,sticky=W+E+N+S, pady=4)

mainloop()