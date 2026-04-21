# WRITE A PROGRAM TO GREET ALL THE PERSON NAMES STORED IN A LIST "l"
# AND WHICH STARTS WITH S


l=["HARRY","SOHAM","SACHIN","RAHUL"]
i=0 
for name in l:
    if(name.startswith("S")):
        print(f"HELLOWW {name}")



# THIS PROGRAM WILL GREET THE PEOPLE WHOSE NAME STARTS WITH S OR R.... 
l=["HARRY","SOHAM","SACHIN","RAHUL"]
i=0 
for name in l:
    if(name.startswith("S") or name.startswith("R")):
        print(f"HELLOWW {name}")
        