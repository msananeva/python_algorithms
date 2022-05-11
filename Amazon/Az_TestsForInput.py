"""
List as many functional tests as you can for a function
that takes in a string as input.
"""

# normal string
# empty string
# string with special chars (like o'hara)
# unicode chars (like Ctrl+C )
# sql injection ->
"""SELECT UserId, Name, Password FROM Users WHERE UserId = 105 or 1=1;
A hacker might get access to all the user names and passwords in a db, 
by simply inserting 105 OR 1=1 into the input field."""
# all ascii chars 0-255
# one char
# one int
# one special char
# one space
# one emoji
# long string
# string w spaces
# string with integers