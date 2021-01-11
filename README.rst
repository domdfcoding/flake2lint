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
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
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

.. |requires| image:: https://requires.io/github/domdfcoding/flake2lint/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/flake2lint/requirements/?branch=master
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/flake2lint/v0.1.0
	:target: https://github.com/domdfcoding/flake2lint/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/flake2lint
	:target: https://github.com/domdfcoding/flake2lint/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/flake2lint
	:target: https://pypi.org/project/flake2lint/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/flake2lint/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/flake2lint/master
	:alt: pre-commit.ci status

.. end shields

Installation
--------------

.. start installation

``flake2lint`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install flake2lint

.. end installation
