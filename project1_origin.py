import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation
file=input() #讀入資料
f=open("NN_HW1_DataSet/NN_HW1_DataSet/"+file,"r")
words=f.read().replace('\r'," ").replace('\n'," ")
f.close()
listxy=[]
listtmp=[]
listexp=[]
words=words.split(" ")

window=tk.Tk()
for i in range(len(words)):
    if i%3==0:
        listtmp.append(float(words[i]))
    elif i%3==1:
        listtmp.append(float(words[i]))
    else:
        listexp.append(int(words[i]))
        listxy.append(listtmp)
        listtmp=[]

def submit():
    global learingtext,learnnumber,listexp,listxy,w,fig
    rate=learingtext.get()
    number=learnnumber.get()
    rate=float(rate)
    number=int(number)

    w=[0,0,0]
    for i in range (3):
        w[i]=random.uniform(-1,1)

    #畫點
    for i in range(len(listexp)):
        if(listexp[i]%2==0):
            plt.scatter(listxy[i][0],listxy[i][1],c='red',s=30)
        else:
            plt.scatter(listxy[i][0],listxy[i][1],c='blue',s=30)
    
    #訓練
    for i in range(number):
        i=i%len(listxy)
        x=[-1]
        for j in range(2):
            x.append(listxy[i][j]) 
        c=0
        for j in range(3): #內積
            c+=w[j]*x[j]
        # print(c)
        if c>0 and listexp[i]%2==0:
            for j in range(3):
                w[j]-=rate*x[j]
        if c<0 and listexp[i]%2==1:
            for j in range(3):
                w[j]+=rate*x[j]
    
    #畫線
    # w[0]=w[1]x+w[2]y
    xline=[]
    yline=[]
    for i in range(-10,10):
        xline.append(i)
        yline.append((w[0]-i*w[1])/w[2])
    
    fig=plt.plot(xline,yline,label="line")
    plt.axis([-10,10,-10,10])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("project1")
    plt.legend(loc='upper right')
    plt.show()

    sum=0 #正確數量
    for i in range(len(listxy)):
        x=[-1]
        for j in range(2):
            x.append(listxy[i][j]) 
        c=0
        for j in range(3): #內積
            c+=w[j]*x[j]
        if c>0 and listexp[i]%2==1:
            sum+=1
        if c<0 and listexp[i]%2==0:
            sum+=1
    print(f"正確率{sum/len(listxy)}")

learnnumbertext=tk.StringVar() #學習次數
learnnumber=tk.Entry(window,textvariable=learnnumbertext)
learnnumber.place(x=120,y=100)
learnnumberlb=tk.Label(window,font="微軟正黑體 8 bold",text="學習次數")
learnnumberlb.place(x=70,y=100)

learingtext=tk.StringVar() #學習率
learingentry=tk.Entry(window,textvariable=learingtext)
learingentry.place(x=120,y=50)
learninglb=tk.Label(window,font="微軟正黑體 8 bold",text="學習率")
learninglb.place(x=70,y=50)

submitbt=tk.Button(window,text="送出",command=submit)
submitbt.place(x=160,y=130)

window.geometry('400x200')
window.title("project1")
window.mainloop()