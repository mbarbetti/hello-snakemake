# Hello world, snakemake! 🐍
Simple implementation of snakemake to sample and plot data

### Contents
1. Rule `sample-rule`
  * Produces .npz file containing data sampled accordingly to {'normal', 'uniform', 'exponential', 'lognormal'} distribution

2. Rule `plot-rule`
  * Produces a histogram figure filled with the data sampled by the previous snakemake rule

3. Rule `all`
  * Produces all the .npz files and the histogram figures 

### Dependencies
`hello-snakemake` requires:
* snakemake
* NumPy
* Matplotlib

### Running example
```shell
snakemake all --forceall
```