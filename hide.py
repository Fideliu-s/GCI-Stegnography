from stegano import lsb
import argparse

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--encode", "-e", help="hide text")
parser.add_argument("--decode", "-d", help="reveal text")

# read arguments from the command line
args = parser.parse_args()

if args.encode:
   text = input("Enter text to hide:")
   secret = lsb.hide(args.encode, text)
   secret.save(args.encode)
   print("Completed!")

elif args.decode:
   msg = lsb.reveal(args.decode)
   print(msg)
else:
   print("No argument passed")

