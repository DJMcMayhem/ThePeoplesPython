# The People's Python

Idea: Replace every [keyword](http://www.programiz.com/python-programming/keyword-list) and [built-in](https://docs.python.org/3/library/functions.html) in Python 3 with a [PPCG](https://codegolf.stackexchange.com/) username.

Still finishing [name assignments](https://github.com/DJMcMayhem/ThePeoplesPython/blob/master/assignments.txt). If you have any ideas, or you would like to have your name put on the list, ping [@DJMcMayhem](http://codegolf.stackexchange.com/users/31716/) in [The Nineteenth Byte](chat.stackexchange.com/rooms/240/the-nineteenth-byte).

[Original idea.](https://chat.stackexchange.com/transcript/message/30148665#30148665)

The `builtins_left.txt` file is a list of builtins that are unassigned as of yet (all the keywords are taken).  The `assignments.txt` is a file of the keywords and builtin functions that _are_ assigned.

Both of these are in dict form, to make it easier to use them in a script.


###How to use:

Run `main.py`, by default it assumes the list of assigned names are in `assignments.txt` and the input code you want to run is in `peoples.txt`. It will compile into standard python and execute the compiled output. It will also write the compiled code into `<input-file-name>-output.txt`, so by default `peoples-output.txt`.
