import io
import sys

_INPUT = """\
6
10 10 3
1 5
3 6
7 10
5 8
4 4
1 4
2 9
1 3
1 1
4 5
1 6
2 7
10 1
10 10 4
1 2
2 4
3 6
4 8
5 10
9 10
7 8
5 6
3 5
1 3
10 1
3 8
2 4
1 3
314159265 10 1
1 10000
500 12031
1414 113232
111111 777777
666661 23423423
12345678 123456789
111111111 314159265
112334 235235235
1 223445
314 1592
1 314159265
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,D,K=map(int,input().split())
  lr=[list(map(int,input().split())) for _ in range(D)]
  for i in range(K):
    s,t=map(int,input().split())
    ans=0
    for j in range(D):
      ans+=1
      l,r=lr[j]
      if l<=s<=r:
        if l<=t<=r: break
        else:
          if s<t: s=r
          else: s=l
    print(ans)