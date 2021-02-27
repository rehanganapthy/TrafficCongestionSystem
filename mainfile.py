

listlen=[l1,l2,l3,l4]
# data from length sensor
boolean s1,s2,s3,s4
listsignal=[s1,s2,s3,s4]
#signal light, green if true

listtime=[t1,t2,t3,t4]
#time green for each signal

for i in listlen:#if length of traffic is greater than 50m then that lane will be green first
    if listlen(0)<50 and listlen(1)<50 and listlen(2)<50 and listlen(3)<50:
        
            listsignal(i)=True
            if listsignal(i)==True:

                #import timer modeule

    else:
        lsort= listlen.sort(reverse=True)
        lmax=max(listlen)
        lsecondmax=lsort(1)
        if lmax>(130/100)*lsecondmax:
            index1=listlen.index(lmax)
            listsignal(index1)=True

    elif l1,l2,l3,l4 > 50:

        #send message to control room

    elif :
        #sound sensor to allow ambulance

    elif:
        #if any of the other signals are blocked, release that lane

        

        
        


                       
