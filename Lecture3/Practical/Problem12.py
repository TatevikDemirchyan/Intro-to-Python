import argparse
parser=argparse.ArgumentParser()
parser.add_argument("number", type=int)
args=parser.parse_args()
set3={4,5,7,6,2,4,6,7,10}
if args.number > min(set3) and args.number < max(set3):
  print(True)
else:
    print(False)