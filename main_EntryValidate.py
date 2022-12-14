"""This Script is used for testing Tkinter Entry object extension custom widget."""

import tkinter as tk
from tkinter import ttk
import clsStatusBar as status_bar
import clsValidateData as validate
import wgtEntryWithEvents as myWidgetEntryWithEvents 

root = tk.Tk()
root.geometry("400x400")

# first always create the status bar
sbar = status_bar.status_bar_obj(root,default_text= "Ready",text="Loading...")
val = validate.validate(statusBarObj= sbar)

""" Initial an implementation of ttk.Entry with Events, Validation and Formatting """
EntryWithEvents = myWidgetEntryWithEvents.EntryWithEvents

        
entry_date = EntryWithEvents(master= root, max_len = 11, widget_name = 'entry_date', 
                             validation_method = val.validate_Date,
                             set_justifiction = tk.LEFT,
                             tool_tip = 'Enter a date or a date shortcut!')
entry_date.pack(expand=True)


entry_details = EntryWithEvents(master=root, max_len = 11, widget_name = 'entry_detail', 
                                validation_method = val.validate_Date)
entry_details.pack(expand=True)


entry_float = EntryWithEvents(master=root, max_len = 15, widget_name = 'entry_float', 
                              validation_method = val.validate_float)
entry_float.pack(expand=True)


entry_decimal = EntryWithEvents(master=root, max_len = 15, widget_name = 'entry_decimal', 
                              validation_method = val.validate_decimal)
entry_decimal.pack(expand=True)


entry_integer = EntryWithEvents(master=root, max_len = 15, widget_name = 'entry_integer', 
                              validation_method = val.validate_integer)
entry_integer.pack(expand=True)


entry_title = EntryWithEvents(master=root, widget_name = 'entry_title', 
                              validation_method = val.validate_title)
entry_title.pack(expand=True)


entry_sentence = EntryWithEvents(master=root, widget_name = 'entry_sentence', 
                              validation_method = val.validate_sentence)
entry_sentence.pack(expand=True)

# set focus to the field we want.
root.after(1, lambda: entry_date.focus_set())

sbar.update()

root.title("Testing") # My Widget - Entry With Events")
root.mainloop()