import argparse
parser=argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()
a=args.text.lower().count("usa")
b=args.text.replace("usa", "Armenia")
c=b.replace("Usa", "Armenia")
d=c.replace("UsA", "Armenia")
e=d.replace("USa", "Armenia")
f=e.replace("uSa", "Armenia")
g=f.replace("uSA", "Armenia")
i=g.replace("usA", "Armenia")
j=i.replace("USA", "Armenia")
print("\n", "The given string: ", args.text, "\n",
"The USA count is: ", a, "\n",
"The new string: ", j)