#!/usr/bin/env python3
#
#  __main__.py
"""
pre-commit hook to augment Flake8 noqa comments with PyLint comments.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import sys
from typing import Iterable

# 3rd party
import click
from consolekit import click_command
from consolekit.options import flag_option
from domdf_python_tools.typing import PathLike

__all__ = ["main"]


@flag_option(
		"-r",
		"--recursive",
		help="Permits the use of the pattern '**' to match any files, directories and subdirectories.",
		)
@click.argument("filenames", type=click.STRING, nargs=-1)
@click_command()
def main(filenames: Iterable[PathLike], recursive: bool = False):
	"""
	Augment Flake8 noqa comments with PyLint comments.
	"""

	# stdlib
	import functools
	import glob
	from itertools import chain

	# 3rd party
	from domdf_python_tools.paths import PathPlus

	# this package
	from flake2lint import process_file

	ret = 0
	glob_func = functools.partial(glob.iglob, recursive=recursive)

	for file in map(PathPlus, chain.from_iterable(map(glob_func, filenames))):
		if ".git" in file.parts or "venv" in file.parts or ".tox" in file.parts:
			continue

		ret |= process_file(file)

	sys.exit(ret)


if __name__ == "__main__":
	main()
