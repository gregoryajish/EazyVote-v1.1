from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.font as TkFont
from PIL import Image, ImageTk
import mysql.connector
x=0
top = Tk()
top.configure(bg="#121e2a")    # Setting the background of the window
top.geometry("1366x768")    # Setting the size of the window
top.title("Voting")
font5 = TkFont.Font(family="Google Sans", size=10, weight="normal")
font6 = TkFont.Font(family="Google Sans", size=15, weight="bold")
continimg = (Image.open("continuebtn.jpg"))
continbtn= ImageTk.PhotoImage(continimg) 
startimg = (Image.open("startscreen.jpg"))
startscrn= ImageTk.PhotoImage(startimg) 


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

c = Canvas(top,bg = "#121e2a",height = 768,width=1366,bd=0,highlightthickness=0) 
c.create_image(0,0,anchor=NW, image =startscrn)
c.pack()

#Buttons for T&C and About
AboutButton = Button(top, text="ⓘ About", width=20,highlightthickness=0,bd=0,activebackground="#121e2a",bg="#121e2a", fg='white',command=clickAbout)
AboutButton.place(x=1230,y=680)
TandCButton = Button(top, text="Terms & Conditions", width=20,highlightthickness=0,bd=0,activebackground="#121e2a",bg="#121e2a", fg='white',command=clickTerms)
TandCButton.place(x=1130,y=680)

continuebtn =tkinter.Button(c, image=continbtn,highlightthickness=0,bd=0,activebackground="#121e2a",command=lambda e = "OK":click(e),bg="#121e2a")
continuebtn.place(x=550,y=350)
ProductLabel = Label(top,text="ⓒ 2024 EazyVote. All rights reserved.", font=font5, fg="#6c6c6c", bg = "#121e2a", highlightthickness=0)
ProductLabel.place(x=562, y=680)
windstat = False
def click(e):
        global windstat
        top.destroy()
        try:
                windstat=top.state()
        except:
                windstat=True
        
top.mainloop()

cnx=mysql.connector.connect(user="root", password = "1234", host = "localhost", database = "george")
cursor = cnx.cursor()

def convertTuple(tup):
    string = ''
    for item in tup:
        string = string + str(item)
    return string

root = Tk()    # Creating a main window
root.configure(bg="#121e2a")    # Setting the background of the window
root.geometry("1366x768")    # Setting the size of the window
root.title("Voting")    # Setting the title of the window

font1 = TkFont.Font(family="Google Sans",size =14)    # Setting the font
font2 = TkFont.Font(family="Google Sans", size=25, weight="bold")
font3 = TkFont.Font(family="Google Sans", size=17, weight="normal")
font4 = TkFont.Font(family="Google Sans", size=10, weight="normal")

quitimg = (Image.open("quitbtn.jpg"))
quitbtn= ImageTk.PhotoImage(quitimg)
img1= (Image.open("Candidates/candidate1.jpg"))    # Opening image of candidates
Candidate1img= ImageTk.PhotoImage(img1)
img2= (Image.open("Candidates/candidate2.jpg"))
Candidate2img= ImageTk.PhotoImage(img2)
img3= (Image.open("Candidates/candidate3.jpg"))
Candidate3img= ImageTk.PhotoImage(img3)
img4= (Image.open("Candidates/candidate4.jpg"))
Candidate4img= ImageTk.PhotoImage(img4)
img5= (Image.open("Candidates/candidate5.jpg"))
Candidate5img= ImageTk.PhotoImage(img5)
img6= (Image.open("Candidates/candidate6.jpg"))
Candidate6img= ImageTk.PhotoImage(img6)
finishimg = (Image.open("finishbtn.jpg"))
finishbtn= ImageTk.PhotoImage(finishimg)


finishimg = (Image.open("finishbtn.jpg"))
finishbtn= ImageTk.PhotoImage(finishimg)

count1 = 0    # Setting counter to 0
count2 = 0
count3 = 0
count4 = 0

