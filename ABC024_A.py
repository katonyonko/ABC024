import io
import sys

_INPUT = """\
6
100 200 50 20
40 10
400 1000 400 21
10 10
400 1000 400 20
10 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C,K=map(int,input().split())
  S,T=map(int,input().split())
  ans=A*S+B*T
  if S+T>=K: ans-=C*(S+T)
  print(ans)