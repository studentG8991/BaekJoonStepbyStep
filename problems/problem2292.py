'''
1 2 9 22 41 66
 1 7 13 19 25
  6 6  6  6
1 7 19 37 61
 6 12 18 24
  6  6  6
2~7까지 1칸, 8~19까지 2칸, 20~37까지 3칸...
'''

n = int(input())
if n>1000000000 or n<1:quit()
a=1
cnt=1
while n>a:
    a+=6*cnt
    cnt+=1
print(cnt)