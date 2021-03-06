#!/usr/bin/env python

from horton import *  # pylint: disable=wildcard-import,unused-wildcard-import


# Define Occupation model, expansion coefficients and overlap
# -----------------------------------------------------------
lf = DenseLinalgFactory(6)
occ_model = AufbauOccModel(3)
modelham = Hubbard(pbc=True)
orb = lf.create_expansion(6)
olp = modelham.compute_overlap(lf)


# One and two-body interaction terms
# ----------------------------------

# t-param, t = -1
hopping = modelham.compute_kinetic(lf, -1)
# U-param, U = 2
onsite = modelham.compute_er(lf, 2)


# Perform initial guess
# ---------------------
guess_core_hamiltonian(olp, hopping, orb)
terms = [
    RTwoIndexTerm(hopping, 'kin'),
    RDirectTerm(onsite, 'hartree'),
    RExchangeTerm(onsite, 'x_hf'),
]
ham = REffHam(terms)


# Do a Hartree-Fock calculation
# -----------------------------
scf_solver = PlainSCFSolver()
scf_solver(ham, lf, olp, occ_model, orb)


# CODE BELOW IS FOR horton-regression-test.py ONLY. IT IS NOT PART OF THE EXAMPLE.
rt_results = {
    'energy': ham.cache["energy"],
    'orb_energies': orb.energies,
    'kinetic': ham.cache["energy_kin"],
    'hartree': ham.cache["energy_hartree"],
    'exchange': ham.cache["energy_x_hf"],
}
# BEGIN AUTOGENERATED CODE. DO NOT CHANGE MANUALLY.
import numpy as np  # pylint: disable=wrong-import-position
rt_previous = {
    'energy': -5.0,
    'exchange': -2.9999999999999982,
    'hartree': 5.9999999999999964,
    'kinetic': -7.999999999999998,
    'orb_energies': np.array([
        -1.0000000000000007, -2.3948019172601905e-16, 1.2845788926350238e-16,
        1.9999999999999991, 2.0000000000000004, 2.9999999999999991
    ]),
}
