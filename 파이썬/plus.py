import sys

if sys.argv[1].isdigit() and sys.argv[2].isdigit():
    op1=int(sys.argv[1])
    op2=int(sys.argv[2])
    result=op1+op2
    print(f'{op1}+ {op2} = {result}')   
