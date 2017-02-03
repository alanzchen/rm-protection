#!/usr/bin/env python3
from sys import argv
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath

suffix = ".rm-protection"

def protect_file():
    for arg in argv[1:]:
        if arg.startswith('-'):
            print("Failed: " + arg)
            print("Error: Cannot proccess file name starts with \"-\".")
            continue
        try:
            path = abspath(expv(expu(arg)))
            dirpath = dirname(path)
            if dirpath[-1] == "/":
                evalpath = dirname(path) + "." + basename(path) + suffix
            else:
                evalpath = dirname(path) + "/." + basename(path) + suffix
            with open(evalpath, "w") as f:
                question = input("Question for " + path + ": ")
                answer = input("Answer: ")
                f.write(question + "\n" + answer)
        except:
            raise

if __name__ == "__main__":
    protect_file()
