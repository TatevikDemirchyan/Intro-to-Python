import sys
set1 = {"Good morning", 50, True}
print(set1)
set1.update(sys.argv[1:])
print(set1)