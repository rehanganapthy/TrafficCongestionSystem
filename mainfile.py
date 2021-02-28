from tkinter import * 
from tkinter import messagebox
import timer_function
import soundsensor
import distancesensor
import decongest_neighbor

listlen=[l1,l2,l3,l4]
# data from length sensor
#l1 in +ve x, l2 in -ve x, l3 in +ve y and l4 in -ve y
s1=False
s2=False
s3=False
s4=False

listsignal=[s1,s2,s3,s4]
#signal light, green if true

listtime=[t1,t2,t3,t4]
#time green for each signal

for i in listlen:#if length of traffic is greater than 50m then that lane will be green first
      #sound sensor to allow ambulance
    soundsensor.channel()
   ''' l1=input("Enter distance: ");#to execute manually
    l2=input("Enter distance: ");
    l3=input("Enter distance: ");
    l4=input("Enter distance: "); ''' 
    if listlen(0)<50 and listlen(1)<50 and listlen(2)<50 and listlen(3)<50:
        listsignal(i)=True
        if listsignal(i)==True:
            timer_function.countdown(60)

    else:
        lsort= listlen.sort(reverse=True)
        lmax=max(listlen)
        lsecondmax=lsort(1)
        if lmax>(130/100)*lsecondmax:
            index1=listlen.index(lmax)
            listsignal(index1)=True

    if l1>50 and l2>50 and l3>50 and l4>50:
        top = Tk()  
        top.geometry("200x300")      
        messagebox.showinfo("Important Message", "Deploy Manpower")  
        top.mainloop()  

        #sound sensor to allow ambulance
        soundsensor.channel()

    decongest_neighbor.mod1()   
