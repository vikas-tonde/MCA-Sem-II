from tkinter import*
from tkinter import messagebox
import re
import os


def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno == "":
        return True
    else:
        messagebox.showinfo(
            'Information', 'Only digits are allowed for phoneno')
        return False


def isValidEmail(user_email):
    if len(user_email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", user_email) != None:
            return True
    else:
        messagebox.showinfo('Information', 'This is not valid email address')
        return False


def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo('Information', 'Please Enter FullName To Proceed')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information', 'Please Enter Password To Proceed')
    elif v_confirmPwd.get() == "":
        messagebox.showinfo(
            'information', 'Please Confirm password to proceed')
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information', 'please eneter phone no to proceed')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information', 'please enter Email Id to procees')
    elif v_gender.get() == 0:
        messagebox.showinfo('Information', 'please select gender to procees')
    elif v_country.get() == 0:
        messagebox.showinfo('Information', 'please select country to procees')
    elif v_skills.get() == 0:
        messagebox.showinfo('Information', 'please select course to procees')
    elif v_pwd.get() != v_confirmPwd.get():
        messagebox.showinfo('Information', 'password missmatch')
    elif v_emailId.get() != "":
        status = isValidEmail(v_emailId.get())
    if (status):
        messagebox.showinfo('Information', 'User Register succsessfully')
    else:
        messagebox.showinfo('Information', 'User Register succsessfully')


def clearAllFields():
    v_fName.set("")
    v_pwd.set("")
    v_confirmPwd("")
    v_phoneNo.set("")
    v_emailId.set("")
    v_skills.set("")


def callNewScreen():
    window.destroy()
    os.system('python LoginScreen.py')


window = Tk()
window.title("Welcome to user registration screen")
window.geometry('500x500')
window.configure(background="#4567fa")
v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_country = StringVar()
v_gender = IntVar()
v_skills = StringVar()

# heading
lb_heading = Label(window, text="Registration", width=20,
                   font=("bold", 20), bg="light blue")
lb_heading.place(x=90, y=53)
# name
lb_fullname = Label(window, text="FullName", width=20,
                    font=("bold", 10), bg="light blue")
lb_fullname.place(x=80, y=130)
entry_fullname = Entry(window, textvariable=v_fName)
entry_fullname.place(x=250, y=130)
# password
lb_pwd = Label(window, text="Password", width=20,
               font=("bold", 10), bg="light blue")
lb_pwd.place(x=80, y=170)
entry_pwd = Entry(window, show="*", textvariable=v_pwd)
entry_pwd.place(x=250, y=170)
# confirm
lb_confirm_pwd = Label(window, text="Confirm Password",
                       width=20, font=("bold", 10), bg="light blue")
lb_confirm_pwd.place(x=80, y=210)
entry_confirm_pwd = Entry(window, show="*", textvariable=v_confirmPwd)
entry_confirm_pwd.place(x=250, y=210)
# phoneno
lb_phoneno = Label(window, text="Phone No", width=20,
                   font=("bold", 10), bg="light blue")
lb_phoneno.place(x=80, y=250)
entry_phoneno = Entry(window, textvariable=v_phoneNo)
entry_phoneno.place(x=250, y=250)
# validation
valid_phoneno = window.register(validate_phoneno)
entry_phoneno.config(validate="key", validatecommand=(valid_phoneno, '%p'))
# email
lb_email = Label(window, text="Email", width=20,
                 font=("bold", 10), bg="light blue")
lb_email.place(x=80, y=290)
entry_email = Entry(window, textvariable=v_emailId)
entry_email.place(x=250, y=290)
# gender
lb_gender = Label(window, text="Gender", width=20,
                  font=("bold", 10), bg="light blue")
lb_gender.place(x=80, y=330)
Radiobutton(window, text="Male", bg="white", padx=5,
            variable=v_gender, value=1).place(x=250, y=330)
Radiobutton(window, text="Female", bg="white", padx=20,
            variable=v_gender, value=2).place(x=300, y=330)
# country
lb_country = Label(window, text="Country", width=20,
                   font=("bold", 10), bg="light blue")
lb_country.place(x=80, y=370)
list_country = {'India', 'Canada', 'UK', 'Nepal', 'Germany'}
droplist = OptionMenu(window, v_country, *list_country)
droplist.config(width=16, bg="white")
v_country.set('select country')
droplist.place(x=250, y=365)
lb_skills = Label(window, text="skills", width=20,
                  font=("bold", 10), bg="light blue")
lb_skills.place(x=80, y=410)

list_skills = {'python', 'java', 'JS', 'CSS', 'Bootstrap', 'C', 'C++', 'HTML'}
droplist = OptionMenu(window, v_skills, *list_skills)
droplist.config(width=16, bg="white")
v_skills.set('select skills')
droplist.place(x=250, y=405)
btn_register = Button(window, text="Register", command=validateAllFields,
                      bg="green", fg="white", font=("bold", 10)).place(x=150, y=450)
btn_clear = Button(window, text="Clear", command=clearAllFields,
                   bg="green", fg="white", font=("bold", 10)).place(x=250, y=450)
btn_existinguser = Button(window, text="Existing User?", command=callNewScreen,
                          bg="green", fg="white", font=("bold", 10)).place(x=330, y=450)

window.mainloop()
