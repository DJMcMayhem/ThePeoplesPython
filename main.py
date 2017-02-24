#!/usr/bin/env python

import tokenize
import json
import os
import argparse
import subprocess as sp

def get_args():
    argparser = argparse.ArgumentParser(description="People's Python - Convert 'people's' python to actual Python",
                                        add_help=True)
    argparser.add_argument('--assignments', required=False, type=str, dest='assignments',
                           default="assignments.txt", help="Assignments file for names to Python builtins. Default is "
                                                           "'assignments.txt'")
    argparser.add_argument('--people', '--peoples', required=False, type=str, dest='peoples', default="peoples.txt",
                           help="People's Python file, for conversion. Default is 'peoples.txt'.")
    argparser.add_argument('--no-write-output', required=False, dest='write', action="store_false",
                           default=True, help="Do not write output from conversion to standard python to a file, "
                                               "if this argument is provided.")
    argparser.add_argument('--no-exec-output', required=False, dest='execute', action="store_false",
                           default=True, help="Do not execute output from conversion and do whatever it is set to do, "
                                              "if this argument is provided.")

    return argparser.parse_args()

def handle_token(type_, token, (srow, scol), (erow, ecol), line):
    # Return the info about the tokens, if it's a NAME token then replace it

    if tokenize.tok_name[type_] == "NAME":
        token = token_names.get(token, token)
    return type_, token, (srow, scol), (erow, ecol), line


def run(assignments, open_from, to_write, to_exec):
    """
    Do the conversion from People's Python to Standard Python
    :param assignments: String denoting the path to open the name list from.
    :param open_from: String denoting the file to get People's Python code input from.
    :param to_write: True/False to determine whether we store the converted code to a file.
    :param to_exec: True/False to determine whether we execute the converted code.
    :return: The converted code.
    """

    with open(assignments, "r") as f:
        # Read the replacements into token_names
        global token_names
        token_names = json.load(f)

    with open(open_from) as source:
        # Get the tokenized version of the input, replace it, and untokenize into pretty output
        tokens = tokenize.generate_tokens(source.readline)
        handled_tokens = (handle_token(*token) for token in tokens)

        output = tokenize.untokenize(handled_tokens)

    writepath = open_from[:-4]+"-output.txt"

    if to_write:
        with open(writepath, 'w') as outfile:
            # Write to the output file
            outfile.write(output)

    if to_exec:
        if not to_write:
            writepath = 'tmp.' + writepath
            with open(writepath, 'w') as outfile:
                # Write to the output file
                outfile.write(output)
            outfile.close()

        (execout, execerr) = sp.Popen(str('python %s' % writepath).split(),
                                      stdout=sp.PIPE, stdin=sp.PIPE).communicate()

        if not to_write:
            os.remove(writepath)

        if execerr and execerr != '':
            raise RuntimeError("An issue occurred running the converted code:\n%s" % str(execerr))

        print execout

    return output


if __name__ == "__main__":
    token_names = None
    args = get_args()
    try:
        run(args.assignments, args.peoples, args.write, args.execute)
    except Exception as e:
        print "An exception has occurred:\n%s" % str(e)
