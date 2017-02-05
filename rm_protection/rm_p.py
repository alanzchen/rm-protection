from sys import argv, exit
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, isdir, exists
from subprocess import Popen, PIPE
from builtins import input
from config import Config


def ask(evalpath, path=""):
    with open(evalpath, "r") as f:
        if path:
            print(path + ": " + f.readline().rstrip("\n"))
        else:
            print("A file is protected by " + evalpath)
            print(f.readline().rstrip("\n"))
        if input("Answer: ") == f.readline().rstrip("\n"):
            return True
        elif path:
            print("Wrong answer! " + path + " will not be removed")
            print("The answer is stored in " + evalpath)
            return False
        else:
            print("Wrong answer! File/directory protected by " + evalpath + " will not be removed")
            return False


def ask_in(q, a):
    if input(q) in a:
        return True
    else:
        return False


def rm(rm_args=[]):
    args = ''
    c = Config()
    paths = []
    evalpaths = []
    option_end = False
    if not rm_args:
        rm_args = argv[1:]
    for arg in rm_args:
        if arg == '--':
            option_end = True
        elif (arg.startswith("-") and not option_end) or arg in c.invalid:
            pass
        else:
            path = abspath(expv(expu(arg)))
            evalpath = dirname(path) + "/." + basename(path) + c.suffix
            if c.suffix in arg:
                print(path + " is a protection file")
                if ask_in(q="Do you want to remove it? (y/n) ", a="Yesyes"):
                    args += arg + ' '
                else:
                    print(path + " will not be removed")
                continue
            if exists(evalpath):
                if ask(evalpath, path):
                    paths.append(path)
                    evalpaths.append(evalpath)
                else:
                    continue
            elif isdir(path):
                find_exec = "find " + path + " -name " + "\".*" + c.suffix + "\"" + " -print"
                out, err = Popen(find_exec, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
                for pfile in iter(out.splitlines()):
                    if not ask(pfile):
                        print("Terminated due to potentially dangerous action")
                        exit(1)
        args += arg + ' '
    Popen("rm " + args, shell=True).wait()
    remove_protection_files = ''
    for evalpath, path in zip(evalpaths, paths):
        if exists(evalpath) and not exists(path):
            remove_protection_files += evalpath + ' '
    if remove_protection_files:
        Popen("rm " + remove_protection_files, shell=True)


if __name__ == "__main__":
    rm()
