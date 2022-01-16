def pyramid_of_stars():

    n = int(input("Enter height for pyramid : "))

    k = n-1           # for Inner looop side blank spaces

    for i in range(n):
        for j in range(k):
            print(end=" ")    #side blank spaces of pyramid
        
        k = k-1
        for l in range(i+1):
            print("* ",end="")  # pyramid stars
        
        print("\r")             # for new line
    
    
pyramid_of_stars()
