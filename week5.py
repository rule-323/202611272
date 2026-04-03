for dan in range(2, 10):
    print("#  %d단  #" % dan, end="\t")
print()

for num in range(1, 10):
    for dan in range(2, 10):
        print("%dX %d= %2d" % (dan, num, dan*num), end="\t")
    print()