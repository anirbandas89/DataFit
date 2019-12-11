import sys
import numpy as np

#---------------------------------------------
# chi square
def chi_sq(d,mu,cov):
    d, mu, cov = np.asarray(d), np.asarray(mu), np.asarray(cov)
    if len(d) != len(mu):
        print 'Lengths of data and theory arrays should match!'
        sys.exit()
    a = d-mu
    return np.dot(a, np.dot(np.linalg.inv(cov), a))

# Gaussian or Normal likelihood
def NormalLikelihood(d,mu,cov):
    return np.exp(-chi_sq(d,mu,cov)/2.)

# Poisson likelihood
def PoissonLikelihood(d,mu):
    d, mu = np.asarray(d), np.asarray(mu)
    if len(d) != len(mu):
        print 'Lengths of data and theory arrays should match!'
        sys.exit()
    N_exp = np.sum(mu)
    b = 1.
    for i, count in enumerate(d):
        b *= (mu[i]**count)/np.math.factorial(count)
    return np.exp(-N_exp) * b

# Test statistics
def TS(d,b,mu,likelihood_type,cov):
    d, b, mu = np.asarray(d), np.asarray(b), np.asarray(mu)
    if likelihood_type in ('Poisson', 'poisson'):
        return -2.*np.log(PoissonLikelihood(b,mu)/PoissonLikelihood(d,mu))
    elif likelihood_type in ('Normal', 'normal', 'Gaussian', 'gaussian'):
        cov = np.asarray(cov)
        return -2.*np.log(NormalLikelihood(b,mu,cov)/NormalLikelihood(d,mu,cov))
    else:
        print 'Likelihood has to be either Poisson or Gaussian.'
        sys.exit()


