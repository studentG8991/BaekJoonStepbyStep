x = int(input())
if x>1000 or x<-1000 or x==0: quit()
y = int(input())
if y>1000 or y<-1000 or y==0: quit()
if x>0 and y>0:print(1)
elif x<0 and y>0:print(2)
elif x<0 and y<0:print(3)
elif x>0 and y<0:print(4)