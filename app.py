import sys
if len(sys.argv)!=3:
    print("usage python app.py<number1> <number2>")
    sys.exit(1)

    num1=float(sys.argv[1])
    num2=float(sys.argv[2])
    print("number 1: ",num1)
    print("number 2: ",num2)
    print("ADD: ",num1+num2)
    print("SUB: ",num1-num2)
    print("MUL: ",num1*num2)
    if num2!=0:
        print("Division",num1/num2)
    else:
        print("Division:cannot divide by zero")