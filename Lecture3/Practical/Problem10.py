import argparse
parser=argparse.ArgumentParser()
parser.add_argument("value")
args=parser.parse_args()
set1 = {"Good morning", "50", "True", "orange"}
print(set1)
if args.value in set1:
 set1.remove(args.value)
 print(set1)
else:
    print("your value is not in set")