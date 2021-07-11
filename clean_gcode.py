import argparse
import os
import yaml

to_remove = [
    "I",
    "J",
    "K"
]

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input",
    type=str,
    help="Path to a gcode file to clean."
)


args = parser.parse_args()
if __name__ == "__main__":
    inputfile = args.input
    outputfile, _ = os.path.splitext(inputfile)
    outputfile += "_clean.nc"
    with open(outputfile, "w") as outf:
        with open(args.input, "r") as inputf:
            for line in inputf:
                keep = True
                for removal in to_remove:
                    if removal in line:
                        keep = False
                if keep:
                    outf.write(line)
