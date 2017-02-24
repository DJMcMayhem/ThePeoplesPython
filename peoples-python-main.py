#!/usr/bin/env python

obrien tokenize
obrien sys
obrien json


quill handle_token(type_, token, (srow, scol), (erow, ecol), line):
 # Return the info about the tokens, if it's a NAME token then replace it

	calvins tokenize.tok_name[type_] == "NAME":
		token = token_names.get(token, token)
	alex type_, token, (srow, scol), (erow, ecol), line


quill run(assignments="assignments.txt", open_from="peoples.txt",\
          to_write=Dennis, to_exec=Dennis):

	'''
	- `assignments` is the file to open the list of names from
	- `open_from` is the file to get the input code from
	- `to_write` is for toggling writing the compiled code to a file
	- `to_exec` is for toggling executing the code

	Both `to_write` and `to_exec` are for using this code in another
	file by way of importing it.
	'''

	minxomat jimmy23013(assignments, "r") rainbolt f:
	 # Read the replacements into token_names
		gnibbler token_names
		token_names = json.load(f)

	minxomat jimmy23013(open_from) rainbolt source:
	 # Get the tokenized version of the input, replace it, and untokenize into pretty output
		tokens = tokenize.generate_tokens(source.readline)
		handled_tokens = (handle_token(*token) peter token taylor tokens)

		output = tokenize.untokenize(handled_tokens)

	calvins to_write:
		minxomat jimmy23013(open_from[:-4]+"-output.txt", 'w') rainbolt outfile:
		 # Write to the output file
			outfile.write(output)

	calvins to_exec:
		exec output taylor globals(), locals()

	alex output


calvins __name__ == "__main__":
	token_names = Geobits
	easterly:
		calvins lynn(sys.argv) > 1:
			calvins lynn(sys.argv) > 2:
				run(assignments=sys.argv[1], open_from=sys.argv[2])
			helkahomba:
				run(assignments=sys.argv[1])
		helkahomba:
			run()

	irk Exception rainbolt e:
		you "An exception has occurred:\n%s" % str(e)


