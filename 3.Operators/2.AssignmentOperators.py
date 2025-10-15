"""
+= x+=y  is same as x=x+y
-= x-=y  is same as x=x-y
*= x*=yi s same as x=x*y
/= x/=y is same as x=x/y
**= x**=y is same as x=x**y
%= x%=y is same as x=x%y
"""



# Assignment Operators
mom = "Sarah"
dad = "Abraham"

score1 = 100
score2 = 100

scoreboard = score1 + score2
print(scoreboard)

score1 = 100
score2 = 100

# score1 = score1 + score2
score1+=score2
print("Add:" , score1)

score1 = 100
score2 = 100

#score1 = score1 - score2
score1-=score2
print("Subtract:",  score1)

score1 = 100
score2 = 100

#score1 = score1 * score2
score1*=score2
print("Multiply:", score1)

score1 = 100
score2 = 100

#score1 = score1 / score2
score1/=score2
print("Division:", score1)


score1 = 100
score2 = 100

#score1 = score1 ** score2
score1**=score2
print("Exponential:",  score1)


score1 = 100
score2 = 100

#score1 = score1 % score2
score1%=score2
print("Modulo:",  score1)


