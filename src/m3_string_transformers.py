"""
This exercise specifies a bunch of ** StringTransformer ** classes,
each of which has only:
  -- The constructor method  __init__  with whatever parameters it needs
  -- A  transform  method that takes a string and "transforms" it,
       returning the transformed string.

The exercise provide practice at determining what INSTANCE VARIABLES
are necessary in a class definition.  It is based on an exercise
originally designed by Lynn Andrea Stein.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    # Uncomment these one-by-one as you do the testing.
    run_test_NameDropper()
    run_test_Censor()
    run_test_Counter()
    run_test_SlowThinker()


###############################################################################
# TODO: 2.  WITH YOUR INSTRUCTOR, read:
#   -- the description of ** StringTransformers **
#        in the doc-string at the top of this file
#   -- the NameDropper class definition below
#   -- the run_test_NameDropper function below the class definition.
#  After you UNDERSTAND what a StringTransformer is and the structure
#  of the exercises in this module, change the above _TODO_ to DONE.
###############################################################################
class NameDropper:
    """
    A NameDropper has a name (string) associated with it.
    Its   transform   method transforms the phrase that it is given by putting
       "BLAH says "
    in front of the phrase, where BLAH is the name associated with the NameDropper.
    Example:
           elsa = NameDropper("Elsa")
           elsa.transform("Robots are fun.")
              returns     "Elsa says Robots are fun."
    """
    def __init__(self, name_to_drop):
        self.name = name_to_drop

    def transform(self, phrase):
        return "{} says {}".format(self.name, phrase)


def run_test_NameDropper():
    """ Tests the   NameDropper   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   NameDropper  class:')
    print('--------------------------------------------------')

    format_string = '    <NameDropper>.transform( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    ##############################
    # Code used for all the tests:
    ##############################
    elsa = NameDropper("Elsa")
    sarah = NameDropper("Sarah")

    # Test 1:
    phrase = "Robots are fun."
    expected = "Elsa says Robots are fun."
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    phrase = "Crayons are fun too."
    expected = "Elsa says Crayons are fun too."
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    phrase = "You make me happy."
    expected = "Sarah says You make me happy."
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = sarah.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    phrase = "I am unsure about rocks."
    expected = "Elsa says I am unsure about rocks."
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###############################################################################
# TODO: 3. With your instructor, implement and test the Censor class (below).
#          We have written tests for you (below).
#   HINT:  Throughout, use string methods to do all the heavy lifting.
#   Type        ""  then  DOT      like this:  "".
#   and PAUSE to let the DOT trick show you string methods.
###############################################################################
class Censor:
    """
    A Censor has a character (string) associated with it,
    that defaults to the character "e".
        HINT: Google for "python default parameter" to learn
        how to use parameters with default values.
    Its   transform   method transforms the phrase that it is given
    by replacing each occurrence of its character with an asterisk ("*").
    Examples:
           elsa = Censor("a")
           elsa.transform("Cats are naturally lazy")
              returns     "C*ts *re n*tur*lly l*zy"

           sarah = Censor()
           sarah.transform("Tweedledee and Tweedledum")
               returns     "Tw**dl*d** and Tw**dl*dum"
    """
    def __init__(self, character_to_censure="e"):
        self.character_to_censure = character_to_censure

    def transform(self, phrase):
        return phrase.replace(self.character_to_censure, "*")


def run_test_Censor():
    """ Tests the   Censor   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   Censor  class:')
    print('--------------------------------------------------')

    format_string = '    <Censor>.transform( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    ##############################
    # Code used for all the tests:
    ##############################
    elsa = Censor("a")
    sarah = Censor()
    bob = Censor("!")

    # Test 1:
    phrase = "Alice in Wonderland"
    expected = "Alice in Wonderl*nd"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    phrase = "Tweedledee and Tweedledum"
    expected = "Tw**dl*d** and Tw**dl*dum"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = sarah.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    phrase = "eeaaee!!"
    expected = "eeaaee**"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    phrase = "Cats are naturally lazy"
    expected = "C*ts *re n*tur*lly l*zy"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###############################################################################
# TODO: 4. Implement and test the Counter class (below).
#          We have written tests for you (below).
###############################################################################
class Counter:
    """
    A Counter's transform  method transforms the phrase that it is given
    by putting a number in front of the phrase, that goes 1, 2, 3, ...
    Examples:
           elsa = Counter()
           bob = Counter()

           elsa.transform("Hello")         returns "1. Hello"
           elsa.transform("Goodbye")       returns "2. Goodbye"
           bob.transform("This is Bob")    returns "1. This is Bob"
           elsa.transform("Sing for me")   returns "3. Sing for me"
    """
    def __init__(self):
        self.counter = 0

    def transform(self, phrase):
        self.counter = self.counter + 1
        return "{}. {}".format(self.counter, phrase)


def run_test_Counter():
    """ Tests the   Counter   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   Counter  class:')
    print('--------------------------------------------------')

    format_string = '    <Counter>.transform( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    ##############################
    # Code used for all the tests:
    ##############################
    bob = Counter()
    alice = Counter()

    # Test 1:
    phrase = "Hello"
    expected = "1. Hello"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    phrase = "Goodbye"
    expected = "2. Goodbye"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    phrase = "Sing for me"
    expected = "3. Sing for me"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    phrase = "This is Alice"
    expected = "1. This is Alice"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = alice.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    phrase = "This is Bob again"
    expected = "4. This is Bob again"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###############################################################################
# TODO: 5. Implement and test the SlowThinker class (below).
#          We have written tests for you (below).
###############################################################################
class SlowThinker:
    """
    A SlowThinker's transform  method transforms the phrase it is given into
    the phrase that it was PREVIOUSLY given.  It returns "START" the first time.

           elsa = SlowThinker()
           bob = SlowThinker()
           elsa.transform("Hello")           returns "START"
           elsa.transform("Goodbye")         returns "Hello"
           elsa.transform("Sing for me")     returns "Goodbye"
           bob.transform("Interruption")     returns "START"
           elsa.transform("What is next?")   returns "Sing for me"
           bob.transform("Not yet")          returns "Interruption"
    """
    def __init__(self):
        self.next_phrase = "START"

    def transform(self, phrase):
        current_phrase = self.next_phrase
        self.next_phrase = phrase
        return current_phrase


def run_test_SlowThinker():
    """ Tests the   SlowThinker   class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SlowThinker  class:')
    print('--------------------------------------------------')

    format_string = '    <SlowThinker>.transform( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    ##############################
    # Code used for all the tests:
    ##############################
    elsa = SlowThinker()
    bob = SlowThinker()

    # Test 1:
    phrase = "Hello"
    expected = "START"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    phrase = "Goodbye"
    expected = "Hello"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    phrase = "Sing for me"
    expected = "Goodbye"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    phrase = "Interruption"
    expected = "START"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    phrase = "What is next?"
    expected = "Sing for me"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = elsa.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    phrase = "Not yet"
    expected = "Interruption"
    print_expected_result_of_test([phrase], expected, test_results,
                                  format_string)
    actual = bob.transform(phrase)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
