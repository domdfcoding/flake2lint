###########
flake2lint
###########

.. start short_desc

**Tool and pre-commit hook to augment Flake8 noqa comments with PyLint comments.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/flake2lint/latest?logo=read-the-docs
	:target: https://flake2lint.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/flake2lint/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/flake2lint/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/flake2lint/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/flake2lint/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/flake2lint/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/flake2lint/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/flake2lint/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.herokuapp.com/github/domdfcoding/flake2lint/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/domdfcoding/flake2lint/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/flake2lint/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/flake2lint?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/flake2lint?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/flake2lint
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/flake2lint
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flake2lint?logo=python&logoColor=white
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flake2lint
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/flake2lint
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/flake2lint
	:target: https://github.com/domdfcoding/flake2lint/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/flake2lint
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/flake2lint/v0.4.2
	:target: https://github.com/domdfcoding/flake2lint/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/flake2lint
	:target: https://github.com/domdfcoding/flake2lint/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2022
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/flake2lint
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``flake2lint`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install flake2lint

.. end installation


Usage
--------

.. code-block:: bash

	flake2lint [-v] [-r] [FILENAMES]

``-v / --verbose``
^^^^^^^^^^^^^^^^^^

Show verbose output.

``-r / --recursive``
^^^^^^^^^^^^^^^^^^^^^

Permits the use of the pattern ``**`` to match any files, directories and subdirectories.


See `the documentation <https://flake2lint.readthedocs.io/en/latest/usage.html>`_ for more details.

Supported Flake8 Codes
------------------------

``flake2lint`` currently augments the following flake8 codes:

* ``A001`` ➞ ``redefined-builtin``
* ``A002`` ➞ ``redefined-builtin``
* ``A003`` ➞ ``redefined-builtin``

Contributions to add support for more codes are more than welcome. The relevant code is `here <https://github.com/domdfcoding/flake2lint/blob/98da9322512d28921bd9cbabb66d6f476066f1f8/flake2lint/__init__.py#L53-L56>`_.


Example
-----------

Before:

.. code-block:: python

	class FancyDialog(wx.Dialog):

		def __init__(
				self,
				parent,
				id=wx.ID_ANY,  # noqa: A002
				title="My Fancy Dialog",
				pos=wx.DefaultPosition,
				size=wx.DefaultSize,
				style=wx.DEFAULT_DIALOG_STYLE,
				name=wx.DialogNameStr,
				data=None
				): ...

After:

.. code-block:: python

	class FancyDialog(wx.Dialog):

		def __init__(
				self,
				parent,
				id=wx.ID_ANY,  # noqa: A002  # pylint: disable=redefined-builtin
				title="My Fancy Dialog",
				pos=wx.DefaultPosition,
				size=wx.DefaultSize,
				style=wx.DEFAULT_DIALOG_STYLE,
				name=wx.DialogNameStr,
				data=None
				): ...
