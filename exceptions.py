# this file will demonstrate the identification and handling of exceptions
# the basic code structure to deal with exceptions is the try-except-finally block

print('first try,')
try:
    print(x)
except:
    print('a part of our code within the "try section" caused and error...')
finally:
    print('program ended - this part is printed regardless of whether there was an error within the try block or not')

print()
print('lets try to be more specific...')
try:
    print(x)
except NameError:
    print('this indicates that we have a naming error.')
except:
    print('while this indicates that another part of our code within the "try section" caused and error.')
finally:
    print('program ended - this part is printed regardless of whether there was an error within the try block or not')


class CustomLowValueError(Exception):
    """The expected input is too low"""


print()
x = -1
print('now lets try to define a custom exception of our own...')
try:
    if x < 0:
        raise CustomLowValueError
except CustomLowValueError:
    print('this indicates that the input value is too low try increasing its value.')
except:
    print('this indicates that a code within the "try section" caused and error other than too low value input.')
finally:
    print('program ended - this part is printed regardless of whether there was an error within the try block or not')
