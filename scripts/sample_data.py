import numpy as np
from argparse import ArgumentParser

SIZE = 10000
CHOICES = ["normal", "uniform", "exponential", "lognormal"]

parser = ArgumentParser()
parser . add_argument ("-d", "--distribution", required = True, choices = CHOICES)
args = parser . parse_args()

if args.distribution == "normal":
  rnd = np.random.normal (size = SIZE)
elif args.distribution == "uniform":
  rnd = np.random.uniform (size = SIZE)
elif args.distribution == "exponential":
  rnd = np.random.exponential (size = SIZE)
elif args.distribution == "lognormal":
  rnd = np.random.lognormal (size = SIZE)

outfile = f"./data/{args.distribution}.npz"
np.savez (outfile, rnd = rnd)

print (f"Data correctly exported to {outfile}")
