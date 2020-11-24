import numpy as np
import numpy.random as rnd
#################### 

##########
def spin_chain(length:int=100):
    """ Generate a spin chain of length 'length'"""
    return rnd.randint(0,2,length)

########## 
def flip(chain, pos):
    """ Flip spin state of chain at position 'pos'"""
    chain[pos] = (chain[pos] + 1)%2
    return chain

########## 
def flip_random_n(chain,n):
    """ Randomly flip n spin-states in the given spin chain"""
    for i in range(n):
        chain = flip(chain, rnd.randint(chain.size))
    return chain

########## 
def flip_random_n_v2(chain,n):
    """ Randomly flip n spin-states in the given spin chain"""
    # more efficient version
    index = rnd.randint(0,2,chain.size)
    return (chain + index)%2

##########
def external_interaction(chain, ext_field = 1.):
    """ Evaluate the energy of a chain in a presence of applied magnetic field"""
    # simple intereaction with external field
    # we know: ground state when all are aligned with the field.
    aux = interaction * 2*(chain-0.5).sum()
    return aux

##########
def z_interaction(chain, z_coeff = 1.):
    """ Evaluare the energy of chain in presence of nearest-neightbor 
    manetic moment interaction
    """
    spin_chain = (2*(0.5 - chain)).astype(int)
    return z_coeff*(spin_chain[:-1] * spin_chain[1:]).sum()

########## 
def anneal(chain, iterations, cooling_rate):
    temperature = float(chain.size)
    while temperature > 0.5:
        min_energy = z_interaction(chain)
        for i in range(iterations):
            disturbed_chain = flip_random_n(chain, round(temperature))
            new_energy = z_interaction(disturbed_chain)
            if new_energy < min_energy:
                min_energy, new_chain = new_energy, disturbed_chain
        new_energy, chain = min_energy, new_chain
        temperature = temperature / cooling_rate
        print(temperature, chain, min_energy)
    return chain
