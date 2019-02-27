from Tkinter import *
from tkMessageBox import *
import sqlite3
conn=sqlite3.Connection('quiz.db')
cur=conn.cursor()

def main_project():
  #root=Tk()
  root=Tk()
  root.geometry('1366x768')
  root.configure(background='black')
  Label(root,text='QUIZ MAKER',relief='sunken',font='helvetica 30',fg='red',bg='pink',justify='center').grid(row=0,column=15)


                          
  def parent_window():
   root=Tk()
   root.geometry('1366x768')
   root.configure(background='black')
   Label(root,text='QUIZ MAKER',relief='sunken',font='helvetica 30',fg='red',bg='pink',justify='center').grid(row=0,column=15)
   Button(root,text='Administrator Login',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=administrator).grid(row=3,column=10)
   Button(root,text='Make a Quiz',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=make_quiz).grid(row=3,column=20)
   Button(root,text='Give a Quiz',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=give_quiz).grid(row=9,column=15)

















  def make_quiz():
    
    root1=Tk()
    root1.geometry('1966x768')
    root1.configure(background="RoyalBlue4")

    Label(root1,text='LOGIN',font='times 30 bold',bg='pink',fg='brown').grid(row=0,column=10)
    Label(root1,text='Faculty ID',font='times 20 bold',fg='yellow',bg='RoyalBlue4').grid(row=4,column=8)
    e1=Entry(root1,font='times 15 bold',border=4)
    e1.grid(row=4,column=10)
    
    
    Label(root1,text='Password',font='times 20 bold',fg='yellow',bg='RoyalBlue4').grid(row=10,column=8)
    e2=Entry(root1,font='times 15 bold',border=4)
    e2.grid(row=10,column=10)
    found=1
    def err():
                  showinfo('error','Faculty ID or Paswword is wrong')
    def check():
        a=cur.execute('select * from faculty')
        for row in a:
            if((e1.get())==(row[0]) and e2.get()==(row[2])):
                o=row[1]
                cur.execute('create table if not exists quiz2(qid varchar(10) PRIMARY KEY,subject varchar(20),batch varchar(4),semester number(1))')
                f=cur.execute('select * from quiz2')
                
                
                def allot_qid():
                   i=0
                   for row in f:
                      #print row 
                      i=i+1 
                   return i+1     
                c=allot_qid() 
                print c

                Label(root1,text=' ',bg='RoyalBlue4').grid(row=15,column=6)
                Label(root1,text=' ',bg='RoyalBlue4').grid(row=19,column=6)
                Label(root1,text=' ',bg='RoyalBlue4').grid(row=23,column=6)


                

                Label(root1,text='Quiz ID : '+str(c),font='times 22 bold',fg='pink',bg='RoyalBlue4').grid(row=25,column=8)

                Label(root1,text='Subject : ',font='times 22 bold',fg='pink',bg='RoyalBlue4').grid(row=27,column=8)
                s2=Entry(root1,font='times 15 bold',fg='orange',border=3)
                s2.grid(row=27,column=10)

                Label(root1,text='Batch : ',font='times 22 bold',fg='pink',bg='RoyalBlue4').grid(row=29,column=8)
                s3=Entry(root1,font='times 15 bold',fg='orange',border=3)
                s3.grid(row=29,column=10)
                
                Label(root1,text='Semester : ',font='times 22 bold',fg='pink',bg='RoyalBlue4').grid(row=31,column=8)
                s4=Entry(root1,font='times 15 bold',fg='orange',border=3)
                s4.grid(row=31,column=10)
                
                def insert_quiz():
                    cur.execute("insert into quiz2 values(?,?,?,?)",(c,s2.get(),s3.get(),s4.get()))
                    conn.commit()
                    root1.destroy()
                    root2=Tk()
                    root2.geometry('800x500')
                    root2.configure(background="grey")
                
                    Label(root2,text=str(o),font='times 25 bold',fg='RoyalBlue4',bg='grey').grid(row=0,column=15)
                    def add():
                         Label(root2,text='Q. No.',font='times 19 bold',fg='VioletRed3',bg='grey').grid(row=5,column=2)                
                         Label(root2,bg='grey').grid(row=4,column=3)
                         Label(root2,text='Questions',font='times 19 bold',fg='VioletRed3',bg='grey').grid(row=7,column=2)
                        
                         q1=Entry(root2,font='times 18 bold',border=3)
                         q1.grid(row=5,column=15)
                         Label(root2,bg='grey').grid(row=6,column=3)
                         q2=Entry(root2,font='times 18 bold',border=3)
                         q2.grid(row=7,column=15)

                         q3=Entry(root2,font='times 18 bold',border=3)
                         q3.grid(row=9,column=15)
                         q4=Entry(root2,font='times 18 bold',border=3)
                         q4.grid(row=11,column=15)
                         q5=Entry(root2,font='times 18 bold',border=3)
                         q5.grid(row=13,column=15)
                         Label(root2,bg='grey').grid(row=8,column=3)
                         Label(root2,text='Option 1',font='times 18 bold',fg='VioletRed3',bg='grey').grid(row=9,column=2)
                         Label(root2,bg='grey').grid(row=10,column=3)
                         Label(root2,text='Option 2',font='times 19 bold',fg='VioletRed3',bg='grey').grid(row=11,column=2)
                         Label(root2,bg='grey').grid(row=12,column=3)
                         Label(root2,text='Answer(option)',font='times 19 bold',fg='VioletRed3',bg='grey').grid(row=13,column=2)

                      
                         def insert():
                              cur.execute('create table if not exists questions2(qid varchar(10),qno number(2),ques varchar(30),opt1 varchar(20),opt2 varchar(20),ans number(3))')
                              cur.execute('insert into questions2(qid,qno,ques,opt1,opt2,ans) values(?,?,?,?,?,?)',(c,q1.get(),q2.get(),q3.get(),q4.get(),q5.get()))
                              conn.commit()
                              x=cur.execute('select * from questions2')    
                              #for row in x:
                                 # print row
                              showinfo('inserted','Question inserted sucessfully')

                         Button(root2,text='ADD',font='times 18 bold italic',height=3,width=10,fg='blue',command=insert).grid(row=20,column=15)
                    Label(root2,bg='grey').grid(row=15,column=3)
                    Button(root2,text='Add Question',font='times 18 bold',fg='orange',bg='red',height=3,width=10,command=add).grid(row=20,column=10)
                     




               
                Button(root1,text='Insert quiz',font='times 15 bold',fg='pink',bg='red',height=2,width=10,command=insert_quiz).grid(row=60,column=9)



                
                
                
                #x=cur.execute('select * from questions2')    
                #for row in x:
                 #   print row
                
    
    #if(found==1):
     #   err()
            
        



    Label(root1,text=' ',bg='RoyalBlue4').grid(row=13,column=6)
    Button(root1,text='Submit',font='times 15 bold',width=6,height=1,command=check).grid(row=15,column=8)
    Button(root1,text='Home',font='times 15 bold',width=6,height=1,command=parent_window).grid(row=15,column=10)  
    
  
    
  def administrator():
    #root.destroy()
    root3=Tk()
    root3.geometry('1366x768')
    root3.configure(background="grey")
    Label(root3,text='Administrator Login',font='times 25 bold italic',fg='red4',bg='cyan3').grid(row=3,column=3)
    Label(root3,text='Administrator ID : ',font='times 25 bold italic',fg='blue2',bg="grey").grid(row=9,column=2)
    a1=Entry(root3,border=5,font='times 15 bold',fg='violet red')
    a1.grid(row=9,column=4)

    Label(root3,text='Administrator Password :',font='times 25 bold italic',fg='blue2',bg="grey").grid(row=12,column=2)
    a2=Entry(root3,border=5,font='times 15 bold',fg='violet red')
    a2.grid(row=12,column=4)
    

    def admin_check():
         if(a1.get()=='1' and a2.get()=='1'):

             def faculty():
                 root3.destroy()
                 
                 cur.execute('create table if not exists faculty(fid varchar(10) PRIMARY KEY,name varchar(20),password varchar(15))')
                 f=cur.execute('select * from faculty')
                 i1=0
                 for row in f:
                    i1=i1+1  

                 root4=Tk()

                 Label(root4,text='Faculty Details ',font='times 20 italic bold',fg='SpringGreen4').grid(row=0,column=3)

                 Label(root4,text='Faculty ID : '+str(i1),font='times 20 bold',fg='SpringGreen4').grid(row=5,column=2)
                 Label(root4,text='Faculty Name :',font='times 20 bold',fg='SpringGreen4').grid(row=7,column=2)
                 f1=Entry(root4)
                 f1.grid(row=7,column=4)
                 Label(root4,text='Password :',font='times 20 bold',fg='SpringGreen4').grid(row=9,column=2)
                 f2=Entry(root4)
                 f2.grid(row=9,column=4)

                 def insert_faculty():
                      cur.execute("insert into faculty(fid,name,password) values(?,?,?)",(i1+1,f1.get(),f2.get()))
                      conn.commit()
                      temp=cur.execute('select * from faculty')
                      for row in temp:
                          print row

                 Button(root4,text='Insert',font='times 20 bold',fg='orange',command=insert_faculty).grid(row=13,column=2)

             def students():
                 #root3.destroy()
                 cur.execute('create table if not exists students(sid varchar(10) PRIMARY KEY,name varchar(20),password varchar(15),batch varchar(4),semester number(1))')
                 f=cur.execute('select * from students')
                 i1=0
                 for row in f:
                    i1=i1+1  

                 root5=Tk()
                 root5.geometry('1366x768')

                 Label(root5,text='Students Details ',font='times 20 bold',fg='light pink',bg='dark orchid').grid(row=0,column=3)

                 Label(root5,text='Student ID :'+str(i1+1),font='times 20 bold',fg='forest green').grid(row=5,column=2)
                 Label(root5,text='Student Name :',font='times 20 bold',fg='forest green').grid(row=7,column=2)
                 f1=Entry(root5,border=4,font='helvetica 16')
                 f1.grid(row=7,column=4)
                 Label(root5,text='Password :',font='times 20 bold',fg='forest green').grid(row=9,column=2)
                 f2=Entry(root5,border=4,font='helvetica 16')
                 f2.grid(row=9,column=4)

                 Label(root5,text='Batch :',font='times 20 bold',fg='forest green').grid(row=11,column=2)
                 f3=Entry(root5,border=4,font='helvetica 16')
                 f3.grid(row=11,column=4,)
                 Label(root5,text='Semester :',font='times 20 bold',fg='forest green').grid(row=13,column=2)
                 f4=Entry(root5,border=4,font='helvetica 16')
                 f4.grid(row=13,column=4)



                 def insert_students():
                      cur.execute("insert into students(sid,name,password,batch,semester) values(?,?,?,?,?)",(i1+1,f1.get(),f2.get(),f3.get(),f4.get()))
                      conn.commit()
                      temp=cur.execute('select * from students')
                      for row in temp:
                          print row

                 Button(root5,text='Insert Student',font='times 20 bold',fg='orange',command=insert_students).grid(row=15,column=2)
                 



             Button(root3,text='New Student',font='times 20 bold',fg='orange',command=students).grid(row=17,column=2)
             Button(root3,text='New Faculty',font='times 20 bold',fg='orange',command=faculty).grid(row=17,column=4)
             Button(root3,text='Home',font='times 20 bold',fg='orange',command=parent_window).grid(row=17,column=6)
             
             
             
              


               


    Button(root3,text='Submit',font='times 16 bold',fg='firebrick1',bg='DarkOrchid4',width=6,height=1,command=lambda:admin_check()).grid(row=15,column=3)


    
    
  def give_quiz():
                 #root.destroy()
                 root6=Tk()
                 root6.geometry('1966x768')
                 root6.configure(background="turquoise4")
                 Label(root6,text='Student Login',font='times 30 bold italic',bg='black',fg='pink').grid(row=0,column=10)
                 
                 Label(root6,bg='turquoise4').grid(row=3,column=3)
                 Label(root6,text='Student ID :',font='times 22 bold',fg='burlywood1',bg="turquoise4").grid(row=5,column=6)
                 s1=Entry(root6,font='times 15 bold',border=4)
                 s1.grid(row=5,column=12)
                 Label(root6,text='Password :',font='times 22 bold',fg='burlywood1',bg="turquoise4").grid(row=9,column=6)
                 s2=Entry(root6,font='times 15 bold',border=4)
                 s2.grid(row=9,column=12)
                 Label(root6,text='Batch :',font='times 22 bold',fg='burlywood1',bg="turquoise4").grid(row=11,column=6)
                 s3=Entry(root6,font='times 15 bold',border=4)
                 s3.grid(row=11,column=12)
                 Label(root6,text='Semester :',font='times 22 bold',fg='burlywood1',bg="turquoise4").grid(row=13,column=6)
                 s4=Entry(root6,font='times 15 bold',border=4)
                 s4.grid(row=13,column=12)


                 def authenticate():
                    a=cur.execute('select * from students')
 
                    for row in a:
        
                       if(str(s1.get())==str(row[0]) and str(s2.get())==str(row[2]) and str(s3.get())==str(row[3]) and str(s4.get())==str(row[4])):
                          
                          root7=Tk()
                          root7.geometry('1966x768')
                          root7.configure(background="gray14")
                          Label(root7,text='Available Quizes',relief='sunken',font='times 25 bold',bg='gray14',fg='tomato2').grid(row=0,column=7)
                          Label(root7,text='Quiz ID ',font='times 20 italic',bg='gray14',fg='orchid').grid(row=5,column=3)
                          Label(root7,text='Subject ',font='times 20 italic',bg='gray14',fg='cyan').grid(row=5,column=5)
                          
                           




                          
                          
                          
                          def give(x):
                                g=cur.execute('select * from questions2')
                                i=4 
                                for row4 in g:
                                 if(x==row4[0]):
                                  f=cur.execute('select subject from quiz2 where qid=?',[x])
                      
                                  sub=[]
                                  sub=cur.fetchall()
                                  for t in sub:
                                    
                                      z=t[0]
                                  root7.destroy()
                                  root8=Tk()
                                  root8.geometry('1966x768')
                                  root8.configure(background="gray95") 
                                  
                                  Label(root8,text='Student Name :'+str(row[1]),font='times 25 bold',bg='gray95',fg='red').grid(row=0,column=2)
                                  Label(root8,text='Quiz ID : '+str(x),font='times 22 bold',bg='gray95',fg='turquoise4').grid(row=3,column=3)                          
                                  Label(root8,bg='purple3')
                                  Label(root8,text='Subject : '+str(z),font='times 22 bold',bg='gray95',fg='turquoise4').grid(row=2,column=3)
                                  
                                  


                                  
                                  
                                      
                                      
                                     
                                
                                
                                  
                                  marks=0    
                                  def show(y):    
                                    root10=Tk()

                                    print x
                                    b=[]
                                    cur.execute('select  * from questions2 where qid=? and qno=?',(x,y))
                                    b=cur.fetchall()
                                    for i in b:
                                        
                                        root10.geometry('400x400')
                                         
                                        Label(root10,text='Q.no : '+str(i[1]),font='times 15 bold',fg='blue').grid(row=2,column=1)
                                        
                                        Label(root10,text=str(i[2]),font='times 15 bold',fg='blue').grid(row=4,column=1)
                                        
                                        rt=IntVar()
                                       

                                        def submit():
                                          if(rt.get()==(i[5])):
                                              showinfo('congratulations','correct answer')
                                          else:   
                                             showinfo('sorry','Wrong answer')
                                        Button(root10,text='Submit',font='times 20 bold',fg='blue',command=submit).grid(row=16,column=1)  
                                        Radiobutton(root10,text=str(i[3]),font='times 15 bold',fg='blue',variable=rt,value=1).grid(row=6,column=2)
                                        
                                        Radiobutton(root10,text=str(i[4]),font='times 15 bold',fg='blue',variable=rt,value=2).grid(row=8,column=2)
                                         
                                        
                                        
                                        def exi():
                                             root10.destroy()
                                        Button(root10,text='Exit',font='times 20 bold',fg='blue',command=exi).grid(row=16,column=3)
                                       



   

                                  def show_buttons():
                                      root8.destroy()
                                      root9=Tk()
                                      root9.geometry('1966x768')
                                      root9.configure(background='pink')
                                      Label(root9,text='Press question...',font='times 24 bold italic',fg='red').grid(row=0,column=5)
                                      Button(root9,text=str(1),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(1))).grid(row=3,column=0)
                                      Button(root9,text=str(2),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(2))).grid(row=3,column=8)
                                      Button(root9,text=str(3),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(3))).grid(row=6,column=0)
                                      Button(root9,text=str(4),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(4))).grid(row=6,column=8)
                                      Button(root9,text=str(5),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(5))).grid(row=8,column=0)
                                      Button(root9,text=str(6),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(6))).grid(row=8,column=8)
                                      Button(root9,text=str(7),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(7))).grid(row=10,column=0)
                                      Button(root9,text=str(8),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(8))).grid(row=10,column=8)
                                      Button(root9,text=str(9),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(9))).grid(row=12,column=0)
                                      Button(root9,text=str(10),font='times 18 bold italic',width=14,height=4,bg='purple',fg='yellow',command=lambda:(show(10))).grid(row=12,column=8)
                                    




                                  Button(root8,text='START',font='times 20 bold',fg='turquoise4',bg='gray95',bd=3,command=show_buttons).grid(row=7,column=2)
                                      
                          
                          m=cur.execute('select qid,subject from quiz2 where batch=? and semester=?',(s3.get(),s4.get()))
                          i=7
                          for row2 in m:
                                 
                                 
                                
                                 Label(root7,text=row2[0],font='times 17 italic',fg='turquoise3',bg='gray14').grid(row=i,column=1)
                                 Label(root7,text=row2[1],font='times 17 italic',fg='turquoise3',bg='gray14').grid(row=i,column=3)       

                                 i=i+1
                          Label(root7,bg="gray14").grid(row=i+3,column=4)
                          
                          Label(root7,text='Enter quiz number to give',font='times 22 italic',bg='gray14',fg='orange').grid(row=i+5,column=2)
                          e=Entry(root7,font='times 17 bold',fg='red',border=5)
                          e.grid(row=i+5,column=4)
                          Label(root7,bg="gray14").grid(row=i+6,column=4)       
                          Button(root7,text='Give it',font='times 20 bold',bg='gray14',fg='pink',bd=4,width=10,height=2,command=lambda:give(e.get())).grid(row=i+7,column=2)
                                                             
                                
                          

                                        
                          
                           
                          
                          

                 Label(root6,text='',bg='turquoise4').grid(row=15,column=3)
                 Label(root6,text='',bg='turquoise4').grid(row=17,column=3)
                 
                          
                 Button(root6,text='Enter',font='times 20 bold',bg='black',bd=3,fg='red',command=authenticate).grid(row=17,column=7)
                 Button(root6,text='Home',font='times 20 bold',bg='black',fg='red',command=parent_window).grid(row=17,column=14)
    
    
    

  Button(root,text='Administrator Login',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=administrator).grid(row=3,column=10)
  Button(root,text='Make a Quiz',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=make_quiz).grid(row=3,column=20)
  Button(root,text='Give a Quiz',font='times 20 italic bold',fg='yellow',bg='purple',width=15,height=3,command=give_quiz).grid(row=9,column=15)


main_project()










mainloop()














