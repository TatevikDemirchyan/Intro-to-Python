import argparse
list2=[400, 5, 10, 10, 20, 36, 45]
parser=argparse.ArgumentParser()
parser.add_argument("value", type=int)
args = parser.parse_args()
a=list2.count(args.value)
print("\n list2= %s \n Number of %ss =%s" % (list2, args.value, a))