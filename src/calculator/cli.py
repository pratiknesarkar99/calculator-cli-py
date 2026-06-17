import sys
import click
from calculator.operations import (
    add as op_add, subtract, multiply, divide,
    power, square_root, filter_even, filter_odd
)
from calculator.exit_codes import ExitCode

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A CLI calculator supporting basic arithmetic operations."""
    pass


# ─── ADD ──────────────────────────────────────────────────────────────────────

@main.group()
def add():
    """Add multiple numbers together."""
    pass


@add.command("all")
@click.argument("numbers", nargs=-1, required=False)
def add_all(numbers):
    """Add all provided numbers. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    result = op_add(parsed)
    click.echo(f"Result: {result}")


@add.command("even")
@click.argument("numbers", nargs=-1, required=False)
def add_even(numbers):
    """Add only even numbers. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    try:
        evens = filter_even(parsed)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(ExitCode.INPUT_ERROR)
    if not evens:
        click.echo("No even numbers found.")
        raise SystemExit(ExitCode.NO_DATA)
    result = op_add(evens)
    click.echo(f"Even numbers: {evens}")
    click.echo(f"Result: {result}")


@add.command("odd")
@click.argument("numbers", nargs=-1, required=False)
def add_odd(numbers):
    """Add only odd numbers. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    try:
        odds = filter_odd(parsed)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(ExitCode.INPUT_ERROR)
    if not odds:
        click.echo("No odd numbers found.")
        raise SystemExit(ExitCode.NO_DATA)
    result = op_add(odds)
    click.echo(f"Odd numbers: {odds}")
    click.echo(f"Result: {result}")


# ─── SUBTRACT ─────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=False)
def sub(numbers):
    """Subtract numbers left to right. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    result = subtract(parsed)
    click.echo(f"Result: {result}")


# ─── MULTIPLY ─────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=False)
def mul(numbers):
    """Multiply numbers together. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    result = multiply(parsed)
    click.echo(f"Result: {result}")


# ─── DIVIDE ───────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=False)
def div(numbers):
    """Divide numbers left to right. Reads from stdin if no arguments given."""
    numbers = numbers or _read_numbers_from_stdin()
    if not numbers:
        click.echo("Error: provide numbers as arguments or via stdin.", err=True)
        raise SystemExit(ExitCode.NO_DATA)
    parsed = _parse_numbers(numbers)
    try:
        result = divide(parsed)
        click.echo(f"Result: {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(ExitCode.MATH_ERROR)


# ─── POWER ────────────────────────────────────────────────────────────────────

@main.command()
@click.argument("base", type=float)
@click.argument("exponent", type=float)
def pow(base, exponent):
    """Raise BASE to the power of EXPONENT."""
    result = power(base, exponent)
    click.echo(f"Result: {result}")


# ─── SQUARE ROOT ──────────────────────────────────────────────────────────────

@main.command()
@click.argument("number", type=str)
def sqrt(number):
    """Calculate the square root of NUMBER."""
    try:
        n = float(number)
        result = square_root(n)
        click.echo(f"Result: {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(ExitCode.MATH_ERROR)


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def _read_numbers_from_stdin() -> tuple[str, ...]:
    """Read whitespace-separated numbers from stdin if available."""
    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()
        if data:
            return tuple(data.split())
    return ()


def _parse_numbers(raw: tuple) -> list[int | float]:
    """
    Auto-detect int vs float from input strings.
    '3' -> 3 (int), '3.0' or '3.5' -> 3.0 (float).
    """
    result = []
    for n in raw:
        try:
            as_float = float(n)
            if as_float == int(as_float) and "." not in n:
                result.append(int(as_float))
            else:
                result.append(as_float)
        except ValueError:
            click.echo(
                f"Error: '{n}' is not a valid number. "
                "Provide integers (1 2 3) or decimals (1.5 2.5).",
                err=True,
            )
            raise SystemExit(ExitCode.INPUT_ERROR)
    return result