import http.client
import json
from tkinter import *
import sys
import os
from tkinter import Tk,Button
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
root = Tk()
root.title("Сovid")
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
coron = data.decode("utf-8")
json = json.loads(coron)
text = Text(width=500, height=500, fg='#0000FF', bg='#90EE90', font=("Times New Romans", 17, "italic"))
text.pack()
for i in range(10):
    text.insert('1.0', list(json[i].items())[14])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[12])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[10])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[2])
    text.insert('1.0', '\n')
Button(root, text="Перезапуск", font=("Times New Romans", 10, "italic"), command=restart_program, fg='#ffffff', bg='#CD5C5C',width=24, height=1,).place(x = 0, y = 0)
root.mainloop()