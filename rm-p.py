#!/usr/bin/env python3
from sys import argv, exit
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, isdir
from subprocess import Popen, PIPE


def ask(evalpath, path=""):
    with open(evalpath, "r") as f:
        if path:
            print(path + ": " + f.readline().rstrip("\n"))
        else:
            print("A file is protected by " + evalpath)
            print(f.readline().rstrip("\n"))
        answer = input("Answer: ")
        if answer == f.readline().rstrip("\n"):
            return True
        elif path:
            print("Wrong answer! " + path + " will not be removed.")
            return False
        else:
            print("Wrong answer! File protected by " + evalpath + " will not be removed.")
            return False


def protected_rm():
    args = ''
    suffix = ".rm-protection"
    for arg in argv[1:]:
        if not arg.startswith("-"):
            try:
                path = abspath(expv(expu(arg)))
                dirpath = dirname(path)
                if dirpath[-1] == "/":
                    evalpath = dirname(path) + "." + basename(path) + suffix
                else:
                    evalpath = dirname(path) + "/." + basename(path) + suffix
                if isdir(path):
                    find_exec = "find " + path + " -name " + "\".*" + suffix + "\"" + " -print"
                    out, err = Popen(find_exec, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
                    for pfile in iter(out.splitlines()):
                        if not ask(pfile):
                            print("Terminated due to potentially dangerous action.")
                            exit(1)
                if ask(evalpath, path):
                    args += arg + ' ' + evalpath + ' '
            except FileNotFoundError:
                args += arg + ' '
        else:
            args += arg + ' '
    Popen("rm " + args, shell=True)


if __name__ == "__main__":
    protected_rm()
