def sort1(s):
    s1=[a for a in s if a < 0]
    s2=[b for b in s if b >= 0]
    return s1 + s2

li=list(map(int, input().split()))
r=sort1(li)
print(*r)
