
"""
        Define a new kind of LOTHypothesis, that gives regex strings.
        These have a special interpretation function that compiles differently than straight python eval.
"""

from LOTlib.Grammar import Grammar
from LOTlib.FunctionNode import isFunctionNode

from LOTlib.DataAndObjects import FunctionData
from LOTlib.Hypotheses.LOTHypothesis import LOTHypothesis
import re

##########################################################
# Define a grammar
grammar = Grammar()

grammar.add_rule('START', '', ['EXPR'], 1.0)

grammar.add_rule('EXPR', 'star_', ['EXPR'], 1.0)
grammar.add_rule('EXPR', 'question_', ['EXPR'], 1.0)
grammar.add_rule('EXPR', 'plus_', ['EXPR'], 1.0)
grammar.add_rule('EXPR', 'or_', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', 'str_append_', ['TERMINAL', 'EXPR'], 5.0)
grammar.add_rule('EXPR', 'terminal_', ['TERMINAL'], 5.0)

for v in 'abc.':
    grammar.add_rule('TERMINAL', v, None, 1.0)


##########################################################
# Map a tree to a regular expression

def to_regex(fn):
    """
            Custom mapping from a function node to a regular expression string (like, e.g. "(ab)*(c|d)" )
    """
    assert isFunctionNode(fn)

    if fn.name == 'star_':         return '(%s)*'% to_regex(fn.args[0])
    elif fn.name == 'plus_':       return '(%s)+'% to_regex(fn.args[0])
    elif fn.name == 'question_':   return '(%s)?'% to_regex(fn.args[0])
    elif fn.name == 'or_':         return '(%s|%s)'% tuple(map(to_regex, fn.args))
    elif fn.name == 'str_append_': return '%s%s'% (fn.args[0], to_regex(fn.args[1]))
    elif fn.name == 'terminal_':   return '%s'%fn.args[0]
    elif fn.name == '':            return to_regex(fn.args[0])
    else:
        assert False, fn

##########################################################
# Define some data

data = [ FunctionData(input=['aaaa'], output=True),\
         FunctionData(input=['aaab'], output=False),\
         FunctionData(input=['aabb'], output=False),\
         FunctionData(input=['aaba'], output=False),\
         FunctionData(input=['aca'],  output=True),\
         FunctionData(input=['aaca'], output=True),\
         FunctionData(input=['a'],    output=True) ]

##########################################################
# make_h0

def make_h0(value=None):
    return RegexHypothesis(grammar, value=value, ALPHA=0.999)


##########################################################
# Hypothesis

class RegexHypothesis(LOTHypothesis):
    """
            Define a special hypothesis for regular expressions. This requires overwritting value2function
            to use our custom interpretation model on trees -- not just simple eval.

            Note that this doesn't require any basic_primitives -- the grammar node names are used by
            to_regex to
    """
    def value2function(self, v):
        regex = to_regex(v)
        c = re.compile(regex)
        return (lambda s: (c.match(s) is not None))

    def __str__(self):
        return to_regex(self.value)