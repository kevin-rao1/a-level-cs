# written in Neovim to avoid AI
def mysteryFunction(X):
    Product = 1

    Factor = 0
    while Product < X:
        Factor += 1
        Product = Product * Factor
        #print(Factor, Product)
    #print("")
    if X == Product:
        Product = 1
        for N in range(1, Factor+1):
            Product = Product * N
            print(N)
    else:
        print("No result")

"""for X in range(2, 1000):
    print(f"{X}:", end="")
    mysteryFunction(X)"""

X = int(input("Enter an integer greater than 1: "))
mysteryFunction(X)