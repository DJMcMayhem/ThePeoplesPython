# The People's Python

Idea: Replace every [keyword](http://www.programiz.com/python-programming/keyword-list) and [built-in](https://docs.python.org/3/library/functions.html) in Python 3 with a [PPCG](https://codegolf.stackexchange.com/) username.

Still finishing [name assignments](https://github.com/DJMcMayhem/ThePeoplesPython/blob/master/assignments.txt). If you have any ideas, or you would like to have your name put on the list, ping [@DJMcMayhem](http://codegolf.stackexchange.com/users/31716/) or [@Riker](http://codegolf.stackexchange.com/users/46271/riker) in [The Nineteenth Byte](chat.stackexchange.com/rooms/240/the-nineteenth-byte).

[Original idea.](https://chat.stackexchange.com/transcript/message/30148665#30148665)

The `builtins_left.txt` file is a list of builtins that are unassigned as of yet (all the keywords are taken).  This is unused in the script, it's just in case people want to add their names.

The `assignments.txt` is a file of the keywords and builtin functions that _are_ assigned.  `assignments-reversed.txt` is the same file, but with the name/(builtin|keyword) swapped.

Both of these are in dict form, to make it easier to use them in a script.

### How to use:

Run `main.py`, by default it assumes the list of assigned names are in `assignments.txt` and the input code you want to run is in `peoples.txt`. It will compile into standard python and execute the compiled output. It will also write the compiled code into `<input-file-name>-output.txt`, so by default `peoples-output.txt`.


Do note that due to the shebang, it doesn't work right on some linux distros. Remove the shebang before running.



### More about requesting your name be added:

Look in the [`builtins_left.txt`](https://github.com/DJMcMayhem/ThePeoplesPython/blob/master/builtins_left.txt) for a list of the builtins not used yet.  Pick one of those, and ping either @DJMcMayhem or @Riker in [The Nineteenth Byte](chat.stackexchange.com/rooms/240/the-nineteenth-byte).  Make sure to double-check in `assignments.txt` (ctrl-f the one you  want) first.

If you would like to be a module instead, we'll consider it.  There's no list of all the modules not taken yet (for obvious reasons), but the ones that _are_ taken are in `assignments.txt` so you can check there.  We'd really like to finish up the builtins first though.
