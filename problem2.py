term_a = 1;
term_b = 2;
term_c = 3;
total = 2;
while term_c < 4000000:
    term_a = term_b;
    term_b = term_c;
    term_c = term_a + term_b;
    if (term_c%2) == 0:
        total = total + term_c;
print(total)
