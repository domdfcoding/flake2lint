#!/usr/bin/env python3
#
#  __init__.py
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
#  PYLINT_INLINE_REGEXP and find_pylint_disable based on Flake8
#  Copyright (C) 2011-2013 Tarek Ziade <tarek@ziade.org>
#  Copyright (C) 2012-2016 Ian Cordasco <graffatcolmingov@gmail.com>
#  MIT Licensed
#

# stdlib
import re
from functools import lru_cache
from typing import Match, Optional

# 3rd party
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import DelimitedList
from domdf_python_tools.typing import PathLike
from flake8.style_guide import find_noqa  # type: ignore

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["find_pylint_disable", "process_file", "find_noqa"]

code_mapping = {
		"A002": "redefined-builtin",
		"A003": "redefined-builtin",
		}

PYLINT_INLINE_REGEXP = re.compile(
		r'# pylint(?::[\s]?disable=(?P<checks>([A-Z0-9-]+(?:[,;\s]+)?)+))?',
		re.IGNORECASE,
		)


@lru_cache(maxsize=512)
def find_pylint_disable(physical_line: str) -> Optional[Match[str]]:
	"""
	Search a string for ``# pylint: disable=...`` comments.

	:param physical_line:
	"""

	return PYLINT_INLINE_REGEXP.search(physical_line)


find_noqa.__doc__ = """
Search a string for ``# noqa: ...`` comments.

:param physical_line:
"""


def process_file(filename: PathLike) -> bool:
	"""
	Augment Flake8 noqa comments with PyLint comments in the given file.

	:param filename:

	:return: :py:obj:`True` if the file contents were changed. :py:obj:`False` otherwise.
	"""

	file = PathPlus(filename)
	contents = file.read_lines()
	original_contents = contents[:]

	for idx, line in enumerate(contents):
		noqa = find_noqa(line)

		if noqa is None:
			continue

		if noqa.groupdict()["codes"] is None:
			continue

		# Line has one or more noqa codes
		flake8_codes = DelimitedList(filter(bool, re.split("[,; ]", noqa.groupdict()["codes"])))

		line_before_comment = line[:noqa.span()[0]]
		line_after_comments = line[noqa.span()[1]:]

		# Search for pylint: disable= after the noqa comment
		disabled = find_pylint_disable(line[noqa.span()[1]:])
		disabled_checks = set()

		if disabled:
			line_after_comments = line[noqa.span()[1]:][disabled.span()[1]:]
			checks = disabled.groupdict()["checks"]

			if checks:
				disabled_checks = set(re.split("[,; ]", checks))

		for code in flake8_codes:
			disabled_checks.add(code_mapping.get(code, ''))

		disabled_checks = set(filter(bool, map(str.strip, disabled_checks)))

		buf = [line_before_comment.rstrip(), f"  # noqa: {flake8_codes:,}"]

		if disabled_checks:
			buf.extend([
					"  # pylint: disable=",
					f"{DelimitedList(sorted(disabled_checks)):,}",
					line_after_comments,
					])

		contents[idx] = ''.join(buf)

	file.write_lines(contents)

	return file.read_lines() != original_contents
