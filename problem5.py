for a in range(20,1000000000,20):
    for b in range(1,11):
        if a%b != 0:
            break
        if b == 10:
            answer = a;
            print(answer)
            quit()
			