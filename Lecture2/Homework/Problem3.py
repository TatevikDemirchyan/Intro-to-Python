import argparse
parser=argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("word1")
parser.add_argument("word2")
args = parser.parse_args()
print("\n The given text: %s \n First word:  %s \n Second word: %s \n Output string: %s" 
% (args.text, args.word1, args.word2, args.text.replace(args.word1, args.word2)))