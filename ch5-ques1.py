# WRITE A PROGRAM TO CREATE A DICTIONARY OF HINDI WORDS WITH VALUES 
# AS THEIR ENGLISH TRANSLATION.PROVIDE USER WITH AN OPTION 
# TO LOOK IT UP !!!

# words={
#     "gaadi":"car",
#     "kursi":"chair",
#     "chappal":"footwear",
#     "mata ji":"mummy",
#     "papaji":"papa",
#     "dadi":"grandmother"
# }
# print(words.items())
# # print(words)

words={
    "MATAJI":"MUMMY",
    "MADAT":"HELP",
    "KURSI":"CHAIR",
    "GAADI":"CAR"
}
word=input("ENTER THE WORD YOU WANT TO KNOW THE MEANING OF :")
print(words[word])

# NOTE: IF THE WORD YOU SEARCHED FOR DOESNT EXISTS IN THE
# DICTIONARY THEN IT WILL GIVE AN ERROR