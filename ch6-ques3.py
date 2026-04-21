# A SPAM COMMENT IS DEFINED AS A TEXT CONTAINING FOLLOWING KEYWORDS:
# "MAKE A LOT OF MONEY","BUY NOW","SUBSCRIBE THIS","CLICK THIS",
# WRITE A PROGRAM TO DETECT THESE SPAMS...

comment=input("ENTER YOUR COMMENT :")

p1="MAKE A LOT OF MONEY"
p2="BUY NOW"
p3="SUBSCRIBE THIS"
p4="CLICK THIS"

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("SPAM COMMENT")
else:
    print("NOT A SPAM COMMENT")    
