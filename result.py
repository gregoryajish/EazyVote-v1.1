from tkinter import *
import tkinter
import mysql.connector
from PIL import Image, ImageTk
import tkinter.font as TkFont
import csv

cnx=mysql.connector.connect(user="root", password = "1234", host = "localhost", database = "george")
cursor = cnx.cursor()

cursor.execute("Select * from votes")
votes = cursor.fetchall()
votetablelist=[]
cursor.execute("Select class, post from candidate")
candidates = cursor.fetchall()
candidatelist=[]
for row in votes:
    a=row[0]
    b=row[1]
    c=row[2]
    votetablelist.append([a,b,c])
for item in candidates:
    d=item[0]
    e=item[1]
    candidatelist.append([d,e])
namelist =  [votetablelist[0][1],votetablelist[1][1],votetablelist[4][1],votetablelist[3][1],votetablelist[2][1],votetablelist[5][1]]
total_votes = votetablelist[0][2] + votetablelist[1][2] + votetablelist[4][2] 
voteslist = [votetablelist[0][2],votetablelist[1][2],votetablelist[4][2],votetablelist[3][2],votetablelist[2][2],votetablelist[5][2]]
# serialnolist = [votetablelist[0][0],votetablelist[1][0],votetablelist[4][0],votetablelist[3][0],votetablelist[2][0],votetablelist[5][0]]
serialnolist = [1,2,3,4,5,6]
postlist = [candidatelist[0][1],candidatelist[1][1],candidatelist[4][1],candidatelist[3][1],candidatelist[2][1],candidatelist[5][1]]
classlist = [candidatelist[0][0],candidatelist[1][0],candidatelist[4][0],candidatelist[3][0],candidatelist[2][0],candidatelist[5][0]]

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Total No of Students who Voted",total_votes])
    writer.writerow(["Serial_No", "Candidate Name", "Class","Votes Polled"])
    for j in range(0,6):
        writer.writerow([serialnolist[j], namelist[j], classlist[j], voteslist[j]]) 

root= Tk()
root.configure(bg="#121e2a")    # Setting the background of the window
root.geometry("1366x768")    # Setting the size of the window
root.title("Election Results")    # Setting the title of the window
font1 = TkFont.Font(family="Google Sans",size =18)    # Setting the font
font2 = TkFont.Font(family="Google Sans", size=16)
font3 = TkFont.Font(family="Google Sans", size=17, weight="normal")
font5 = TkFont.Font(family="Google Sans", size=10, weight="normal")
font6 = TkFont.Font(family="Google Sans", size=15, weight="bold")
font4 = TkFont.Font(family="Google Sans", size=10, weight="normal")
ylist = [325,380,432,484,537,589,710]

# Information in the Copyright and Terms of Conditions popup
def clickAbout():
    toplevel = Toplevel(bg = "#121e2a")
    toplevel.title('About EazyVote')
    ABOUT_TEXT = """
    EazyVote represents the pinnacle of election management solutions, 
    featuring a meticulously crafted and visually stunning user interface designed to 
    elevate the integrity and efficiency of internal and student council elections 
    within educational institutions. Powered by robust local databases and leveraging 
    on-site hardware infrastructure, EazyVote guarantees unparalleled levels of security, 
    speed, and scalability, supporting virtually unlimited concurrent users with seamless 
    performance.

    Tailored to meet the precise needs of St. George Public School, Kottapady for the 2024-2025 
    academic session, EazyVote redefines electoral management with its rapid deployment 
    capabilities and real-time data synchronization. Administrators benefit from instantaneous
    access to live election results, presented in a streamlined and intuitive interface. 
    This seamless integration ensures administrators can make informed decisions promptly, 
    fostering a culture of transparency and efficiency within the institution.

    Moreover, EazyVote eliminates post-election delays through its agile real-time updating 
    system, providing administrators with immediate access to comprehensive election statistics 
    and analytics. By streamlining the reporting process and offering unparalleled data 
    visibility, EazyVote accelerates decision-making processes and ensures timely outcomes.

    
    Last updated on: 10th July 2024"""
    label1 = Label(toplevel, text='EazyVote v2.1.1', height=0, width=30, font=font6,bg = "#121e2a",fg='cyan')
    label1.pack()
    label2 = Label(toplevel, text=ABOUT_TEXT, height=0, width=80, font=font5,bg = "#121e2a",fg='#93c4bf')
    label2.pack()

