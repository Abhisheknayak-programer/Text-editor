import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog

main_application=tk.Tk()
main_application.geometry("800x400")
main_application.title("text editor".upper())
main_application.wm_iconbitmap("icon.ico")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#################################################### main menu #############################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


main_menu=tk.Menu(main_application)

#--------------------------------file--------------------------------------------------------
# -----------------------------icons of file--------------------------------------------------- 
new_icon=tk.PhotoImage(file="icons2/new.png")
open_icon=tk.PhotoImage(file="icons2/open.png")
save_icon=tk.PhotoImage(file="icons2/save.png")
save_as_icon=tk.PhotoImage(file="icons2/save_as.png")
exit_icon=tk.PhotoImage(file="icons2/exit.png")


file = tk.Menu(main_menu,tearoff=False)

#-----------------------------------edit--------------------------------------------------------------
#-----------------------------------edit icons--------------------------------------------------------


copy_icon=tk.PhotoImage(file="icons2/copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

#------------------------------------------edit labels------------------------------------------------
edit= tk.Menu(main_menu,tearoff=False)

#---------------------------------view------------------------------------------------------------------
#---------------------------------view icons-------------------------------------------------------------
tool_bar_icon=tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons2/status_bar.png")

view = tk.Menu(main_menu,tearoff=False)


#------------------------------colour theme-------------------------------------------------------------------
#------------------------------colour theme icon---------------------------------------------------------------
light_default_icon=tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons2/light_plus.png")
dark_icon=tk.PhotoImage(file="icons2/dark.png")
red_icon=tk.PhotoImage(file="icons2/red.png")
monokai_icon=tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file="icons2/night_blue.png")

#======================================= label colour theme=============================================

colour_theme = tk.Menu(main_menu,tearoff=False)

theme_choice=tk.StringVar()

colour_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

colour_dict={
    "light default".upper():("#000000","#ffffff"),
    "light plus".upper():("#474747","#e0e0e0"),
    "dark".upper():("#c4c4c4","#2d2d2d"),
    "red".upper():("#2d2d2d","#ffe8e8"),
    "monokai".upper():("#d3b774","#474747"),
    "light blue".upper():("#ededed","#6b9dc2")
}


#####################################################  cascade  #######( for the declaration of the name in win)
main_menu.add_cascade(label="FILE",menu=file)
main_menu.add_cascade(label="EDIT",menu=edit)
main_menu.add_cascade(label="VIEW",menu=view)
main_menu.add_cascade(label="COLOUR THEME",menu=colour_theme)


# --------------------------------------------------end menu-----------------------------------------------# 




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#################################################### tool bar #############################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



tool_bar=ttk.Label(main_application)            # label of tool bar
tool_bar.pack(side=tk.TOP,fill=tk.X)            # packing of toolbar from side top and fiiling from x == left


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         font box  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

font_tuple=tk.font.families()               # tk.font.familes() contains all the designed type of fonts

font_family=tk.StringVar()             

font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box['values']=font_tuple   
font_box.grid(row=0, column=0,padx=5)

font_box.current(font_tuple.index("System"))    # for creating a current data inside the combobox

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    size box @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


size_var=tk.StringVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")

font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  bold button @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

bold_icons=tk.PhotoImage(file="icons2/bold.png")

bold_button=tk.Button(tool_bar,image=bold_icons)
bold_button.grid(row=0,column=2,padx=5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ italic button @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
italic_icons=tk.PhotoImage(file="icons2/italic.png")

italic_button=tk.Button(tool_bar,image=italic_icons)
italic_button.grid(row=0,column=3,padx=5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ underline button @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

underline_icons=tk.PhotoImage(file="icons2/underline.png")

underline_button=tk.Button(tool_bar,image=underline_icons)
underline_button.grid(row=0,column=4,padx=5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ font colour buttons @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

font_colour_icon=tk.PhotoImage(file="icons2/font_color.png")

font_colour_button=ttk.Button(tool_bar,image=font_colour_icon)
font_colour_button.grid(row=0,column=5,padx=5)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ align left @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
align_left_icon=tk.PhotoImage(file="icons2/align_left.png")
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ align center @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
align_center_icon=tk.PhotoImage(file="icons2/align_center.png")
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ align right @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
align_right_icon=tk.PhotoImage(file="icons2/align_right.png")
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5)



# -------------------------------------------------end tool bar-----------------------------------------------# 
#################################################### text  editor #############################################
text_editor=tk.Text(main_application)                              # text() contains the text inside it
text_editor.config(wrap="word",relief=tk.FLAT)                    ## wrap="word" means word will be inputed in it
##                                                               ### relief=tk.FLAT means the way it will go or typed


scroll_bar=tk.Scrollbar(main_application)                       ####  scroll bar making

text_editor.focus_set()                                          # it means a line will occur 


scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)                        ## packing it toward the right side and filling it in y axis
text_editor.pack(fill=tk.BOTH,expand=True)                      # packing it towared both means up and down and toward each and every side 


scroll_bar.config(command=text_editor.yview)                    # necessaray for scroll bar
text_editor.config(yscrollcommand=scroll_bar.set)               # necessary for the montion between them

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> font family and font size functionality >>>>>>>>>>>>>>>>>>>>>>>>>
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

current_font_family="Arial"
current_font_size=12

text_editor.configure(font=("Arial",12))

def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)


