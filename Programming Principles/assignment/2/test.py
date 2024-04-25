
import tkinter as tk 
   
# initialize a tkinter window 
root = tk.Tk() 
  
# Creating the geometry with width and height of 300px 
root.geometry("300x300") 
  
# create a button 
btn = tk.Button(root, text ="I am button") 
btn.pack() 
  
# text widget 
txt = tk.Entry(root, width=10) 
txt.pack() 
  
# create a radio button 
rb = tk.Radiobutton(root, text ="I am radio button")  
rb.pack()  
  
# create a check button 
cb = tk.Checkbutton(root, text = "I am check button") 
cb.pack() 
  
  
root.mainloop()