def clickTerms():
    toplevel = Toplevel(bg = "#121e2a")
    toplevel.title('Terms and Conditions')

    termsandconditions = '''
    By accessing or using EazyVote v2.1.1, you agree to comply with these terms and conditions. 
    You are authorized to use this software solely for its intended purpose as described in the 
    product documentation. Any unauthorized use, reproduction, or distribution of EazyVote v2.1.1
    is strictly prohibited and may result in legal action.

    Both Lestlin Robins and/or Gregory Ajish reserve the right to modify, suspend, or
    terminate access to the software at any time without prior notice. EazyVote v2.1.1 is provided
    "as is" without warranty of any kind, express or implied, including but not limited to the 
    warranties of merchantability, fitness for a particular purpose, and non-infringement.

    In no event shall Lestlin Robins and/or Gregory Ajish be liable for any direct, indirect, incidental,
    special, or consequential damages arising out of the use or inability to use EazyVote v2.1.1, 
    including but not limited to loss of data, loss of profits, or business interruption.
    '''

    copyrightText = '''
    EazyVote v2.1.1, developed by Gregory Ajish and Lestlin Robins, is a sophisticated and innovative 
    election management program designed to handle an unlimited number of concurrent users with 
    exceptional efficiency and security. This cutting-edge software provides comprehensive features, 
    including ballot management, real-time analytics, and secure voting protocols. Tailored to meet 
    the specific requirements of St. George School Kottapady, EazyVote v2.1.1 integrates state-of-the-art
    security measures and user-friendly interfaces to ensure a seamless election process.

    Any unauthorized reproduction, distribution, or modification of this software is strictly prohibited. 
    EazyVote v2.1.1 is protected by copyright laws and international treaties.'''

    label1 = Label(toplevel, text='Terms and Conditions', height=0, width=40,font=font6,bg = "#121e2a",fg='cyan')
    label1.pack()
    label2 = Label(toplevel, text=termsandconditions, height=0, width=100,font=font5,bg = "#121e2a",fg='#93c4bf')
    label2.pack()
    label3 = Label(toplevel, text='Copyright © 2024 EazyVote v2.1.1. All rights reserved.', height=0, width=45,font=font6,bg = "#121e2a",fg='cyan')
    label3.pack()
    label4 = Label(toplevel, text=copyrightText, height=0, width=100,font=font5,bg = "#121e2a",fg='#93c4bf')
    label4.pack()

def click(button):
    c.destroy()
    tab = Canvas(root,bg = "#000a12",height = 768,width=1366,bd=0,highlightthickness=0) 
    tab.create_image(0,0,anchor=NW, image =tablescrn)
    tab.pack()
    votelabel = Label(root, text = total_votes, font=font1,fg="cyan", bg="#000a12", highlightthickness=0)
    votelabel.place(x=1013,y=187)
    for i in range(0,6):
        votelabel = Label(root, text =voteslist[i], font=font2,fg="cyan", bg="#000a12", highlightthickness=0)
        votelabel.place(x=1110,y=ylist[i])
        namelabel = Label(root, text =namelist[i], font=font2,fg="cyan", bg="#000a12", highlightthickness=0)
        namelabel.place(x=270,y=ylist[i])
        sernolabel = Label(root, text =serialnolist[i], font=font2,fg="cyan", bg="#000a12", highlightthickness=0)
        sernolabel.place(x=155,y=ylist[i])
        classlabel = Label(root, text =classlist[i], font=font2,fg="cyan", bg="#000a12", highlightthickness=0)
        classlabel.place(x=880,y=ylist[i])
    ProductLabel = Label(root,text="ⓒ 2024 EazyVote. All rights reserved.", font=font4, fg="#6c6c6c", bg = "#121e2a", highlightthickness=0)
    ProductLabel.place(x=562, y=680)

startimg = (Image.open("resstrtscrn.jpg"))
startscrn= ImageTk.PhotoImage(startimg)
generimg = (Image.open("generbtn.jpg"))
generbtn= ImageTk.PhotoImage(generimg)
tableimg = (Image.open("table.jpg"))
tablescrn= ImageTk.PhotoImage(tableimg)

c = Canvas(root,bg = "#121e2a",height = 768,width=1366,bd=0,highlightthickness=0) 
c.create_image(0,0,anchor=NW, image =startscrn)
generatebtn = tkinter.Button(c, image=generbtn,highlightthickness=0,bd=0,activebackground="#121e2a",command=lambda e = "OK":click(e),bg="#121e2a")
generatebtn.place(x=570,y=390)
ProductLabel = Label(root,text="ⓒ 2024 EazyVote. All rights reserved.", font=font4, fg="#6c6c6c", bg = "#121e2a", highlightthickness=0)
ProductLabel.place(x=562, y=680)
#Buttons for T&C and About
AboutButton = Button(root, text="ⓘ About", width=20,highlightthickness=0,bd=0,activebackground="#121e2a",bg="#121e2a", fg='white',command=clickAbout)
AboutButton.place(x=1230,y=680)
TandCButton = Button(root, text="Terms & Conditions", width=20,highlightthickness=0,bd=0,activebackground="#121e2a",bg="#121e2a", fg='white',command=clickTerms)
TandCButton.place(x=1130,y=680)



c.pack()

root.mainloop()
   


