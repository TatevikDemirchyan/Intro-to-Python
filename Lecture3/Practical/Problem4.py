import argparse
list4=[50, 5, 10, 10, 20, 36, 45]
parser=argparse.ArgumentParser()
parser.add_argument("value", type=int)
args = parser.parse_args()
print(list4)
list4.remove(args.value)
print(list4)