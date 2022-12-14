import random
import datetime


name = []
phno = []
add = []
bookedin = []
bookedout= []
car = []
price = []
rc = []
p = []
carno = []
custid = []
day = []


i = 0


def Home():
      
      
    print( "********************* Welcome To Car Rental *********************\n")
    print("\t\t 1 Booking\n")
    print("\t\t 2 Cars_info\n")
    print("\t\t 3 Payment\n")
    print("\t\t 4 Record\n")
    print("\t\t 0 Exit\n")
  
    
    ch=int(input("->"))
	
    if ch == 1:
        print(" ")
        Booking()

    elif ch == 2:
        print(" ")
        CARS_Info()


    elif ch == 3:
        print(" ")
        Payment()


    elif ch == 4:
        print(" ")
        Record()

    else:
        exit()
    
        
#----------BOOKING DATE-------
def date(c):
    
    if c[2]>=2021 and c[2]<=2025:
        
        if c[1]!=0 and c[1]<=12:
            
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                
                if c[2]%4==0 and c[0]<=31:
                    pass
                
                elif c[0]<=29:
                    pass
                
                else:
                    print("Invalid Date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    bookedin.pop(i)
                    bookedout.pop(i)
                    Booking()
            
            
            
            elif c[1]<=7 and c[1]%2!=0 and c[0]<31:
                pass
            
            elif c[1]<=7 and c[1]%2==0 and c[0]<=30 and c[1]!=2:
                pass
            
            elif c[1]>=8 and c[1]%2 == 0 and c[0]<=31:
                pass
            
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                pass
            
            
            else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                bookedin.pop(i)
                bookedout.pop(i)
                Booking()
                
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            bookedin.pop(i)
            bookedout.pop(i)
            Booking()
    
    
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        bookedin.pop(i)
        bookedout.pop(i)
        Booking()


#-----------BOOKING PROCESS --------
def Booking():
      
      
       global i
       print("Booking Car")
       print(" ")
       
       
       while 1 :
           n = str(input("Your Name: "))
           p1 = str(input("Phone No.:"))
           a = str(input("Address:"))
           
           
           if n!="" and p1!="" and a!="":
               name.append(n)
               add.append(a)
               break
           else:
               print("\tName,Phone No, & Address cannot be empty.")
               
       #write date as example: dd/mm/yyyy)
        
       cii=str(input("Booked-in(dd/mm/yyyy): "))
       bookedin.append(cii)
       cii=cii.split('/')
       ci=cii
       ci[0]=int(ci[0])
       ci[1]=int(ci[1])
       ci[2]=int(ci[2])
       date(ci)
      
       coo=str(input("Booked-Out: "))
       bookedout.append(coo)
       coo=coo.split('/')
       co=coo
       co[0]=int(co[0])
       co[1]=int(co[1])
       co[2]=int(co[2])
       
       if co[1]<ci[1] and co[2]<ci[2]:

           print("\n\tErr..!!\n\tbooked-Out date must fall after booked-In\n")
           name.pop(i)
           add.pop(i)
           bookedin.pop(i)
           bookedout.pop(i)
           Booking()
       
       elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
           print("\n\tErr..!!\n\tBooked-Out date must fall after booked-In\n")
           name.pop(i)
           add.pop(i)
           bookedin.pop(i)
           bookedout.pop(i)
           Booking()
       else:
           pass
       
       date(co)
       d1 = datetime.datetime(ci[2],ci[1],ci[0])
       d2 = datetime.datetime(co[2],co[1],co[0])
       d = (d2-d1).days
       day.append(d)
       
       print("\t\t\t\t\t SELECT CAR TYPE \t\t\t\t\t")
       print(" 1. SEDAN ")
       print(" 2. SUV ")
       print(" 3. COUPE ")
       print(" 4. SPORTS CAR ")
       print("\t\t\t\t Press 0 for CAR Prices \t\t\t\t\t")
       
       ch=int(input(">>>"))
       
       
       if ch==0:
           print(" 1. SEDAN --- Rs. 10000")
           print(" 2. SUV--- Rs. 15000")
           print(" 3. COUPE --- Rs. 20000")
           print(" 4. SPORTS CAR --- Rs. 130000")  
           ch=int(input())
           
       if ch==1:
           car.append('SEDAN')
           print("CAR TYPE- SEDAN")
           price.append(10000)
           print("price-Rs.10000")
           
       elif ch==2:
           car.append('SUV')
           print("CAR TYPE- SUV")
           price.append(15000)
           print("price-Rs.15000")           
       elif ch==3:
           car.append('COUPE')
           print("CAR TYPE- COUPE")
           price.append(20000)
           print("price-Rs.20000")
       elif ch==4:
           car.append('SPORTS CAR')
           print("CAR TYPE- SPORTS")
           price.append(30000)
           print("price-Rs.30000")           
       else:
           print("Wrong Choice..!!")    
           
           
       
       rn=random.randrange(40)+300
       cid=random.randrange(40)+10
       
       while rn in carno or cid in custid:
           rn=random.randrange(60)+300
           cid=random.randrange(60)+10
           
       rc.append(0)
       p.append(0)
       
       if p1 not in phno:
           phno.append(p1)
       elif p1 in phno:
           for n in range(0,i):
               if p1== phno[n]:
                   if p[n]==1:
                       phno.append(p1)
       elif p1 in phno:
           for n in range(0,i):
               if p1== phno[n]:
                   if p[n]==0:
                      print("\tPhone no. already exists and payment yet not done..!!")
                      name.pop(i)
                      add.pop(i)
                      bookedin.pop(i)
                      bookedout.pop(i)
                      Booking()                                              
       print(" ")
       print("\t\t\t\t***CAR BOOKED SUCCESSFULLY***\t\t\t\t")    
       print("CAR No. - ",rn)
       print("Customer Id - ",cid)
       carno.append(rn)
       custid.append(cid)
       i=i+1
       n=int(input("enter 3 for payment\n0-BACK\n-->>"))
       if n==0:
           Home()
       elif n==3:
           Payment()  
       else:
           exit()
           
  #------CAR INFO -----        
def CARS_Info():
    print(" 1). SEDAN CARS")
    print("\t Passengers - 5 ") 
    print("\t Air Bags- 2-5 ") 
    print("\tCARS-->Hyundai Verna,Honda City,Amaze,Vento,Ciaz ")  
    print("---Well maintained CARS,")
    print("---3 to 5 star feedback given by customer")
    
           
    print(" 2). SUV CARS")
    print("\t Passengers - 6-7 ") 
    print("\t Air Bags- 2-5 ") 
    print("\tCARS--> VITARA BREZZA , CRETA , FORTUNER,  ")  
    print("---Well maintained CARS,")
    print("---3 to 5 star feedback given by customer")
    
    print(" 3). COUPE CARS")
    print("\t Passengers - 2 ") 
    print("\t Air Bags- 4 ") 
    print("\tCARS--> BMW 2 Series Gran Coupe,NISSAN GTR ")  
    print("---Well maintained CARS,")
    print("---3 to 5 star feedback given by customer")  
    
    print(" 4). SPORTS CARS")
    print("\t Passengers - 2 ") 
    print("\t Air Bags- 4 ") 
    print("\tCARS--> FORD MUSTANG, BMW M3/M4, PORSHE 911, SUPRA ")  
    print("---Well maintained CARS,")
    print("---3 to 5 star feedback given by customer")                       
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit() 
        
        
        
#----------PAYMENT PROCESS-------
def Payment():
    
    ph=str(input("phone Number: ")) 
    global i 
    f=0
    
    for n in range(0,i):
        if ph==phno[n]:
            
            
            if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print(" MODE OF PAYMENT")
                print(" 1- Credit/Debit Card")
                print(" 2- Paytm/PhonePe")
                print(" 3- Using UPI")
                print(" 4- Cash")
                x=int(input("-> "))
                print("\n Amount: ",(price[n]*day[n])+rc[n])
                print("\n		 Pay For Nishi")
                print(" (yes/no)")
                ch=str(input("->"))                
                
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("		 CAR RENTAL")
                    print(" --------------------------------")
                    print("			 Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Booked-In: ",bookedin[n],"\t\n Booked-Out: ",bookedout[n],"\t")
                    print("\n CAR TYPE: ",car[n],"\t\n CAR Charges: ",price[n]*day[n],"\t")

                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("		 Thank You")
                    print("		 Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)


                    carno.pop(n)
                    custid.pop(n)
                    carno.insert(n,0)
                    custid.insert(n,0)
            else: 
                
                for j in range(n+1,i):
                    if ph==phno[j] :
                        if p[j]==0:
                            pass
                        else:
                            f=1
                            print("\n\t Payment has been made :) \n\t")  
    if f==0:
        print("Invalid Customer Id") 
        
    n=int(input("enter 4 for record\n0-BACK\n -->")) 
    if n==0:
        Home()
    elif n==4:
        Record()    
    else:
        exit()                                            

#--------RECORD FUNCTION-----------
def Record():
	
	# checks if any record exists or not
	if phno!=[]:
		print("	 *** CAR RECORD ***\n")
		print("| Name	 | Phone No. | Address	 | Booked-In | Booked-Out	 | CAR Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,i):
			print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",bookedin[n],"\t|",bookedout[n],"\t|",car[n],"\t|",price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No Records Found")
	n = int(input("0-BACK\n ->"))
	if n == 0:
		Home()
		
	else:
		exit()
           
Home()                    