def change_fontsize(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_fontsize)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< buttons functionality <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#......................................... bold button functionality .....................................


def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == "normal":
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()['weight'] == "bold":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    
bold_button.configure(command=change_bold)

#.................................... italic button functonality ...........................................


def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == "roman":
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()['slant'] == "italic":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    
italic_button.configure(command=change_italic)

#............................................underline button functionality ....................................

def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
    
underline_button.configure(command=change_underline)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>change font colour functionality >>>>>>>>>>>>>>>>>>>>>>>>>>
def change_font_colour():
    colour_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_var[1])

font_colour_button.configure(command=change_font_colour)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> align functionality>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#### align left

def align_left():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=align_left)


#### align center

def align_center():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"center")
align_center_button.configure(command=align_center)



### align right


def align_right():
    text_content=text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,"right")
align_right_button.configure(command=align_right)





# --------------------------------------------------end text editor-----------------------------------------------# 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#################################################### main status bar #############################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

status_bar=ttk.Label(main_application,text="status bar".upper())
status_bar.pack(side=tk.BOTTOM)

#///////////////////////////////////////////////// status bar functionality ////////////////////////////////////


text_changed=False
def change(event=None):                                  # for the counting of the no.s of word and charecters
    global text_changed
    if text_editor.edit_modified():
        words=len(text_editor.get(1.0,"end-1c").split())        
        charecters=len(text_editor.get(1.0,"end-1c"))
        status_bar.config(text=f"CHARACTERS : {charecters} , WORDS : {words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# --------------------------------------------------end  status bar-----------------------------------------------# 
#################################################### main menu functionality #############################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


####################variable
url=""


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> new functionality >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def new_file(event=None):
    global url
    url=""
    text_editor.delete(1.0,tk.END)

#>>>>>>>>>>>>>>>>>>>>>>>>>>> open  a file functionality >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> saving file functionality>>>>>>>>>>>>>>>>>>>>>>>>>

def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,"w",encoding="utf-8") as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode="w",defaultextension=".txt", filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>save as functionality<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode="w",defaultextension=".txt", filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> exit functionality   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> find functionality >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
#--------------------------------------file labels------------------------------------------#

file.add_command(label="OPEN",image=open_icon,compound=tk.LEFT,accelerator='ctrl+O'.upper(),command=open_file)
file.add_command(label="NEW",image=new_icon,compound=tk.LEFT,accelerator='ctrl+N'.upper(),command=new_file)
file.add_command(label="SAVE",image=save_icon,compound=tk.LEFT,accelerator='ctrl+S'.upper(),command=save_file)
file.add_command(label="SAVE AS",image=save_as_icon,compound=tk.LEFT,accelerator='ctrl+ALT+S'.upper(),command=save_as)
file.add_command(label="EXIT",image=exit_icon,compound=tk.LEFT,accelerator='ctrl+Q'.upper(),command=exit_func)




#------------------------------------------edit labels------------------------------------------------

edit.add_command(label="COPY",image=copy_icon,compound=tk.LEFT,accelerator="ctrl+C".upper(),command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="PASTE",image=paste_icon,compound=tk.LEFT,accelerator="ctrl+V".upper(),command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="CUT",image=cut_icon,compound=tk.LEFT,accelerator="ctrl+x".upper(),command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="CLEAR ALL",image=clear_all_icon,compound=tk.LEFT,accelerator="ctrl+ALT+X".upper(),command=lambda:text_editor.delete(1.0 , tk.END))
edit.add_command(label="FIND",image=find_icon,compound=tk.LEFT,accelerator="ctrl+F".upper(),command=find_func)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#--------------------------------view labels-----------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> hide tool bar functionality >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False 
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> hide status bar functionality >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 



view.add_checkbutton(label="TOOL BAR",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label="STATUS BAR",onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#-------------------------------colour theme labels--------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





def change_theme():
    chosen_theme=theme_choice.get()
    colour_tuple =colour_dict.get(chosen_theme)
    fg_color ,bg_colour = colour_tuple[0],colour_tuple[1]
    text_editor.config(background=bg_colour,foreground=fg_color)


count=0
for i in colour_dict:
    colour_theme.add_radiobutton(label=i,image=colour_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count=count+1




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# --------------------------------------------------end menu  functionality-----------------------------------------------# 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#### bind shortcut keys 
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)



main_application.config(menu=main_menu)
main_application.mainloop()