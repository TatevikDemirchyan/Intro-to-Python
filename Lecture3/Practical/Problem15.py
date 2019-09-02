import argparse
parser=argparse.ArgumentParser()
parser.add_argument("key", type=str)
parser.add_argument("value", type=str)
args = parser.parse_args()
dict1={"Monday":"1", "Sunday":"7"}
print(dict1)
dict1[args.key] = args.value
print(dict1)