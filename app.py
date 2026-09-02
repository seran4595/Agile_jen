if len(sys.argv)!=3:
    print("usage python app.py<number1> <number2>")
    sys.exist(1)

    num1=float(sys.argv[1])
    num2=float(sys.argv[2])
    result=num1+num2
    print("number 1: ",num1)
    print("number 2: ",num2)
    print("sum: ",result)