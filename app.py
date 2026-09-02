import sys
if len(sys.argv)!=4:
    print("Usage: python app.py <number1> <number2> <number3>")
    sys.exit(1)

M1=float(sys.argv[1])
M2=float(sys.argv[2])
M3=float(sys.argv[3])
t=M1+M2+M3
avg=t/3
print("subject 1: ",M1)
print("subject 2: ",M2)
print("subject 3: ",M3)
print("Total:",t)
print("Average:",avg)
if M1>=40 and M2>=40 and M3>=40:
    print("RESULT : PASS")
else:
    print("RESULT:FAIL")