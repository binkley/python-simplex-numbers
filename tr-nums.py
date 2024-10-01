#!/usr/bin/env python
import argparse
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


def main():
    parser = argparse.ArgumentParser(
        description='Generate inverse triangular numbers and their gaps.'
    )
    parser.add_argument(
        '-d',
        '--dimension',
        type=int,
        default=2,
        help='triangular number dimension'
    )
    args = parser.parse_args()

    gen = inv_tr_nums(args.dimension)
    for num in islice(gen, N):
        print(num)
    print('---')
    gen = inv_gap_nums(args.dimension)
    for num in islice(gen, N + 1):
        print(num)


if __name__ == '__main__':
    main()
