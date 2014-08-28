Introduction to LOTlib Testing framework
========================================


In order to make sure that new code doesn't break the main LOTlib functionality, as of Summer 2014 we've added a suite of tests for LOTlib. These are located in the LOTlibTest/ directory, and are based on Python's unittest module. So far, we've created simple tests for FunctionNode.py, FiniteBestSet.py, Grammar.py, and Miscellaneous.py.

Terminology:

* Each individual test is referred to as a test case (unittest.TestCase). Each test case is supposed to test one feature of the code.
* A bundle of individual tests is referred to as a test suite (unittest.TestSuite). Test suites are basically collections of test cases, and sometimes other test suites. They are supposed to test a collection of features in the code.
* For more information about terminology and about Python's built-in library for testing things, please visit the unittest_ documentation page.

Running tests:

* To run a bundle of tests in a particular LOTlib testing file, execute the following command within the LOTlibTest/ directory:
    .. code:: sh

        $ python <file>.py
 where <file> is either FiniteBestSetTest, FunctionNodeTest, GrammarTest, or MiscellaneousTest.
* To run every test, execute:
    .. code:: sh

        $ python Test_LOTlib.py

Skipping tests: Sometimes it is convenient to not execute some tests when debugging. To skip a test, navigate to the file containing the testing code, go to the test case's header, and add `@unittest.skip("<reason for skipping test>")` right before the function header. Replace <reason for skipping test> with a one-sentence description of why you are skipping the test case. For example, if you wanted to skip the `test_lp_regenerate_propose_to()` test in GrammarTest.py, we would want GrammarTest.py to look something like this:
    .. code:: python

        @unittest.skip('Dont need to run chi-squared test right now')
        def test_lp_regenerate_propose_to(self):

Adding a test:

* To make a test, navigate to the testing file you'd like to add test code for. Then define a new method that starts with "test_". For example, if you wanted to test the as_list() function in FunctionNode, you would want to add a method called test_aslist() in FunctionNodeTest.py.
* If you would like to add a test case in a new file (i.e. one that doesn't already exist in LOTlibTest), it's a good idea to let Test_LOTlib.py know. That way, your test will be included when testing all of LOTlib. To add a new file to Test_LOTlib.py, add the name of the file to the `tests` variable inside the test_all() function within Test_LOTlib.py. For example, if you wrote a test in FooTest.py, then Test_LOTlib.py would look something like this:
    .. code:: python

        # executes all tests within the LOTlibTest package
        def test_all():
            # a list of test modules we should execute
            tests = ['DataAndObjectsTest','FunctionNodeTest','GrammarTest','SubtreesTest','FiniteBestSetTest','GrammarRuleTest','MiscellaneousTest','ProposalsTest','FooTest'
                    # ,'ParsingTest' # we need the pyparsing module to do this test
            ]
* If you're having trouble writing test code, please refer to the list of assertions that the unittest library has here_.


.. _here: https://docs.python.org/2/library/unittest.html#assert-methods
.. _unittest: https://docs.python.org/2/library/unittest.html

.. helpful thing for rendering inline code
.. http://stackoverflow.com/questions/10870719/inline-code-highlighting-in-rest
.. role:: bash(code)
    :language: bash

.. role:: python(code)
    :language: python