count = 1
cursor.execute("Select Name from candidate order by Serial_No ASC")
record=cursor.fetchall()
candlist=[]
for i in record:
    i=convertTuple(i)
    candlist.append(i)

cursor.execute("Select Serial_NO from candidate order by Serial_No ASC")
sernotuple = cursor.fetchall()
sernolist=[]
for i in sernotuple:
    i=str(convertTuple(i))
    sernolist.append(i)

cursor.execute("select distinct post from candidate ")
posttuple = cursor.fetchall()
postlist=[]
for i in posttuple:
    i=convertTuple(i)
    postlist.append(i)


def clicked(button):
    global PostLabel1,PostLabel2
    global x   
    global nextBtn1,nextBtn2,nextBtn3,nextBtn4      
    global testLabel1,testLabel2,testLabel3,testLabel4,testLabel5,testLabel6
    global Candidate1Btn,Candidate2Btn,Candidate3Btn,Candidate4Btn,Candidate5Btn,Candidate6Btn
    global Candidate1Label,Candidate2Label,Candidate3Label,Candidate4Label,Candidate5Label,Candidate6Label    
    x+=1
    a=button
    no1=testLabel1.cget("text")
    no2=testLabel2.cget("text")
    no5=testLabel5.cget('text')
    Candidate1Btn["state"] = DISABLED
    Candidate2Btn["state"] = DISABLED
    Candidate5Btn['state'] = DISABLED
    if a == "Button 1":
        count1=1
        count2=0
        count5=0
    elif a== "Button 2":
        count2=1
        count1=0
        count5=0
    elif a== "Button 5":
         count5=1
         count2=0
         count1=0
    cursor.execute("update votes set votes = votes+ "+str(count1)+" where serial_no = "+str(no1))
    cursor.execute("update votes set votes = votes + "+str(count2)+" where serial_no = "+str(no2)) 
    cursor.execute("update votes set votes = votes + "+str(count5)+" where serial_no = "+str(no5)) 
    if x==8:
        nextBtn4 = tkinter.Button(root, image=finishbtn,command=lambda n="Button 4":nextclick4(n),bd=0, highlightthickness=0, activebackground="#121e2a")
        nextBtn4.place(x=590,y=500)
    if x==2:
        nextBtn1 = tkinter.Button(root, image=finishbtn,command=lambda n="Button 4":nextclick4(n),highlightthickness=0, bd=0,activebackground="#121e2a")
        nextBtn1.place(x=590,y=500)  
    cnx.commit()

def clicked1(button):
    global x
    global PostLabel1,PostLabel2   
    global nextBtn1,nextBtn2,nextBtn3,nextBtn4      
    global testLabel1,testLabel2,testLabel3,testLabel4,testLabel5,testLabel6
    global Candidate1Btn,Candidate2Btn,Candidate3Btn,Candidate4Btn,Candidate5Btn,Candidate6Btn
    global Candidate1Label,Candidate2Label,Candidate3Label,Candidate4Label,Candidate5Label,Candidate6Label  
    x+=1    
    no3=testLabel3.cget("text")
    no4=testLabel4.cget("text")
    no6=testLabel6.cget("text")
    b=button
    Candidate3Btn["state"] = DISABLED
    Candidate4Btn["state"] = DISABLED
    Candidate6Btn["state"] = DISABLED
    if b == "Button 3":
        count3=1
        count4=0
        count6=0
    elif b== "Button 4":
        count4=1
        count3=0
        count6=0
    elif b== "Button 6":
        count4=0
        count3=0
        count6=1
    cursor.execute("update votes set votes = votes +"+str(count3)+" where serial_no = "+str(no3))
    cursor.execute("update votes set votes = votes +"+str(count4)+" where serial_no = "+str(no4))
    cursor.execute("update votes set votes = votes +"+str(count6)+" where serial_no = "+str(no6))
    cnx.commit()
    if x==8:
        nextBtn4 = tkinter.Button(root, image=finishbtn,command=lambda n="Button 4":nextclick4(n),bd=0, highlightthickness=0, activebackground="#121e2a")
        nextBtn4.place(x=590,y=500)
        x=0
    if x==2:
        nextBtn1 = tkinter.Button(root, image=finishbtn,command=lambda n="Button 4":nextclick4(n),highlightthickness=0, bd=0,activebackground="#121e2a")
        nextBtn1.place(x=590,y=500)


