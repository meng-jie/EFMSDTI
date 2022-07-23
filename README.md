## paper "Drug-target interaction prediction based on multi-source data efficient fusion"


### Quick start
We provides an example script to run experiments with the fusion of networks and network features already extracted from our dataset:
- Run `main.py`: predict drug-target interactions, and evaluate the results with cross-validation.

### Experimental environment and version
We test the code on Ubuntu 20.04 with Matlab R2018a installed for fusion of networks and network embedding.
We test the code on Windows 10 with pycharm for predicting DTIs.
Operating system:Linux 5.11.0

### Code and data
#### `Compute_Entropy/` directory
Entropy was calculated for each network and the entropy-weighted drug target network was respectively. 


#### `predict/` directory
- `main.py`: Input features into the prediction model to predict DTIs.
- `test.py`: Calculate the mean score of the five fold crossover experiment.


#### `data/` directory
- `drug_dict.txt`: list of drug unique identifier and drug names
- `protein_dict.txt`: list of target unique identifier and target names
- `disease_dict.txt`: list of disease unique identifier and disease names
- `se_dict.txt`: list of side effect unique identifier and side effect names
- `drugdrug.txt`: DDI matrix
- `drugDisease.txt`: DD matrix
- `drugsideEffect.txt`: DSE  matrix
- `drugsim1network.txt`: SD<sub>C</sub>  matrix
- `drugsim2network.txt`: SD<SUB>ATC</SUB>  matrix
- `drugsim3network.txt`: SD<SUB>P</SUB>  matrix
- `drugsim4network.txt`: SD<SUB>BP</SUB>  matrix
- `drugsim5network.txt`: SD<SUB>CC</SUB>  matrix
- `drugsim6network.txt`: SD<SUB>MF</SUB>  matrix
- `proteinprotein.txt`: TTI matrix
- `proteinDisease.txt`: TD matrix
- `proteinsim1network.txt`: ST<SUB>P</SUB>  matrix
- `proteinsim2network.txt`: ST<SUB>BP</SUB>  matrix
- `proteinsim3network.txt`: ST<SUB>CC</SUB>  matrix
- `proteinsim4network.txt`: ST<SUB>MF</SUB>  matrix

#### ` fusion/` directory
We provided the pre-fused networks for drug and target, which were used to produce the results in our paper.

#### `feature/` directory
We provided the pre-trained vector representations for the fusion networks of drug and target.

#### `DNGR/` directory
This directory contains code necessary to run the DNGR algorithm.
- Run `main.m`: it will generate a low-dimensional vector representation of features for each node in the fused drug or target network.
