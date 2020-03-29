from tkinter import *
import tkinter
import webbrowser
def gui():
    top = tkinter.Tk()
    top.geometry("550x550")
    top.configure(background='pink')
    def move():   
        if message.winfo_x() + message.move >= message.x_limit or message.winfo_x() + message.move < 0:
            message.move = -message.move
        message.place(x=message.winfo_x() + message.move)
        message.after(message.delay, move)
    message = Label(top, text = 'THE OS PROJECT')
    message.config (fg = 'white',bg='red' ,font=('times','24'))
    message.x_limit = 290
    message.move = 2
    message.delay = 25
    message.place(x=1,y=20)
    message.after(25, move)
    def close_window():
        top.destroy()
    def gui2():
         webbrowser.open('https://en.wikipedia.org/wiki/Page_replacement_algorithm')
    label2=tkinter.Label(text="TOPIC -PAGE REPLACEMENT ALGORITHMS",font=("times new roman",12),fg='white',bg='red')
    label2.place(x=20,y=80)
    label2=tkinter.Label(text="CREDITS :",font=("times new roman",12),fg='white',bg='red')
    label2.place(x=20,y=290)
    label3=tkinter.Label(text="SOHAM PRADHAN -16102B0003",font=("Times New Roman",12),fg='white',bg='blue')
    label3.place(x=20,y=340)
    label3=tkinter.Label(text="ABHI KADAM -16102B0004",font=("Times New Roman",12),fg='white',bg='blue')
    label3.place(x=20,y=360)
    label3=tkinter.Label(text="MAYUR WANVE -16102B0009",font=("Times New Roman",12),fg='white',bg='blue')
    label3.place(x=20,y=380)
    label3=tkinter.Label(text="ATHARVA JOSHI -16104B0003",font=("Times New Roman",12),fg='white',bg='blue')
    label3.place(x=20,y=400)
    label4=tkinter.Label(text="ANUPAMA MHATRE -16104B0069",font=("Times New Roman",12),fg='white',bg='blue')
    label4.place(x=20,y=420)
    label5=tkinter.Label(text="WHAT ARE PAGE REPLACEMENT ALGORITHMS ?",font=("Times New Roman",12),fg='white',bg='green')
    label5.place(x=20,y=120)
    label6=tkinter.Label(text="I WANT TO SEE HOW THEY WORK",font=("Times New Roman",12),fg='white',bg='green')
    label6.place(x=20,y=200)
    button1=tkinter.Button(text="CLICK ME",command =gui2,fg='white',bg='green')
    button1.place(x=20,y=160)
    button1=tkinter.Button(text="CLICK ME",command =close_window,fg='white',bg='green')
    button1.place(x=20,y=240)
    top.mainloop()
def max1(l):
    max2=l[0]
    pos=0
    for i in range(1,frame):
        if max2<l[i]:
            max2=l[i]
            pos=i
    return pos

def search(l,ele):
    for i in range(len(l)):
        if ele==l[i]:
            return 1
    return 0

def fifo(n,frame):
    outmat=[]
    for i in range(frame):
        outmat.append([])
    sign = "_"
    for i in range(frame):
        for j in range(n):
            outmat[i].append(sign)
    temp=[]
    hit=0
    m=0    
    for i in range(frame):
        temp.append(0)
    c=0
    for i in range(n):
        flag=0
        if c==frame:
            break
        for j in range(len(temp)):
            if l[i]==temp[j] and i!=j:
                hit+=1
                flag=1
                break
        if flag==0:
            temp[c]=l[i]
            c+=1
    for q in range(len(temp)):
        for w in range(n):
            if q<=w:
                outmat[q][w]=temp[q]
    for z in range(i,n):
        count=0    
        for k in range(frame):
            if l[z]==temp[count]:
                hit+=1
                break
            else:
                count+=1
        if count==frame:
            u=m%frame
            temp[u]=l[z]
            m+=1
            for itr in range(z,n):
                outmat[u][itr]=temp[u]
    print()
    print("FIFO:")
    print()
    for dis in range(len(l)):
        print(" ",l[dis],end=" ")
    print()
    for h in range(n):
        print("---",end="-")
    print()
    for x in range(frame):
        print("|",end=" ")
        for y in range(n):
            print(outmat[x][y],end=" | ")
        print()
        for y in range(n):
            print("---",end="-")
        print()
    print("Hit = ",hit)
    hratio=(hit/n)
    print("Hit ratio = ",hratio)
    return(hit)
    
