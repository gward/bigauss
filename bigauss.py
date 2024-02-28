#!venv/bin/python

'''bigauss: divine overlapping Gaussian distributions in data'''

import argparse

import numpy
from sklearn import mixture


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    assert args.infile.readline().startswith('Elapsed Times (ms)')
    assert args.infile.readline().strip().split('\t') == ['STEP 1', 'STEP 2', 'STEP 3']

    distros = [[], [], []]
    for line in args.infile:
        values = [int(val) for val in line.split('\t')]
        for (idx, val) in enumerate(values):
            distros[idx].append(val)

    for (idx, samples) in enumerate(distros):
        summary = str(samples[:5])[1:-1] + ', ..., ' + str(samples[-3:])[1:-1]
        print(f'set {idx+1}: {summary}')
        samples = numpy.array(samples)
        mxt = mixture.GaussianMixture(n_components=2).fit(samples.reshape(-1, 1))
        means_hat = mxt.means_.flatten()
        weights_hat = mxt.weights_.flatten()
        sds_hat = numpy.sqrt(mxt.covariances_).flatten()

        print(f'  {mxt.converged_=}')
        print(f'  {means_hat=}')
        print(f'  {sds_hat=}')
        print(f'  {weights_hat=}')


main()
