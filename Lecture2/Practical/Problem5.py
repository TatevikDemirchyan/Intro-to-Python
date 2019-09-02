import argparse
parser=argparse.ArgumentParser()
parser.add_argument("str")
args = parser.parse_args()
print("\n The given string: %s \n All lowercase: %s \n All uppercase: %s" % (args.str, args.str.lower(), args.str.upper()))