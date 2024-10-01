#!/usr/bin/env python

from fractions import Fraction
from itertools import islice

# from scipy.special import beta
from scipy.special import gamma


def inv_tr_nums(d=2):
    n = 1
    while True:
        # yield d * beta(n, n + d)
        yield 1 / Fraction((gamma(n + d) / (gamma(n) * gamma(d + 1))))
        n += 1


def inv_gap_nums(d=2):
    x = -1
    gen_inv_tr_nums = inv_tr_nums(d)
    while True:
        x += next(gen_inv_tr_nums)
        yield x


N = 10

gen = inv_tr_nums()
for num in islice(gen, N):
    print(num)

print('---')
gen = inv_tr_nums(3)
for num in islice(gen, N):
    print(num)

print('---')
gen = inv_gap_nums()
for num in islice(gen, N):
    print(num)

print('---')
gen = inv_gap_nums(3)
for num in islice(gen, N):
    print(num)
