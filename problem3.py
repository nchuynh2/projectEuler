n = 600851475143;
prime = 2;
i = 2;
while n != 1:
    while (n%i) != 0:
        i = i + 1;
    prime = i;
    n = n / prime;
    i = i + 1;
print(prime)
