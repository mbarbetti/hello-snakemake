import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

CHOICES = ["normal", "uniform", "exponential", "lognormal"]
RESOLUTION = 300

parser = ArgumentParser()
parser . add_argument ("-d", "--distribution", required = True, choices = CHOICES)
args = parser . parse_args()

npzfile = np.load (f"./data/{args.distribution}.npz")
rnd = npzfile["rnd"]

fig, ax = plt.subplots (figsize = (4,3), dpi = RESOLUTION)
ax.set_xlabel ("$x$", fontsize = 12)
ax.set_ylabel ("$f(x)$", fontsize = 12)
ax.hist (rnd, bins = 50, label = f"{args.distribution}")
ax.legend (fontsize = 10)

plt.tight_layout()
outfile = f"./images/{args.distribution}.png"
plt.savefig (outfile, format = "png", dpi = RESOLUTION)

print (f"Plot correctly exported to {outfile}")
