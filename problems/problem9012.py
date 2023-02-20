from sys import stdin
input=stdin.readline

# 참조: https://somjang.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if not self.isEmpty():
            pop_object=self.stack.pop()
        
        return pop_object
    def top(self):
        top_object=None
        if not self.isEmpty():
            top_object=self.stack[-1]
        
        return top_object
    
    def isEmpty(self):
        is_empty=False
        if len(self.stack)==0:
            is_empty=True

        return is_empty
    
    def getStack(self):
        get_stack=self.stack
        return get_stack
    
    def clear(self):
        self.stack=[]
    
stack=Stack()
n=int(input())
ans = [None]*n

for i in range(n):
    s=input().rstrip()
    for c in s:
        if c=='(':
            stack.push(c)
        elif c==')' and not stack.isEmpty():
            stack.pop()
        else:
            ans[i]='NO'
            break
    if ans[i]!=None:continue
    
    if stack.isEmpty():ans[i]='YES'
    else:
        stack.clear()
        ans[i]='NO'

for i in ans:
    print(i)