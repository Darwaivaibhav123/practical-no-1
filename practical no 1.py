marksinsubject=[]

numberofstudents=int(input("Enter total number of students : ")) 
for i in range(numberofstudents):
   marks=int(input("Enter marks of student "+str(i+1)+" : "))
   marksinsubject.append(marks)
   # avrage and sum of students :
def vaibhav ():
    global sum1
    global avrage
    sum1 = 0
    count = 0
    for i in range(len(marksinsubject)):
        sum1 = sum1 +marksinsubject[i]
        count = count + 1
        avrage = sum1 /count
vaibhav()
print ("total marks  =",sum1 )
print ("avrage marks of student =",avrage )
 
# higest marks  by student student :
def high ():
    global mx
    mx =marksinsubject[0]
    for i in range (len(marksinsubject)):
   
        if mx<(marksinsubject[i]):
             mx = marksinsubject[i]
high ()
print ("higest marks obtion by student=", mx)
# lowest marks obtion by student :
def lowest ():
    global mn 
    mn =marksinsubject[0]
    for i in range( len(marksinsubject)):
        if  marksinsubject[i] < mn :
             mn =  marksinsubject[i]
lowest ()
print ("lowest marks obtion by student=", mn)
#count of  absent no of student for test :
def count ():
    global absent 
    for i in range ( len(marksinsubject)):
        absent = 0
        if [i] == -1 :
            absent+=1
count () 
print ("absent no student = ", absent)
