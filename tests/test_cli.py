from click.testing import CliRunner
from calculator.cli import main
from calculator.exit_codes import ExitCode


runner = CliRunner()


# ─── ADD ALL ──────────────────────────────────────────────────────────────────

def test_add_all_integers():
    result = runner.invoke(main, ["add", "all", "1", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_add_all_floats():
    result = runner.invoke(main, ["add", "all", "1.5", "2.5"])
    assert result.exit_code == 0
    assert "Result: 4.0" in result.output


def test_add_all_no_args():
    result = runner.invoke(main, ["add", "all"])
    assert result.exit_code == ExitCode.NO_DATA


def test_add_auto_detects_float():
    result = runner.invoke(main, ["add", "all", "1", "2.5", "3"])
    assert result.exit_code == 0
    assert "Result: 6.5" in result.output


# ─── ADD EVEN ─────────────────────────────────────────────────────────────────

def test_add_even_basic():
    result = runner.invoke(main, ["add", "even", "1", "2", "3", "4"])
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_add_even_none_found():
    result = runner.invoke(main, ["add", "even", "1", "3", "5"])
    assert result.exit_code == ExitCode.NO_DATA


def test_add_even_rejects_non_whole_float():
    result = runner.invoke(main, ["add", "even", "1.5", "2.5"])
    assert result.exit_code == ExitCode.INPUT_ERROR


# ─── ADD ODD ──────────────────────────────────────────────────────────────────

def test_add_odd_basic():
    result = runner.invoke(main, ["add", "odd", "1", "2", "3", "4", "5"])
    assert result.exit_code == 0
    assert "Result: 9" in result.output


def test_add_odd_none_found():
    result = runner.invoke(main, ["add", "odd", "2", "4", "6"])
    assert result.exit_code == ExitCode.NO_DATA


# ─── SUBTRACT ─────────────────────────────────────────────────────────────────

def test_sub_basic():
    result = runner.invoke(main, ["sub", "10", "3", "2"])
    assert result.exit_code == 0
    assert "Result: 5" in result.output


def test_sub_floats():
    result = runner.invoke(main, ["sub", "10.5", "0.5"])
    assert result.exit_code == 0
    assert "Result: 10.0" in result.output


def test_sub_no_args():
    result = runner.invoke(main, ["sub"])
    assert result.exit_code == ExitCode.NO_DATA


# ─── MULTIPLY ─────────────────────────────────────────────────────────────────

def test_mul_basic():
    result = runner.invoke(main, ["mul", "2", "3", "4"])
    assert result.exit_code == 0
    assert "Result: 24" in result.output


def test_mul_by_zero():
    result = runner.invoke(main, ["mul", "5", "0"])
    assert result.exit_code == 0
    assert "Result: 0" in result.output


def test_mul_no_args():
    result = runner.invoke(main, ["mul"])
    assert result.exit_code == ExitCode.NO_DATA


# ─── DIVIDE ───────────────────────────────────────────────────────────────────

def test_div_basic():
    result = runner.invoke(main, ["div", "20", "4"])
    assert result.exit_code == 0
    assert "Result: 5.0" in result.output


def test_div_by_zero():
    result = runner.invoke(main, ["div", "10", "0"])
    assert result.exit_code == ExitCode.MATH_ERROR


def test_div_no_args():
    result = runner.invoke(main, ["div"])
    assert result.exit_code == ExitCode.NO_DATA


# ─── POWER ────────────────────────────────────────────────────────────────────

def test_pow_basic():
    result = runner.invoke(main, ["pow", "2", "10"])
    assert result.exit_code == 0
    assert "Result: 1024.0" in result.output


def test_pow_zero_exponent():
    result = runner.invoke(main, ["pow", "5", "0"])
    assert result.exit_code == 0
    assert "Result: 1.0" in result.output


# ─── SQUARE ROOT ──────────────────────────────────────────────────────────────

def test_sqrt_basic():
    result = runner.invoke(main, ["sqrt", "9"])
    assert result.exit_code == 0
    assert "Result: 3.0" in result.output


def test_sqrt_negative():
    result = runner.invoke(main, ["sqrt", "--", "-1"])
    assert result.exit_code == ExitCode.MATH_ERROR


# ─── INVALID INPUT ────────────────────────────────────────────────────────────

def test_parse_invalid_input():
    result = runner.invoke(main, ["add", "all", "abc"])
    assert result.exit_code == ExitCode.INPUT_ERROR


# ─── PIPELINE / STDIN ─────────────────────────────────────────────────────────

def test_add_all_from_stdin():
    result = runner.invoke(main, ["add", "all"], input="1 2 3")
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_add_even_from_stdin():
    result = runner.invoke(main, ["add", "even"], input="1 2 3 4 5")
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_sub_from_stdin():
    result = runner.invoke(main, ["sub"], input="10 3 2")
    assert result.exit_code == 0
    assert "Result: 5" in result.output


def test_mul_from_stdin():
    result = runner.invoke(main, ["mul"], input="2 3 4")
    assert result.exit_code == 0
    assert "Result: 24" in result.output


def test_div_from_stdin():
    result = runner.invoke(main, ["div"], input="20 4")
    assert result.exit_code == 0
    assert "Result: 5.0" in result.output


def test_no_args_no_stdin():
    result = runner.invoke(main, ["add", "all"])
    assert result.exit_code == ExitCode.NO_DATA


# ─── HELP ─────────────────────────────────────────────────────────────────────

def test_main_help():
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_main_help_short_flag():
    result = runner.invoke(main, ["-h"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_add_cmd_help():
    result = runner.invoke(main, ["add", "--help"])
    assert result.exit_code == 0
    assert "even" in result.output
    assert "odd" in result.output

def test_version_flag():
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output

def test_version_short_flag():
    result = runner.invoke(main, ["-V"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output