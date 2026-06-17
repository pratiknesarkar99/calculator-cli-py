from click.testing import CliRunner
from calculator.cli import main


runner = CliRunner()


# ─── ADD ALL ──────────────────────────────────────────────────────────────────

def test_add_all_integers():
    result = runner.invoke(main, ["add", "all", "1", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_add_all_floats():
    result = runner.invoke(main, ["add", "all", "1.5", "2.5", "-f"])
    assert result.exit_code == 0
    assert "Result: 4.0" in result.output


def test_add_all_no_args():
    result = runner.invoke(main, ["add", "all"])
    assert result.exit_code != 0


# ─── ADD EVEN ─────────────────────────────────────────────────────────────────

def test_add_even_basic():
    result = runner.invoke(main, ["add", "even", "1", "2", "3", "4"])
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_add_even_none_found():
    result = runner.invoke(main, ["add", "even", "1", "3", "5"])
    assert result.exit_code == 0
    assert "No even numbers found." in result.output


# ─── ADD ODD ──────────────────────────────────────────────────────────────────

def test_add_odd_basic():
    result = runner.invoke(main, ["add", "odd", "1", "2", "3", "4", "5"])
    assert result.exit_code == 0
    assert "Result: 9" in result.output


def test_add_odd_none_found():
    result = runner.invoke(main, ["add", "odd", "2", "4", "6"])
    assert result.exit_code == 0
    assert "No odd numbers found." in result.output


# ─── SUBTRACT ─────────────────────────────────────────────────────────────────

def test_sub_basic():
    result = runner.invoke(main, ["sub", "10", "3", "2"])
    assert result.exit_code == 0
    assert "Result: 5" in result.output


def test_sub_floats():
    result = runner.invoke(main, ["sub", "10.5", "0.5", "-f"])
    assert result.exit_code == 0
    assert "Result: 10.0" in result.output


# ─── MULTIPLY ─────────────────────────────────────────────────────────────────

def test_mul_basic():
    result = runner.invoke(main, ["mul", "2", "3", "4"])
    assert result.exit_code == 0
    assert "Result: 24" in result.output


def test_mul_by_zero():
    result = runner.invoke(main, ["mul", "5", "0"])
    assert result.exit_code == 0
    assert "Result: 0" in result.output


# ─── DIVIDE ───────────────────────────────────────────────────────────────────

def test_div_basic():
    result = runner.invoke(main, ["div", "20", "4"])
    assert result.exit_code == 0
    assert "Result: 5.0" in result.output


def test_div_by_zero():
    result = runner.invoke(main, ["div", "10", "0"])
    assert result.exit_code == 1


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
    assert result.exit_code == 1

# ─── HELP ─────────────────────────────────────────────────────────────────────

def test_main_help():
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_add_cmd_help():
    result = runner.invoke(main, ["add", "--help"])
    assert result.exit_code == 0
    assert "even" in result.output
    assert "odd" in result.output