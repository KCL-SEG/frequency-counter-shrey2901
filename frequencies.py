"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for value in items.items():
        if value in frequencies.keys():
            frequencies[value] += 1
        else:
            frequencies[value] = 1
    return frequencies
