# stdlib
import time

# 3rd party
import pytest
from coincidence import check_file_output
from consolekit.testing import CliRunner, Result
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from flake2lint import process_file
from flake2lint.__main__ import main


@pytest.fixture()
def example_file(tmp_pathplus):
	example_file = tmp_pathplus / "code.py"

	example_file.write_lines([
			"# noqa: D100",
			'',
			"def foo(  # noqa",
			"\tid: int = -1,  # noqa: A002  # pragma: no cover",
			"\tdir: PathLike = '.',  # noqa: A002",
			"\t): ...",
			'',
			"def easter_egg() -> None:  # noqa: D102,D103  # pragma: no cover",
			"\teaster = calc_easter(today.year)",
			"\teaster_margin = timedelta(days=7)",
			'',
			])

	return example_file


def test_flake2lint(example_file, file_regression: FileRegressionFixture):
	st = (example_file).stat()
	assert st == st

	time.sleep(0.1)  # the whole thing happens so quickly the mtime was ending up the same

	assert process_file(example_file)
	check_file_output(example_file, file_regression)

	# mtime should have changed
	new_st = (example_file).stat()
	assert new_st.st_mtime != st.st_mtime
	assert new_st != st

	# Calling a second time shouldn't change anything
	assert not process_file(example_file)
	check_file_output(example_file, file_regression)

	# mtime should be the same
	assert (example_file).stat().st_mtime == new_st.st_mtime
	assert (example_file).stat() == new_st


def test_cli(
		example_file,
		tmp_pathplus,
		file_regression: FileRegressionFixture,
		cli_runner: CliRunner,
		):
	st = (example_file).stat()
	assert st == st

	time.sleep(0.1)  # the whole thing happens so quickly the mtime was ending up the same

	result: Result = cli_runner.invoke(main, catch_exceptions=False, args=[str(example_file)])
	check_file_output(example_file, file_regression)
	assert result.exit_code == 1

	# mtime should have changed
	new_st = (example_file).stat()
	assert new_st.st_mtime != st.st_mtime
	assert new_st != st

	# Calling a second time shouldn't change anything
	result = cli_runner.invoke(main, catch_exceptions=False, args=[str(example_file)])
	check_file_output(example_file, file_regression)
	assert result.exit_code == 0

	# mtime should be the same
	assert (example_file).stat().st_mtime == new_st.st_mtime
	assert (example_file).stat() == new_st


def test_cli_verbose(
		example_file,
		tmp_pathplus,
		file_regression: FileRegressionFixture,
		cli_runner: CliRunner,
		):
	result: Result

	st = (example_file).stat()
	assert st == st

	time.sleep(0.1)  # the whole thing happens so quickly the mtime was ending up the same

	result = cli_runner.invoke(main, catch_exceptions=False, args=[str(example_file), "--verbose"])
	assert result.stdout.rstrip().endswith("code.py'")
	assert result.stdout.startswith("Rewriting '")
	assert result.exit_code == 1

	# mtime should have changed
	new_st = (tmp_pathplus / "code.py").stat()
	assert new_st.st_mtime != st.st_mtime
	assert new_st != st

	# Calling a second time shouldn't change anything
	result = cli_runner.invoke(main, catch_exceptions=False, args=[str(example_file), "--verbose"])
	assert "code.py" not in result.stdout
	assert "Rewriting '" not in result.stdout
	assert result.exit_code == 0

	# mtime should be the same
	assert (tmp_pathplus / "code.py").stat().st_mtime == new_st.st_mtime
	assert (tmp_pathplus / "code.py").stat() == new_st
