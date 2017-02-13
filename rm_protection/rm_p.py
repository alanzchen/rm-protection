from sys import argv, exit
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, isdir, exists
from subprocess import Popen, PIPE
from builtins import input
from rm_protection.config import Config


c = Config()


def ask(evalpath, parent=False):
    with open(evalpath, "r") as f:
        question = f.readline().rstrip("\n")
        answer = f.readline().rstrip("\n")
        try:
            flags = f.readline().rstrip("\n")
        except:
            flags = ''
        if parent and 'R' not in flags:
            print(original_path(evalpath) + ' is protected but flag "R" is missing.')
            return True
        else:
            print(original_path(evalpath) + ": " + question)
            if input("Answer: ") == answer:
                return True
            else:
                print("Wrong answer! " + original_path(evalpath) + " will not be removed")
                print("The answer is stored in " + evalpath)
            return False


def original_path(evalpath):
    global c
    basepath = dirname(evalpath)
    filename = basename(evalpath)[1:-len(c.suffix)]
    if basepath == '/':
        return basepath + filename
    else:
        return basepath + '/' + filename

def ask_in(q, a):
    return bool(input(q) in a)


def gen_evalpaths(path):
    paths = {}
    path = dirname(path)
    while path != '/':
        evalpath = gen_eval(path)
        paths[path] = evalpath
        path = dirname(path)
    return paths


def gen_eval(path):
    global c
    basedir = dirname(path)
    if basedir == '/':
        basedir = ''
    return basedir + "/." + basename(path) + c.suffix


def parent_clear(file_evalpaths):
    for filepath in file_evalpaths:
        parent_eval = file_evalpaths[filepath]
        if exists(parent_eval):
            print('The parent directory ' + filepath + ' is protected')
            result = ask(parent_eval, parent=True)
            if not result:
                print(filepath + ' will not be removed')
                return False
    return True


def rm(rm_args=None):
    global c
    args = ''
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
            file_evalpaths = gen_evalpaths(path)
            evalpath = gen_eval(path)
            if c.suffix in arg:
                print(path + " is a protection file")
                if ask_in(q="Do you want to remove it? (y/n) ", a="Yesyes"):
                    args += arg + ' '
                else:
                    print(path + " will not be removed")
                continue
            if exists(evalpath):
                if ask(evalpath):
                    paths.append(path)
                    evalpaths.append(evalpath)
                else:
                    continue
            if not parent_clear(file_evalpaths):
                continue
            if isdir(path):
                find_exec = "find " + path + " -name " + "\".*" + c.suffix + "\"" + " -print"
                out, err = Popen(find_exec, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
                for pfile in iter(out.splitlines()):
                    print("A protected file or directory is found inside " + path)
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
