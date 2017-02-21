#!/usr/bin/env python2

import tokenize
import ast


def handle_token(type, token, (srow, scol), (erow, ecol), line):
	if tokenize.tok_name[type] == "NAME":
		token = token_names.get(token, token)
	return (type, token, (srow, scol), (erow, ecol), line)


def run(assignments="assignments.txt",open_from="peoples.txt"):
	with open(assignments, "r") as f:
		global token_names
		token_names = ast.literal_eval(f.read())


	with open(open_from) as source:
		tokens = tokenize.generate_tokens(source.readline)
		handled_tokens = (handle_token(*token) for token in tokens)

		output = tokenize.untokenize(handled_tokens)

	with open(open_from[:-3]+"-output.txt",'w') as outfile:
		outfile.write(output)
	
	return output


if __name__ == "__main__":
	exec run()

