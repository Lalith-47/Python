import sys
try:
    signs=['+','-','*','%','//','/']
    if len(sys.argv)==4:
        first=int(sys.argv[1])
        last=int(sys.argv[3])
        sign=sys.argv[2]
        if sign not in signs:
            sys.exit(1)
        if sign=='+':
            print(f" Result: {first+last}")
        elif sign=='-':
            print(f" Result: {first-last}")
        elif sign=='*':
            print(f" Result: {first*last}")
        elif sign=='//':
            print(f" Result: {first//last}")
        elif sign=='/':
            print(f" Result: {first/last}")
        elif sign=='%':
            print(f" Result: {first%last}")
        else:
            print(f"Please Check The input")
    else:
        print(f"Arguments not matching")
        sys.exit(1)
except SystemExit as e:
    print(f"Exited with Code: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    print(f"Code execution completed")