def nextclick4(button):
    global ClassLabel1,ClassLabel2,ClassLabel3,ClassLabel4,ClassLabel5,ClassLabel6
    global FinishLabel1,FinishLabel2, ProductLabel
    global PostLabel1,PostLabel2, testLabel1,testLabel2,testLabel3,testLabel4,testLabel5,testLabel6
    global Candidate1Label,Candidate2Label,Candidate3Label,Candidate4Label,Candidate5Label,Candidate6Label
    global Candidate1Btn,Candidate2Btn,Candidate3Btn,Candidate4Btn,Candidate5Btn,Candidate6Btn 
    global nextBtn4,exitbtn
    ClassLabel1.destroy()
    ClassLabel2.destroy()
    ClassLabel3.destroy()
    ClassLabel4.destroy()
    ClassLabel5.destroy()
    ClassLabel6.destroy()
    Candidate1Btn.destroy()
    Candidate2Btn.destroy()
    Candidate3Btn.destroy()
    Candidate4Btn.destroy()
    Candidate5Btn.destroy()
    Candidate6Btn.destroy()
    Candidate1Label.destroy()
    Candidate2Label.destroy()
    Candidate3Label.destroy()
    Candidate4Label.destroy()
    Candidate5Label.destroy()
    Candidate6Label.destroy()
    testLabel1.destroy()
    testLabel2.destroy()
    testLabel3.destroy()
    testLabel4.destroy()
    testLabel5.destroy()
    testLabel6.destroy()
    PostLabel1.destroy()
    PostLabel2.destroy()
    nextBtn1.destroy()
    FinishLabel1 = Label(root,text="Congratulations! You have finished the voting procedure.", font = font2, fg="#7D6AF0", bg = "#121e2a", highlightthickness=0, highlightcolor="#000000")
    FinishLabel1.place(x=240,y=190)
    FinishLabel2 = Label(root,text="Thank you for using this service.", font = font1, fg="#8899A6", bg = "#121e2a", highlightthickness=0)
    FinishLabel2.place(x=535,y=250)
    exitbtn = tkinter.Button(root, image=quitbtn,command=lambda n="Button 4":extclick(n),highlightthickness=0,bd=0,activebackground="#121e2a")
    exitbtn.place(x=590,y=500)


