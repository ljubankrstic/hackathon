import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib



task_data=pd.read_csv('task_data.csv')
random_entry=task_data.sample(n=100)

#we are importing various matplotlib modules to plot our data
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

#creating and customizing
root=tk.Tk()
root.geometry("1000x650")

#dividing the root
sidebar=tk.Frame(root,width=300,bg="#2f2e2e")
MAPP_title=tk.Label(sidebar,text="MAPP",font=("Roboto",60),fg="white",bg="#2f2e2e")





subframe=tk.Frame(root,bg="white")
x=list(range(10))
y=[i**2 for i in x]
figure=Figure(figsize=(6, 4), dpi=100)
figure.add_subplot(111).scatter()
figure_canvas=FigureCanvasTkAgg(figure,subframe)
figure_canvas.draw()
  
# placing the canvas on the Tkinter window
figure_canvas.get_tk_widget().pack()
#customizing the main grid
root.columnconfigure(0,minsize=300,weight=0)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
sidebar.grid(column=0,row=0,sticky="nswe")
subframe.grid(column=1,row=0,sticky="nswe")
MAPP_title.grid(row=0,column=0,sticky="wsne")




root.mainloop()
