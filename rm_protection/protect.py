from sys import argv
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, exists
from builtins import input
from rm_protection.config import Config


def protect(protect_args=None):
    c = Config()
    flags = ''
    option_end = False
    if not protect_args:
        protect_args = argv[1:]
    for arg in protect_args:
        if arg == '--':
            option_end = True
        elif (arg.startswith("-") and not option_end):
            flags = flags + arg[arg.rfind('-') + 1:]
        elif arg in c.invalid:
            print('protect: "." and ".." may not be protected')
        else:
            path = abspath(expv(expu(arg)))
            evalpath = dirname(path) + "/." + basename(path) + c.suffix
            if not exists(path):
                print("Warning: " + path + " does not exist")
            with open(evalpath, "w") as f:
                question = input("Question for " + path + ": ")
                answer = input("Answer: ")
                f.write(question + "\n" + answer + "\n" + flags.upper())


if __name__ == "__main__":
    protect()