def lru(n,frame):
    outmat=[]
    for i in range(frame):
        outmat.append([])
    sign = "_"
    for i in range(frame):
        for j in range(n):
            outmat[i].append(sign)
    temp=[]
    hit=0
    m=0    
    for i in range(frame):
        temp.append(0)
    c=0
    for i in range(n):
        flag=0
        if c==frame:
            break
        for j in range(len(temp)):
            if l[i]==temp[j]:
                hit+=1
                flag=1
                break
        if flag==0:
            temp[c]=l[i]
            c+=1
    for q in range(len(temp)):
        for w in range(n):
            if q<=w:
                outmat[q][w]=temp[q]
    for q in range(i,n):
        if search(temp,l[q]): #if hit
            hit+=1
        else:
            ctemp=[]
            for r in range(frame): #finding lru element
                count=0
                ctemp.append(0)
                for w in range(q-1,-1,-1):
                    if l[w]!=temp[r]:
                        count+=1
                    else:
                        break
                ctemp[r]=count
            pos=max1(ctemp)
            temp[pos]=l[q]
            for itr in range(q,n):
                   outmat[pos][itr]=temp[pos]
    print()
    print("LRU:")
    print()
    for dis in range(len(l)):
        print(" ",l[dis],end=" ")
    print()
    for h in range(n):
        print("---",end="-")
    print()
    for x in range(frame):
        print("|",end=" ")
        for y in range(n):
            print(outmat[x][y],end=" | ")
        print()
        for y in range(n):
            print("---",end="-")
        print()
    print("Hit = ",hit)
    hratio=(hit/n)
    print("Hit ratio = ",hratio)
    return(hit)
    
def optimal(n,frame):
    outmat=[]
    for i in range(frame):
        outmat.append([])
    sign = "_"
    for i in range(frame):
        for j in range(n):
            outmat[i].append(sign)
    temp=[]
    hit=0
    m=0    
    for i in range(frame):
        temp.append(0)
    c=0
    for i in range(n):
        flag=0
        if c==frame:
            break
        for j in range(len(temp)):
            if l[i]==temp[j]:
                hit+=1
                flag=1
                break
        if flag==0:
            temp[c]=l[i]
            c+=1
    for q in range(len(temp)):
        for w in range(n):
            if q<=w:
                outmat[q][w]=temp[q]
    for q in range(i,n):
        if search(temp,l[q]): #if hit
            hit+=1
        else:
            ctemp=[]
            for r in range(frame): #finding lru element
                count=0
                ctemp.append(0)
                for w in range(q+1,n):
                    if l[w]!=temp[r]:
                        count+=1
                    else:
                        break
                ctemp[r]=count
            pos=max1(ctemp)
            temp[pos]=l[q]
            for itr in range(q,n):
                   outmat[pos][itr]=temp[pos]
    print()
    print("OPTIMAL:")
    print()
    for dis in range(len(l)):
        print(" ",l[dis],end=" ")
    print()
    for h in range(n):
        print("---",end="-")
    print()
    for x in range(frame):
        print("|",end=" ")
        for y in range(n):
            print(outmat[x][y],end=" | ")
        print()
        for y in range(n):
            print("---",end="-")
        print()
    print("Hit = ",hit)
    hratio=(hit/n)
    print("Hit ratio = ",hratio)
    return(hit)

def analyze(n,frame):
    hits=[]
    hits.append(fifo(n,frame))
    hits.append(lru(n,frame))
    hits.append(optimal(n,frame))
    max1=hits[0]
    pos=0
    for i in range(1,3):
        if max1<hits[i]:
            max1=hits[i]
            pos=i
    if max1==hits[0]==hits[1]:
        print("Any method can be used to solve the problem")
    elif max1==hits[0]:
        if max1==hits[1]:
            print("FIFO and LRU methods are suitable for these inputs")
        elif max1==hits[2]:
            print("FIFO and OPTIMAL methods are suitable for these inputs")
    elif max1==hits[1]:
        print("LRU and OPTIMAL methods are suitable for these inputs")
    else:
        if pos==0:
            print("FIFO is the best suitable method for these inputs")
        elif pos==1:
            print("LRU is the best suitable method for these inputs")
        elif pos==2:
            print("OPTIMAL is the best suitable method for these inputs")
gui()        
n=int(input("Enter total number of pages to insert:"))
frame=int(input("Enter total number of cache frames:"))
l=[]
for i in range(n):
    print("Enter number",i+1,":")
    x=int(input())
    l.append(x)
while(True):
    ch=int(input("Enter choice 1:FIFO 2:LRU 3:OPTIMAL 4:Analyze 5:Exit:"))
    if ch==1:
        fifo(n,frame)
    elif ch==2:
        lru(n,frame)
    elif ch==3:
        optimal(n,frame)
    elif ch==4:
        analyze(n,frame)
        break
    elif ch==5:
        break
    else:
        print("Invalid choice")

'''Try these inputs:
number of elements = 10
frames = 4
numbers= 1 5 4 3 1 2 6 7 3 2
Same number of hits'''
