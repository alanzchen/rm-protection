|rm-protection logo|

rm-protection
=============

A safe alternative for ``rm`` with minimum difference.

What is this?
=============

``rm-protection`` is a safe alternative for removing file. It works
exactly the same as ``rm`` (in fact it passes arguments to rm). The only
difference is that it refuses to procceed if a ``.*.rm-protection`` file is
found and you failed to answer a question.

Quick Start
===========

``pip install rm-protection``

1. Install from PyPi and make an alias for ``rm-p``.
2. Protect your files using ``protect``.
3. Happy rm-ing!

How does it work?
=================

It consists of two utilities: ``rm-p`` and ``protect``. The latter one
is to help you protect files.

For example, you have a file called ``important_file`` and it is
``protect``\ ed by ``.important_file.rm-protection``. ``rm-p`` will
recognise that ``important_file`` is protected and prompt to ask you a
question stored in ``.important_file.rm-protection``. ``rm-p`` will only
proceed if you get the answer right.

See it in action:

.. figure:: https://ooo.0o0.ooo/2017/02/03/58943760b76ed.gif
   :alt: Basic usage
   :scale: 80%

   Basic usage

It will also prevent you from deleting a directory with ``protect``\ ed
file(s) inside.

.. figure:: https://ooo.0o0.ooo/2017/02/03/589437603366e.png
   :alt: Recursive protection
   :scale: 80%
   
   Recursive protection

Requirements
============

-  Python 2 or 3
-  Linux, unix and macOS
-  ``find``

Known issues
============

-  Currently does not support protecting files whose name starts with
   "-".

Comparison with alternative methods
===================================

+---------------------------+---------------+----------------+---------+-------------+
| Methods                   | Can be uesd   | Protect        | Flexibi | Additional  |
|                           | as "rm"?      | Specific Files | lity    | Files       |
+===========================+===============+================+=========+=============+
| `trash-cli <https://githu | Yes           | Somehow        | High    | Centralised |
| b.com/sindresorhus/trash- |               |                |         | Config      |
| cli>`__                   |               |                |         |             |
+---------------------------+---------------+----------------+---------+-------------+
| rm -i                     | Yes           | No or Somehow  | High    |             |
+---------------------------+---------------+----------------+---------+-------------+
| `safe-rm <https://launchp | Yes           | Yes            | Low     | Centralised |
| ad.net/safe-rm>`__        |               |                |         | Config      |
+---------------------------+---------------+----------------+---------+-------------+
| rm-protection             | Yes           | Yes            | High    | One for     |
|                           |               |                |         | each        |
+---------------------------+---------------+----------------+---------+-------------+

``rm-protection`` aims at providing maximum protection and flexibility
while making minimum impact on daily operation.

``rm -i`` can be very annoying, ``trash-cli`` is a bit complex (imagine
you have a habit of emptying the trash without a second thought, or
imagine you are trying to free up spaces on a budget vm). Safe-rm is
inconvenient when you really need to delete something (you have to edit
the configuration file).

Instead, ``rm-protection`` asks you a question set by you. You are fully
covered when removing files (you won't accidentally empty the trash with
``trash-cli`` or ``| yes`` with ``rm -i``), and you can quickly remove
files (without editing any configuration files).

How to contribute?
==================

Pull requests and issues are all welcome! Or tell others about this, so
you can even ``protect`` the files you send to others!

.. |rm-protection logo| image:: https://ooo.0o0.ooo/2017/02/03/58943f1ed88cd.png
	:scale: 50%

