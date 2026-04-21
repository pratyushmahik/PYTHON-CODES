# WRITE A PROGRAM TO FIND OUT WHETHER A STUDENT HAS PASSED OR FAILED 
# IF IT REQUIRES A TOTAL OF 40% AND ATLEAST 33% IN EACH SUBJECT 
# TO PASS.ASSUME 3 SUBJECTS AND TAKE MARKS AS AN INPUT FROM THE USER

phy=int(input("ENTER THE MARKS IN PHYSICS:"))
chem=int(input("ENTER THE AMRKS IN PHY :"))
maths=int(input("ENTER THE MARKS IN MATHS :"))
total_percentage=((phy+chem+maths)/300)*100

if(phy>33 and chem>33 and maths>33 and total_percentage>40):
    print("YOU PASSED THE EXAM",total_percentage)

else:
    print("YOU FAILED THE EXAM",total_percentage)