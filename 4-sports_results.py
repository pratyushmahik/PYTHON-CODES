# WRITE A PROGRAM TO STORE THE SCORES/RESULTS OF 
# SPORTS TOURNAMENT USING LISTS AND TUPLES IN PYTHON :-)

# HERE WE HAVE CREATED A LIST NAMED SCORES AND STORED
# THE SCORES OF FIVE PLAYERS IN IT
scores=[56,89,100,69,84]

# NOW WE HAVE SORTED THE SCORES OF THE PLAYERS
# ON DESCENDING ORDER
scores.sort()
print(scores)
scores.reverse()
print(scores)

# NOW WE HAVE TO CONVERT THE SORTED LIST INTO TUPLE
scores_tuple=tuple(scores)
print(scores_tuple)

# NOW WE ARE UNPACKING THE TUPLE INTO SEPERATE 
# VARIABLES NAMED HIGHEST SCORE,LOWEST SCORE AND ASLO
# THE AVERAGE SCORE

highest,second,third,fourth,lowest=scores_tuple

print("THE HIGHEST SCORE IS :",highest)
print("THE LOWEST SCORE IS :",lowest)
print("THE AVERAGE SCORE IS :",round(sum(scores_tuple)/len(scores_tuple)))
# print("THE AVERAGE SCORE IS :",(scoredsum(highest+second+third+fourth+lowest/5))) #NOTE:WRONG CODE ASK MAM 