import io
import sys

_INPUT = """\
6
15
35
21
126
252
210
144949225
545897619
393065978
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=10**9+7
  A=int(input())
  B=int(input())
  C=int(input())
  r=(B*C-A*C)*pow((A-C)*B+A*C,mod-2,mod)%mod
  c=(B*C-A*B)*pow((A-B)*C+A*B,mod-2,mod)%mod
  print(r,c)