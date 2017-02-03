![rm-protection logo](https://ooo.0o0.ooo/2017/02/03/58943f1ed88cd.png)
# rm-protection

 ![PyPi Downloads](https://img.shields.io/pypi/dm/rm-protection.svg)  ![PyPiversion](https://img.shields.io/pypi/v/rm-protection.svg) ![Wheel](https://img.shields.io/pypi/format/rm-protection.svg)  ![python version](https://img.shields.io/pypi/pyversions/rm-protection.svg)

A safe alternative for `rm` with minimum difference.

# What is this?
 `rm-protection` is a safe alternative for removing file. It works exactly the same as `rm` (in fact it passes arguments to rm). The only difference is that it refuses to procceed if a `.*.rm-protection`  file is found and you failed to answer a question.

# Quick Start

1.  Install from PyPi and make an alias for `rm-p` .

     `pip install rm-protection & alias rm="rm-p"`

2.  Protect your files using `protect`.

3.  Happy rm-ing!

# How does it work?

 It consists of two utilities: `rm-p` and `protect`. The latter one is to help you protect files.

 For example, you have a file called `important_file` and it is `protect`ed by `.important_file.rm-protection`. `rm-p` will recognise that `important_file` is protected and prompt to ask you a question stored in `.important_file.rm-protection`. `rm-p` will only proceed if you get the answer right.

 See it in action:

 ![Basic usage](https://ooo.0o0.ooo/2017/02/03/58943760b76ed.gif)

 It will also prevent you from deleting a directory with `protect`ed file(s) inside.

![Recursive protection](https://ooo.0o0.ooo/2017/02/03/589437603366e.png)

# Requirements
- Python 3
- Linux, unix and macOS
- `find`

# Known issues
- Currently does not support protecting files whose name starts with "-".

# Comparison with alternative methods
| Methods                                  | Can be uesd as "rm"? | Protect Specific Files | Flexibility | Additional Files   |
| ---------------------------------------- | -------------------- | ---------------------- | ----------- | ------------------ |
| [trash-cli](https://github.com/sindresorhus/trash-cli) | Yes                  | Somehow                | High        | Centralised Config |
| rm -i                                    | Yes                  | No or Somehow          | High        |                    |
| [safe-rm](https://launchpad.net/safe-rm) | Yes                  | Yes                    | Low         | Centralised Config |
| rm-protection                            | Yes                  | Yes                    | High        | One for each       |

 `rm-protection` aims at providing maximum protection and flexibility while making minimum impact on daily operation.

 `rm -i` can be very annoying, `trash-cli` is a bit complex (imagine you have a habit of emptying the trash without a second thought, or imagine you are trying to free up spaces on a budget vm). ` Safe-rm` is inconvenient when you really need to delete something (you have to edit the configuration file).

 Instead, `rm-protection` asks you a question set by you. You are fully covered when removing files (you won't accidentally empty the trash with `trash-cli` or `| yes` with `rm -i`), and you can quickly remove files (without editing any configuration files).

# How to contribute?
Pull requests and issues are all welcome! Or tell others about this, so you can even `protect` the files you send to others!
