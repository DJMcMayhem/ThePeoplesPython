#!/usr/bin/env python

import tokenize
import sys
import json


def handle_token(type_, token, (srow, scol), (erow, ecol), line):
	# Return the info about the tokens, if it's a NAME token then replace it

	if tokenize.tok_name[type_] == "NAME":
		token = token_names.get(token, token)
	return type_, token, (srow, scol), (erow, ecol), line


def run(assignments="assignments.txt", open_from="peoples.txt", \
										to_write=True, to_exec=True):

	'''
	- `assignments` is the file to open the list of names from
	- `open_from` is the file to get the input code from
	- `to_write` is for toggling writing the compiled code to a file
	- `to_exec` is for toggling executing the code

	Both `to_write` and `to_exec` are for using this code in another
	file by way of importing it.
	'''

	with open(assignments, "r") as f:
		# Read the replacements into token_names
		global token_names
		token_names = json.load(f)

	with open(open_from) as source:
		# Get the tokenized version of the input, replace it, and untokenize into pretty output
		tokens = tokenize.generate_tokens(source.readline)
		handled_tokens = (handle_token(*token) for token in tokens)

		output = tokenize.untokenize(handled_tokens)

	if to_write:
		with open(open_from[:-4]+"-output.txt", 'w') as outfile:
			# Write to the output file
			outfile.write(output)

	if to_exec:
		exec output in globals(), locals()

	return output


if __name__ == "__main__":
	token_names = None
	try:
		if len(sys.argv) > 1:
			if len(sys.argv) > 2:
				run(assignments=sys.argv[1], open_from=sys.argv[2])
			else:
				run(assignments=sys.argv[1])
		else:
			run()

	except Exception as e:
		print "An exception has occurred:\n%s" % str(e)


