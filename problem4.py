palindrome = 0;
for a in range(1,1000):
    for b in range(1,1000):
        product = a*b;
        string = str(product);
        if string == string[::-1] and product > palindrome:
            palindrome = product;
print(palindrome)
