
"""
        An example of inference over first-order logical expressions.
        Here, we take sets of objects and generate quantified descriptions
"""

from LOTlib.Miscellaneous import unique
from LOTlib.Grammar import Grammar
from LOTlib.Hypotheses.LOTHypothesis import LOTHypothesis

grammar = Grammar()

grammar.add_rule('START', '', ['QUANT'], 1.0)

# Very simple -- one allowed quantifier
grammar.add_rule('QUANT', 'exists_', ['FUNCTION', 'SET'], 1.00)
grammar.add_rule('QUANT', 'forall_', ['FUNCTION', 'SET'], 1.00)

# The thing we are a function of
grammar.add_rule('SET', 'S', None, 1.0)

# And allow us to create a new kind of function
grammar.add_rule('FUNCTION', 'lambda', ['BOOL'], 1.0, bv_type='OBJECT')
grammar.add_rule('BOOL', 'and_', ['BOOL', 'BOOL'], 1.0)
grammar.add_rule('BOOL', 'or_', ['BOOL', 'BOOL'], 1.0)
grammar.add_rule('BOOL', 'not_', ['BOOL'], 1.0)

# non-terminal arguments get passed as normal python arguments
grammar.add_rule('BOOL', 'is_color_',  ['OBJECT', '\'red\''],   5.00) # --> is_color_(OBJECT, 'red') --> OBJECT.color == 'red'
grammar.add_rule('BOOL', 'is_color_',  ['OBJECT', '\'blue\''],  5.00)
grammar.add_rule('BOOL', 'is_color_',  ['OBJECT', '\'green\''], 5.00)


#grammar.add_rule('BOOL', 'applylambda', ['BOOL'], 1.0, bv_type='OBJECT')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Just generate from this grammar
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#for i in xrange(100):
        #print grammar.generate()

# Or we can make them as hypotheses (functions of S):
#for i in xrange(100):
        #print LOTHypothesis(grammar, args=['S'])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Or real inference:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from LOTlib.DataAndObjects import FunctionData, Obj # for nicely managing data
from LOTlib.Inference.MetropolisHastings import mh_sample # for running MCMC


# Make up some data -- here just one set containing {red, red, green} colors
data = [ FunctionData(input=[ {Obj(color='red'), Obj(color='red'), Obj(color='green')} ], \
                      output=True) ]

# Create an initial hypothesis
h0 = LOTHypothesis(grammar, args=['S'])

# OR if we want to specify and use insert/delete proposals
#from LOTlib.Proposals import *
#h0 = LOTHypothesis(grammar, proposal_function=MixtureProposal(grammar, [RegenerationProposal(grammar), InsertDeleteProposal(grammar)] ) )

if __name__ == "__main__":
        
    # MCMC!
    for h in mh_sample(h0, data, 4000): # run sampler
    #for h in unique(mh_sample(h0, data, 4000)): # get unique samples
            # hypotheses' .prior, .likelihood, and .posterior_score are set in mh_sample
        print h.likelihood, h.prior, h.posterior_score, h
