import tkinter as tk
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def show_entry_fields():
    future = producer.send('test', str.encode(e1.get()))
    result = future.get(timeout=60)

master = tk.Tk()

tk.Label(master, 
         text="Enter Number").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)


tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()


