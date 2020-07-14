def divideby42(denominator):
    try:
        return 42/denominator
    except:
        print("Error: you tried to divide by zero")    


print(divideby42(2))
print(divideby42(0))