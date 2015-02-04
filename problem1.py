multiple_3 = 3;
total_3 = 0;
while multiple_3 < 1000:
    if (multiple_3 % 5) != 0:
        total_3 = total_3 + multiple_3;
        multiple_3 = multiple_3 + 3;
    else:
        multiple_3 = multiple_3 + 3;

multiple_5 = 5;
total_5 = 0;
while multiple_5 < 1000:
    total_5 = total_5 + multiple_5;
    multiple_5 = multiple_5 + 5;

answer = total_3 + total_5;
print(answer)
