"""
The Plugboard class you will implement, will:

Take a list of wire pairs at construction in the form of a string,
with a default behaviour of no wires configured.
E.g. "ABCD" would wire A <-> B and C <-> D.
Validate that the wire pairings are legitimate. Raise an exception if not.
Implement the process method to translate a single character
input into an output.

Examples

plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
plugboard.process("A") ==> "B"
plugboard.process("B") ==> "A"
plugboard.process("X") ==> "X"
plugboard.process(".") ==> "."
"""

import re
class Plugboard(object):
    def __init__(self, wires=''):
        if len(wires)>20 or len(wires)%2!=0 or len(set(wires))!=len(wires):
            raise Exception("Bad wiring")
        else:
            self.dct_to = dict(re.findall(r'(?i)([a-z][a-z])',
                               wires[:20]))#+wires[:20][::-1]))
            self.dct_from = dict(re.findall(r'(?i)([a-z][a-z])',
                                 wires[:20][::-1]))#+wires[:20][::-1]))
        pass


    def process(self, c):
        """
        c: The single character to process
        """
        if c in self.dct_to.keys():
            return self.dct_to[c]
        elif c in self.dct_from.keys():
            return self.dct_from[c]
        else:
            return c
