#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Mar 07, 2020 03:52:37 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global He_radio,Endodontics, Periodont, Orthodontics, Surgery, Pedodont, Oralpatho, Public_Health, Oral_Mea, Prostho

    He_radio = tk.IntVar(None, 0)
    Endodontics = tk.IntVar(None, 0)
    Periodont = tk.IntVar(None, 0)
    Orthodontics = tk.IntVar(None, 0)
    Surgery = tk.IntVar(None, 0)
    Pedodont = tk.IntVar(None, 0)
    Oralpatho = tk.IntVar(None, 0)
    Public_Health = tk.IntVar(None, 0)
    Oral_Mea = tk.IntVar(None, 0)
    Prostho = tk.IntVar(None, 0)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top



def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import department_single_window
    department_single_window.vp_start_gui()




