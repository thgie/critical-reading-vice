# Critical reading VICE
This is the repository of the scripts that were used in helping in an attempt of critically reading the VICE[^1] source code. 

> VICE is a program that runs on a Unix, MS-DOS, Win32, OS/2, BeOS, QNX 4.x, QNX 6.x, Amiga, Syllable or Mac OS X machine and executes programs intended for the old 8-bit computers.

More information on this analysis can be found under [https://phd.thgie.ch/notes/VICE.html](https://phd.thgie.ch/notes/VICE.html).

## Setup
1. Download the source distribution from [https://vice-emu.sourceforge.io/index.html#download](https://vice-emu.sourceforge.io/index.html#download)
2. Copy all files ending in `*.c` and `*.h` from the downloaded archive's `src` folder to this repository's `src` folder
3. Flatten the hierarchy in the repository's `src` folder; no subfolders!
4. You are now able to execute the python scripts

## Scripts
- `count.py` counts the total lines of code in all the files
- `split.py` splits the provided source code files into files with either just comments or just code, and moves them to the appropriate folders
- `vice-network.py` generates a CSV file with the relations between files and their authors; meant to be imported in Gephi after
- `authors-network.py` generates a CSV file with the relations between files according to their `#include` statements; to be imported in Gephi after

[1]: https://web.archive.org/web/20230622010758/https://vice-emu.sourceforge.io/