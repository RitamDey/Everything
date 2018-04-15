# This code illustrates a few aspects of Failures.
# Generally, Twisted makes Failures for us.
from twisted.python.failure import Failure


class RhymeSchemeViolation(Exception):
    pass


print("Just making an exception")
print()

e = RhymeSchemeViolation()
failure = Failure(e)  # This failure won't contain any traceback info
print(failure, end="\n\n\n")


print("Catching an exception: ", end="\n\n")


def analyze_poem(poem):
    raise RhymeSchemeViolation()


try:
    analyze_poem("""\
            Roses are red.
            Violets are violet.
            That's why they're called Violets.
            Duh.
            """)
except:
    failure = Failure()


# This failure will contain both the exception raised and the traceback
print(failure)
