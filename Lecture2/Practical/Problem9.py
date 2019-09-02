import argparse
parser=argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("index1", type=int)
parser.add_argument("index2", type=int)
args=parser.parse_args()
print("\n The given text: %s \n Start index: %s \n End index: %s \n Output string: %s" 
%(args.text, args.index1, args.index2, args.text[args.index1:args.index2]))