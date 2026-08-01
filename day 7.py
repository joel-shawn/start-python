# Jump statements
"""
break-stop
continue-skip
pass-placeholder
return(function)
"""
if 24==24:
    pass

print("welcome")

for x in range(1,11):
    if x==6:
        break
    print(x,end=" ")

for y in range(1, 11):
    if y==4 or y==8:
        continue
    print (y, end=" ")