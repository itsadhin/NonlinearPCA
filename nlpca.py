"""
Reimplementation of Nonlinear PCA by Matthias Scholz

Modified by Adhin 
"""

import numpy as np
import torch
import torch.nn as nn

class NLPCA():
    def __intit__(self,n_components):
        self.n_components = int(n_components)
        if n_components < 1:
            raise ValueError("Please enter a value greater than 1 for number of components")

