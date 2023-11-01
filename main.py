def chislo(num):
    if num/10>=1:
        num = chislo(sum([int(i) for i in str(num)]))
    else:
        return num
    if num/10<1:
        return num

print(chislo(38))
print(chislo(1))