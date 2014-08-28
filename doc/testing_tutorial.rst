Introduction to LOTlib Testing framework
========================================


In order to make sure that new code doesn't break the main LOTlib functionality, as of Summer 2014 we've added a suite of tests for LOTlib. These are located in the LOTlibTest/ directory, and are based on Python's unittest module. So far, we've created simple tests for FunctionNode.py, FiniteBestSet.py, Grammar.py, and Miscellaneous.py.

Terminology:

* Each individual test is referred to as a test case (unittest.TestCase). Each test case is supposed to test one feature of the code.
* A bundle of individual tests is referred to as a test suite (unittest.TestSuite). Test suites are basically collections of test cases, and sometimes other test suites. They are supposed to test a collection of features in the code.

Running tests:

* To run a bundle of tests in a particular LOTlib testing file, execute the following command within the LOTlibTest/ directory:
    .. code:: sh

        $ python <file>.py
 where <file> is either FiniteBestSetTest, FunctionNodeTest, GrammarTest, or MiscellaneousTest.
* To run every test, execute:
    .. code:: sh

        $ python Test_LOTlib.py

Skipping tests: Sometimes it is convenient to not execute some tests when debugging. To skip a test, navigate to the file containing the testing code, go to the test case's header, and add "@" right before


.. helpful thing for rendering inline code
.. http://stackoverflow.com/questions/10870719/inline-code-highlighting-in-rest
.. role:: bash(code)
    :language: bash

.. role:: python(code)
    :language: python
