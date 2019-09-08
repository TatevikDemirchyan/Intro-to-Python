import argparse
parser=argparse.ArgumentParser()
parser.add_argument("value")
args=parser.parse_args()
set1 = {"Good morning", "50", "True", "orange"}
print(set1)
set1.remove(args.value)
print(set1)