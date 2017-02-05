![rm-protection logo](https://ooo.0o0.ooo/2017/02/03/58943f1ed88cd.png)
# rm-protection

![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0e08692cc124bcc8a416284d7e6e41a) ![PyPiversion](https://img.shields.io/pypi/v/rm-protection.svg)  ![Wheel](https://img.shields.io/pypi/format/rm-protection.svg)  ![python version](https://img.shields.io/pypi/pyversions/rm-protection.svg) ![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/alanzchen/rm-protection.svg)

A safe alternative for `rm` with minimum difference

Wiki: https://github.com/alanzchen/rm-protection/wiki

# What is this?
 `rm-protection` is a safe alternative for removing file. It works exactly the same as `rm` (in fact it passes arguments to `rm` almost untouched). The only difference is that it refuses to proceed if a `.*.rm-protection`  file is found and you failed to answer a question.

# Why are you here?

I watched GitLab engineers trying to recover their production database live on YouTube.

Suddenly an idea struck me: What if `rm` prompted to ask "Which server are you on?" or "Which database are you trying to delete?"?

![What if GitLab Ops had this...](https://ooo.0o0.ooo/2017/02/05/5896a5a715673.png)

The disaster could have been avoided.

# Quick Start

1.  Install from PyPi and make an alias for `rm-p` .

     `pip install rm-protection` and if you are sure, `alias rm="rm-p"`

2.  Protect your files using `protect`.

3.  Happy rm-ing!

# How does it work?

 It consists of two utilities: `rm-p` and `protect`. The latter one is to help you protect files.

 For example, you have a file called `important_file` and it is `protect`ed by `.important_file.rm-protection`. `rm-p` will recognize that `important_file` is protected and prompt to ask you a question stored in `.important_file.rm-protection`. `rm-p` will only proceed if you get the answer right.

 See it in action:

 ![Basic usage](https://ooo.0o0.ooo/2017/02/03/58943760b76ed.gif)

 It will also prevent you from deleting a directory with `protect`ed file(s) inside.

![Recursive protection](https://ooo.0o0.ooo/2017/02/03/589437603366e.png)

# Requirements
- Python 2 or 3
- Linux, unix and macOS
- `find`

# Known issues
- Currently does not support protecting files whose name starts with "-".

# Comparison with alternative methods
| Methods                                  | Can be used as "rm"? | Protect Specific Files | Flexibility | Additional Files   |
| ---------------------------------------- | -------------------- | ---------------------- | ----------- | ------------------ |
| [trash-cli](https://github.com/sindresorhus/trash-cli) | Yes                  | Somehow                | High        | Centralised Config |
| rm -i                                    | Yes                  | No or Somehow          | High        |                    |
| [safe-rm](https://launchpad.net/safe-rm) | Yes                  | Yes                    | Low         | Centralized Config |
| rm-protection                            | Yes                  | Yes                    | High        | One for each       |

# Why don't you just use XXX?

 `rm-protection` aims at providing maximum protection and flexibility while making minimum impact on daily operation.

 `rm -i` can be very annoying, `trash-cli` is a bit complex (imagine you have a habit of emptying the trash without a second thought, or imagine you are trying to free up spaces on a budget vm). ` Safe-rm` is inconvenient when you really need to delete something (you have to edit the configuration file).

 Instead, `rm-protection` asks you a question set by you. You are fully covered when removing files (you won't accidentally empty the trash with `trash-cli` or `| yes` with `rm -i`), and you can quickly remove files (without editing any configuration files).

# How to contribute?
Pull requests and issues are all welcome! Or tell others about this, so you can even `protect` the files you send to others!

Actually I don't care if people are using my implementation at all. I just think this kind of mechanism can be great -- using a `.rm-protection` file that asks questions.

If the community welcomes this mechanism, it will soon be ported/rewritten in every platform or languages, or even be implemented in the GNU coreutils. Then you can even get some default protections shipped with distributions and packages.

**So if you agree on this mechanism, please share with others!**