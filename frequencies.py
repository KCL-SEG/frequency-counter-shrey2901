"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for value in items:
        if value in frequencies.keys():
            frequencies[value] += 1
    return frequencies
