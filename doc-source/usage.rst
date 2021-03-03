=======
Usage
=======

flake2lint
--------------

.. click:: flake2lint.__main__:main
	:prog: flake2lint
	:nested: none


.. versionadded:: 0.3.0

	Added the :option:`-v / --verbose <-v>` option.

pre-commit hook
------------------

Sample ``.pre-commit-config.yaml``:

.. pre-commit::
	:rev: v0.4.0

See `pre-commit <https://github.com/pre-commit/pre-commit>`_ for further information.

Supported Flake8 Codes
------------------------

``flake2lint`` currently augments the following flake8 codes:

* ``A001`` ➞ ``redefined-builtin``

  .. versionadded:: 0.4.0

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
			title='My Fancy Dialog',
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
			title='My Fancy Dialog',
			pos=wx.DefaultPosition,
			size=wx.DefaultSize,
			style=wx.DEFAULT_DIALOG_STYLE,
			name=wx.DialogNameStr,
			data=None
			): ...
