import sys
sys.path.append('../')
import numpy as np
import lkl.likelihoods as lkl

a = [1.,3.,1.,2.,2.]
b = [2.,2.,2.,2.,2.]
mu=np.ones(5)
c = np.diag([1.,1.,1.,1.,1.])

print lkl.TS(a,b,mu,'Poisson',c)
