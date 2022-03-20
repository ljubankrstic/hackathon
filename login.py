import tkinter as tk
import pandas as pd
import sys
import subprocess
#from newWin.py import newWin
#creating the main window
root=tk.Tk()

#reading the csv data(we messed around with mongo db but unfortunately it didnt work
employee_login_data=pd.read_csv("employee_data.csv")
#configuring grid layout
root.rowconfigure([0,1,2,3,4],weight=1)

#creating the label widgets
username_label=tk.Label(root,text="Username")
password_label=tk.Label(root,text="password")

#function to check if username and password match with according data

#creating the entry widgets
username=tk.Entry(root)
password=tk.Entry(root)

def check():
	name=username.get()
	passwd=password.get()
	for row in employee_login_data:
		print(row)
		if row["username"]==name:
			if row["password"]==passwd:
				subprocess.run(['python3','newwin.py'])
		
#creating the submit button
button=tk.Button(root,text="Submit",command=check)


#putting widgets in window
username_label.grid(row=0,column=0)
username.grid(row=1,column=0)
password_label.grid(row=2,column=0)
password.grid(row=3,column=0)
button.grid(row=4,column=0)

root.mainloop()
