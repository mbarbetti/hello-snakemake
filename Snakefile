# Run with:
# snakemake all 


CHOICES = ["normal", "uniform", "exponential", "lognormal"]

rule sample_rule:
  input:
    script = "./scripts/sample_data.py"

  output:
    data = "./data/{distr}.npz"

  shell:
    "python3 {input.script} -d {wildcards.distr}"


rule plot_rule:
  input:
    script = "./scripts/plot_data.py" ,
    data = "./data/{distr}.npz"

  output:
    img = "./images/{distr}.png"

  shell:
    "python3 {input.script} -d {wildcards.distr}"

rule all:
  input:
    expand ("./images/{distr}.png", distr = CHOICES)

  output:
    ".all_images_exported"

  shell:
    "touch {output}"
