import io
import sys

_INPUT = """\
6
5 10
20
100
105
217
314
10 10
1
2
3
4
5
6
7
8
9
10
10 100000
3
31
314
3141
31415
314159
400000
410000
500000
777777
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,T=map(int,input().split())
  A=[int(input()) for _ in range(N)]
  ans=N*T
  for i in range(N-1):
    ans-=max(0,A[i]+T-A[i+1])
  print(ans)