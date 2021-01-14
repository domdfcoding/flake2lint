# 3rd party
import pytest
from click.testing import CliRunner, Result
from domdf_python_tools.testing import check_file_output
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from flake2lint import process_file
from flake2lint.__main__ import main


@pytest.fixture()
def example_file(tmp_pathplus):
	example_file = tmp_pathplus / "code.py"

	example_file.write_lines([
			'# noqa: D100',
			'',
			"def foo(  # noqa",
			"\tid: int = -1,  # noqa: A002  # pragma: no cover",
			"\tdir: PathLike = '.',  # noqa: A002  # pylint: disable=redefined-builtin",
			"\t): ...",
			'',
			"def easter_egg() -> None:  # noqa: D102,D103  # pragma: no cover",
			"\teaster = calc_easter(today.year)",
			"\teaster_margin = timedelta(days=7)",
			'',
			])

	return example_file


def test_flake2lint(example_file, file_regression: FileRegressionFixture):
	assert process_file(example_file)
	check_file_output(example_file, file_regression)


def test_cli(example_file, tmp_pathplus, file_regression: FileRegressionFixture):
	runner = CliRunner()

	result: Result = runner.invoke(main, catch_exceptions=False, args=[str(example_file)])
	check_file_output(example_file, file_regression)
	assert result.exit_code == 1
