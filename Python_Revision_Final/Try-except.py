# working of Try Except
try:
# write code inside Try block that could raise exception
    name = input("Enter name")
# writing different classes to catch exceptions:
#
except EOFError:
    # it occurs when we have aksed user input data and data not input
    print("Hello user, this is EOF exception,please enter some value")
except KeyboardInterrupt:
    print('Hello user you have pressed ctrl-c button.')
#     if both of above exception classes does not match, it will go in else
else:
    print('Hello user there is some format error')

"""
Here, first code inside try gets exceuted,
if no data entered, it raises EOFError,
if user presses ctrl+c, them keyboardInterrupt is there.
If no exception matches to given classes, it will give python error written in else.
"""


