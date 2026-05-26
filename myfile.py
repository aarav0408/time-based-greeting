import time
name=input("enter your name:")
Recenttime=time.strftime("%H:%M:%S")
recenttime=int(time.strftime("%H"))
c=name.capitalize()
if(4<=recenttime<12):
    print("GOOD MORNING",c,"its",Recenttime)
elif(12<recenttime<17):
    print("GOOD EVENING",c,"its",Recenttime)
else:
    print("GOOD NIGHT",c,"its",Recenttime)