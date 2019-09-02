import argparse
parser=argparse.ArgumentParser()
parser.add_argument("str", type=str)
args = parser.parse_args()
if len(args.str)%2==1 and len(args.str)>=7:
 mi=int(len(args.str)/2)
 text=args.str[(mi-1):(mi+2)]
 text2=args.str[:(mi-1)]+text.upper()+args.str[(mi+1):]
 print("\n","The old string:", args.str, "\n",
 "Middle 3 characters:", text, "\n",
 "The new string:", text2)
else:
    print("Enter other word")