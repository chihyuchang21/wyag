# import argparse #To parse command line arguments
# import collections # OrderedDict
# import configparser
# from datetime import datetime
# import  gitRepository

# # To read the users/group DB on Unix
# import grp #Group
# import pwd #Users

# from fnmatch import fnmatch # Support .gitignore: match filenames against patterns like *.txt.
# import hashlib # Git uses the SHA-1 function quite extensively
# from math import ceil
# import os # Provide nice filesystem abstraction routines
# import re # Regular Expression
# import sys  # access the actual command-line arguments
# import zlib # Git compresses everything using zlib

# argparser = argparse.ArgumentParser(description="The stupidest content tracker")
# argsubparsers = argparser.add_subparsers(title= "Commands", dest= "command") # handle subcommands (as in git: init, commit, etc.
# argsubparsers.required = True

# # 3.2: git init
# argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
# argsp.add_argument("path",
#                    metavar="directory",
#                    nargs="?",
#                    default=".",
#                    help="Where to create the repository.")

# # 4.6: git cat-file
# argsp = argsubparsers.add_parser("cat-file",
#                                  help="Provide content of repository objects")

# argsp.add_argument("type",
#                    metavar="type",
#                    choices=["blob", "commit", "tag", "tree"],
#                    help="Specify the type")

# argsp.add_argument("object",
#                    metavar="object",
#                    help="The object to display")



# def main(argv=sys.argv[1:]):
#     args = argparser.parse_args(argv)
#     match args.command:
#         # case "add"          : cmd_add(args)
#         case "cat-file"     : cmd_cat_file(args)
#         # case "check-ignore" : cmd_check_ignore(args)
#         # case "checkout"     : cmd_checkout(args)
#         # case "commit"       : cmd_commit(args)
#         # case "hash-object"  : cmd_hash_object(args)
#         case "init"         : cmd_init(args)
#         # case "log"          : cmd_log(args)
#         # case "ls-files"     : cmd_ls_files(args)
#         # case "ls-tree"      : cmd_ls_tree(args)
#         # case "rev-parse"    : cmd_rev_parse(args)
#         # case "rm"           : cmd_rm(args)
#         # case "show-ref"     : cmd_show_ref(args)
#         # case "status"       : cmd_status(args)
#         # case "tag"          : cmd_tag(args)
#         case _              : print("Bad command.")


# def cmd_init(args):
#     gitRepository.repo_create(args.path)

               
