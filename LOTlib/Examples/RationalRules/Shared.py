"""
        Shared functions for all RationalRules examples
"""

from LOTlib.Miscellaneous import q

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set up our grammar. DNF defautly includes the logical connectives
# in disjunctive normal form, but we need to add predicates to it.

from LOTlib.DefaultGrammars import DNF
grammar = DNF

# Two predicates for checking x's color and shape
# Note: per style, functions in the LOT end in _
grammar.add_rule('PREDICATE', 'is_color_', ['x', 'COLOR'], 1.0)
grammar.add_rule('PREDICATE', 'is_shape_', ['x', 'SHAPE'], 1.0)

# Some colors/shapes each (for this simple demo)
# These are written in quotes so they can be evaled
grammar.add_rule('COLOR', q('red'), None, 1.0)
grammar.add_rule('COLOR', q('blue'), None, 1.0)
grammar.add_rule('COLOR', q('green'), None, 1.0)
grammar.add_rule('COLOR', q('mauve'), None, 1.0)

grammar.add_rule('SHAPE', q('square'), None, 1.0)
grammar.add_rule('SHAPE', q('circle'), None, 1.0)
grammar.add_rule('SHAPE', q('triangle'), None, 1.0)
grammar.add_rule('SHAPE', q('diamond'), None, 1.0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Make up some data
# Let's give data from a simple conjunction (note this example data is not exhaustive)

from LOTlib.DataAndObjects import FunctionData, Obj

# FunctionData takes a list of arguments and a return value. The arguments are objects (which are handled correctly automatically
# by is_color_ and is_shape_
data = [ FunctionData( [Obj(shape='square', color='red')], True), \
         FunctionData( [Obj(shape='square', color='blue')], False), \
         FunctionData( [Obj(shape='triangle', color='blue')], False), \
         FunctionData( [Obj(shape='triangle', color='red')], False), \
         ]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Other standard exports

from LOTlib.Hypotheses.RationalRulesLOTHypothesis import RationalRulesLOTHypothesis

def make_h0(value=None):
    return RationalRulesLOTHypothesis(grammar=DNF, value=value, rrAlpha=1.0)


if __name__ == "__main__":
    
    from LOTlib.Inference.MetropolisHastings import MHSampler
    
    for h in MHSampler(make_h0(), data):
        print h