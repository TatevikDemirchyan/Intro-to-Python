import sys
list1=["hello", 1, True]
new_list1=list1.copy()
new_list1.extend(sys.argv[1:])
print("\n", "list1:", list1, "\n",
"new_list1:", new_list1)