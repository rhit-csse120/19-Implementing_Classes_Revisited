"""
This exercise specifies a bunch of classes, each of which has only:
  -- The constructor method  __init__  with whatever parameters it needs
  -- A  transform  method that takes a string and "transforms" it,
       returning the transformed string.

The exercise provide practice at determining what INSTANCE VARIABLES
are necessary in a class definition.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
"""
A NameDropper has a name (string) associated with it.
Its   transform   method transforms the phrase that it is given by putting     
   "BLAH says "
in front of the phrase, where BLAH is the name associated with the NameDropper.

       elsa = NameDropper("Elsa")
       elsa.transform("Robots are fun.")
          returns     "Elsa says Robots are fun."

Here are some examples that you can use for testing:
       elsa = NameDropper("Elsa")
       sarah = NameDropper("Sarah")
       a = elsa.transform("Robots are fun.")
       b = elsa.transform("Crayons are fun too.")
       c = sarah.transform("You make me happy.")
       d = elsa.transform("I am unsure about rocks.")
       print(a, b, c, d, sep="\n")

       prints:
           Elsa says Robots are fun.
           Elsa says Crayons are fun too.
           Sarah says You make me happy.
           Elsa says I am unsure about rocks.
"""


# TODO: 2. Live code with your instructor
#       Implement the NameDropper class and add some code that tests it.
###############################################################################


###############################################################################
""" 
A Censor has a character (string) associated with it, that defaults to the
character "e". (HINT: Google for "python default parameter" to learn 
how to use parameters with default values.)
Its   transform   method transforms the phrase that it is given
by replacing each occurrence of its character with an asterisk ("*").

       elsa = Censor("a")
       elsa.transform("Cats are naturally lazy")
          returns     "C*ts *re n*tur*lly l*zy"
       
       sarah = Censor()
       sarah.transform("Tweedledee and Tweedledum")
           returns     "Tw**dl*d** and Tw**dl*dum"
           
Here are some examples that you can use for testing:
       elsa = Censor("a")
       sarah = Censor()
       a = elsa.transform("Alice in Wonderland")
       b = sarah.transform("Tweedledee and Tweedledum")
       c = sarah.transform("eeaaee!!")
       d = elsa.transform("Cats are naturally lazy")
       print(a, b, c, d, sep="\n")
       
       prints:
           Alice in Wonderl*nd
           Tw**dl*d** and Tw**dl*dum
           **aa**!!
           C*ts a*e n*tur*lly l*zy
"""


# TODO: 3. Implement the Censor class and add some code that tests it.
#       *** READ THIS HINT: ***
#   HINT:  Throughout, use string methods to do all the heavy lifting.
#   Type        "" then DOT           or, if you prefer,  "xxx" then DOT
#   and PAUSE to let the DOT trick show you string methods.
###############################################################################





###############################################################################
"""
A Counter's transform  method transforms the phrase that it is given
by putting a number in front of the phrase, that goes 1, 2, 3, ...

       elsa = Counter()
       elsa.transform("Hello")         returns "1. Hello"
       elsa.transform("Goodbye")       returns "2. Goodbye"
       elsa.transform("Sing for me")   returns "3. Sing for me"

Here are some examples that you can use for testing:
       bob = Counter()
       alice = Counter()
       a = bob.transform("Hello")
       b = bob.transform("Goodbye")
       c = bob.transform("Sing for me")
       d = alice.transform("This is Alice")
       e = bob.transform("This is Bob again")
       print(a, b, c, d, e, sep="\n")
       
       prints:
           1. Hello
           2. Goodbye
           3. Sing for me
           1. This is Alice
           4. This is Bob again
"""


# TODO: 4. Implement the Counter class and add some code that tests it.
###############################################################################


###############################################################################
"""
A SlowThinker's transform  method transforms the phrase it is given into
the phrase that it was PREVIOUSLY given.  It returns "START" the first time.

       elsa = SlowThinker()
       elsa.transform("Hello")           returns "START"
       elsa.transform("Goodbye")         returns "Hello"
       elsa.transform("Sing for me")     returns "Goodbye"
       elsa.transform("What is next?")   returns "Sing for me"
"""


# TODO: 5. Implement the SlowThinker class and add some code that tests it.
###############################################################################
