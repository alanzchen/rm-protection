from sys import argv, exit
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, isdir, exists
from subprocess import Popen, PIPE
from builtins import input


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
    paths = []
    evalpaths = []
    for arg in argv[1:]:
        if not arg.startswith("-"):
            path = abspath(expv(expu(arg)))
            evalpath = dirname(path) + "/." + basename(path) + suffix
            if suffix in arg:
                print(path + " will not be removed.")
                continue
            if exists(evalpath):
                if ask(evalpath, path):
                    paths.append(path)
                    evalpaths.append(evalpath)
                else:
                    continue
            elif isdir(path):
                find_exec = "find " + path + " -name " + "\".*" + suffix + "\"" + " -print"
                out, err = Popen(find_exec, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
                for pfile in iter(out.splitlines()):
                    if not ask(pfile):
                        print("Terminated due to potentially dangerous action.")
                        exit(1)
            args += arg + ' '
        else:
            args += arg + ' '
    Popen("rm " + args, shell=True).wait()
    remove_protection_files = ''
    for i in range(len(paths)):
        if exists(evalpaths[i]) and not exists(paths[i]):
            remove_protection_files += evalpaths[i] + ' '
    if remove_protection_files:
        Popen("rm " + remove_protection_files, shell=True)


if __name__ == "__main__":
    protected_rm()
