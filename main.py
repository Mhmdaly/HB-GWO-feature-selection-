"""
HB-GWO Feature Selection Algorithm
Author: Mohammed Aly
"""

import numpy as np

# BOA Parameters
BOA_params = {
    "sensory_modality": 0.01,  # c
    "power_exponent": 0.1,     # a
    "switch_probability": 0.8  # p
}

# GWO Coefficients are computed dynamically:
def compute_A_C(a):
    r1, r2 = np.random.rand(), np.random.rand()
    A = 2 * a * r1 - a
    C = 2 * r2
    return A, C

# HB-GWO General Parameters
HB_GWO_config = {
    "population_size": 30,
    "max_iterations": 200,
    "switching_decay_alpha": 0.65,
    "fitness_weight_lambda": 0.75,
    "random_forest_n_estimators": 100
}

if __name__ == "__main__":
    print("HB-GWO Parameters:")
    print("BOA:", BOA_params)
    print("GWO Example A/C:", compute_A_C(2))
    print("HB-GWO Config:", HB_GWO_config)