def extclick(n):
    global x
    global ClassLabel1,ClassLabel2,ClassLabel3,ClassLabel4, ClassLabel5, ClassLabel6
    global FinishLabel1,FinishLabel2
    global exitbtn
    global testLabel1,testLabel2,testLabel3,testLabel4,testLabel5,testLabel6, PostLabel1, PostLabel2
    global Candidate1Label,Candidate2Label,Candidate3Label,Candidate4Label,Candidate5Label,Candidate6Label
    global nextBtn1,Candidate1Btn,Candidate2Btn,Candidate3Btn,Candidate4Btn,Candidate5Btn,Candidate6Btn 
    x=0
    exitbtn.destroy()
    FinishLabel1.destroy()
    FinishLabel2.destroy()
    PostLabel1 = Label(root, text=postlist[0], font = font2, bg = "#121e2a", fg="#03dac6", highlightthickness=0)
    PostLabel1.place(x=230, y=80)
    PostLabel2 = Label(root, text=postlist[1], font = font2, bg = "#121e2a", fg="#03dac6", highlightthickness=0)
    PostLabel2.place(x=910, y=80)
    testLabel1=Label(root, text =str(sernolist[0]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel1.place(x=160,y=300)
    a=int(testLabel1.cget("text"))
    Candidate1Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
    Candidate1Label = Label(root, text =candlist[a-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name 
    Candidate1Label.place(x=150, y=360)    # Positioning the label with candidate name
    Candidate1Btn= tkinter.Button(root, image=Candidate1img,command=lambda m="Button 1":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate1Btn.place(x=110,y=150)    

    #Candidate2
    testLabel2=Label(root, text =str(sernolist[1]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel2.place(x=420,y=300)
    b=int(testLabel2.cget("text"))
    Candidate2Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
    Candidate2Label = Label(root, text =candlist[b-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
    Candidate2Label.place(x=410, y=360)    # Positioning the label with candidate name
    Candidate2Btn= tkinter.Button(root, image=Candidate2img,command=lambda m="Button 2":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate2Btn.place(x=380,y=150)  

    #Candidate3
    testLabel3=Label(root, text =str(sernolist[2]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel3.place(x=820,y=300)
    c=int(testLabel3.cget("text"))
    Candidate3Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
    Candidate3Label = Label(root, text =candlist[c-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
    Candidate3Label.place(x=820, y=360)    # Positioning the label with candidate name
    Candidate3Btn= tkinter.Button(root, image=Candidate3img,command=lambda n="Button 3":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate3Btn.place(x=790,y=150) 

    #Candidate4
    testLabel4=Label(root, text =str(sernolist[3]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel4.place(x=1130,y=300)
    d=int(testLabel4.cget("text"))
    Candidate4Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
    Candidate4Label = Label(root, text =candlist[d-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
    Candidate4Label.place(x=1090, y=360)    # Positioning the label with candidate name
    Candidate4Btn= tkinter.Button(root, image=Candidate4img,command=lambda n="Button 4":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate4Btn.place(x=1060,y=150)

    #Candidate5
    testLabel5=Label(root, text =str(sernolist[4]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel5.place(x=420,y=530)
    e=int(testLabel5.cget("text"))
    Candidate5Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name.
    Candidate5Label = Label(root, text =candlist[e-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name. 
    Candidate5Label.place(x=285, y=640)    # Positioning the label with candidate name.
    Candidate5Btn= tkinter.Button(root, image=Candidate5img,command=lambda m="Button 5":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate5Btn.place(x=245,y=430)    

    #Candidate6
    testLabel6=Label(root, text =str(sernolist[5]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
    testLabel6.place(x=990,y=530)
    f=int(testLabel6.cget("text"))
    Candidate6Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name.
    Candidate6Label = Label(root, text =candlist[f-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name.
    Candidate6Label.place(x=970, y=640)    # Positioning the label with candidate name.
    Candidate6Btn= tkinter.Button(root, image=Candidate6img,command=lambda n="Button 6":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
    Candidate6Btn.place(x=925,y=430)  

    ClassLabel1 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel1.place(x=190,y=385)
    ClassLabel2 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel2.place(x=460,y=385)
    ClassLabel3 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel3.place(x=870,y=385)
    ClassLabel4 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel4.place(x=1140,y=385)
    ClassLabel5 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel5.place(x=330,y=665)
    ClassLabel6 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
    ClassLabel6.place(x=1010,y=665)

    
    if x==2:
        nextBtn1 = tkinter.Button(root, image=finishbtn,command=lambda n="Button 4":nextclick4(n),highlightthickness=0, bd=0,activebackground="#121e2a")
        nextBtn1.place(x=590,y=500)

#Candidate 1
PostLabel1 = Label(root, text=postlist[0], font = font2, bg = "#121e2a", fg="#03dac6", highlightthickness=0)
PostLabel1.place(x=230, y=80)
PostLabel2 = Label(root, text=postlist[1], font = font2, bg = "#121e2a", fg="#03dac6", highlightthickness=0)
PostLabel2.place(x=910, y=80)
testLabel1=Label(root, text =str(sernolist[0]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel1.place(x=160,y=300)
a=int(testLabel1.cget("text"))
Candidate1Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
Candidate1Label = Label(root, text =candlist[a-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name 
Candidate1Label.place(x=150, y=360)    # Positioning the label with candidate name
Candidate1Btn= tkinter.Button(root, image=Candidate1img,command=lambda m="Button 1":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate1Btn.place(x=110,y=150)    

#Candidate2
testLabel2=Label(root, text =str(sernolist[1]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel2.place(x=420,y=300)
b=int(testLabel2.cget("text"))
Candidate2Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
Candidate2Label = Label(root, text =candlist[b-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
Candidate2Label.place(x=410, y=360)    # Positioning the label with candidate name
Candidate2Btn= tkinter.Button(root, image=Candidate2img,command=lambda m="Button 2":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate2Btn.place(x=380,y=150)  

#Candidate3
testLabel3=Label(root, text =str(sernolist[2]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel3.place(x=820,y=300)
c=int(testLabel3.cget("text"))
Candidate3Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
Candidate3Label = Label(root, text =candlist[c-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
Candidate3Label.place(x=825, y=360)    # Positioning the label with candidate name
Candidate3Btn= tkinter.Button(root, image=Candidate3img,command=lambda n="Button 3":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate3Btn.place(x=790,y=150) 

#Candidate4
testLabel4=Label(root, text =str(sernolist[3]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel4.place(x=1130,y=300)
d=int(testLabel4.cget("text"))
Candidate4Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name
Candidate4Label = Label(root, text =candlist[d-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name
Candidate4Label.place(x=1090, y=360)    # Positioning the label with candidate name
Candidate4Btn= tkinter.Button(root, image=Candidate4img,command=lambda n="Button 4":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate4Btn.place(x=1060,y=150)

#Candidate1
testLabel5=Label(root, text =str(sernolist[4]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel5.place(x=420,y=530)
e=int(testLabel5.cget("text"))
Candidate5Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name.
Candidate5Label = Label(root, text =candlist[e-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name. 
Candidate5Label.place(x=285, y=640)    # Positioning the label with candidate name.
Candidate5Btn= tkinter.Button(root, image=Candidate5img,command=lambda m="Button 5":clicked(m), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate5Btn.place(x=245,y=430)    

#Candidate2
testLabel6=Label(root, text =str(sernolist[5]),font=font1,fg="White",bg="#121e2a", highlightthickness=0)
testLabel6.place(x=990,y=530)
f=int(testLabel6.cget("text"))
Candidate6Name = Text(root, height = 5, width = 52)    # Creating a text object with candidate name.
Candidate6Label = Label(root, text =candlist[f-1],font=font1,fg="White",bg="#121e2a", highlightthickness=0)    # Displaying candidate name.
Candidate6Label.place(x=970, y=640)    # Positioning the label with candidate name.
Candidate6Btn= tkinter.Button(root, image=Candidate6img,command=lambda n="Button 6":clicked1(n), borderwidth=0, highlightthickness=0,activebackground="black")
Candidate6Btn.place(x=925,y=430)  

ClassLabel5 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel5.place(x=330,y=665)
ClassLabel6 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel6.place(x=1010,y=665)

ClassLabel1 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel1.place(x=190,y=385)
ClassLabel2 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel2.place(x=460,y=385)
ClassLabel3 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel3.place(x=870,y=385)
ClassLabel4 = Label(root, text = "(X)", font=font1,fg="grey", bg="#121e2a", highlightthickness=0)
ClassLabel4.place(x=1140,y=385)

ProductLabel = Label(root,text="ⓒ 2024 EazyVote. All rights reserved.", font=font4, fg="#6c6c6c", bg = "#121e2a", highlightthickness=0)
ProductLabel.place(x=562, y=680)

if windstat== True:
        root.mainloop()
else:
        pass
cnx.close()
