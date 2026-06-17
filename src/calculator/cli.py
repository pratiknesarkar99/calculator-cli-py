import click
from calculator.operations import (
    add, subtract, multiply, divide,
    power, square_root, filter_even, filter_odd
)


@click.group()
def main():
    """A CLI calculator supporting basic arithmetic operations."""
    pass


# ─── ADD ──────────────────────────────────────────────────────────────────────

@main.group()
def add_cmd():
    """Add multiple numbers together."""
    pass


@add_cmd.command("all")
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def add_all(numbers, use_float):
    """Add all provided numbers."""
    parsed = _parse_numbers(numbers, use_float)
    result = add(parsed)
    click.echo(f"Result: {result}")


@add_cmd.command("even")
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def add_even(numbers, use_float):
    """Add only even numbers from the provided list."""
    parsed = _parse_numbers(numbers, use_float)
    evens = filter_even(parsed)
    if not evens:
        click.echo("No even numbers found.")
        return
    result = add(evens)
    click.echo(f"Even numbers: {evens}")
    click.echo(f"Result: {result}")


@add_cmd.command("odd")
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def add_odd(numbers, use_float):
    """Add only odd numbers from the provided list."""
    parsed = _parse_numbers(numbers, use_float)
    odds = filter_odd(parsed)
    if not odds:
        click.echo("No odd numbers found.")
        return
    result = add(odds)
    click.echo(f"Odd numbers: {odds}")
    click.echo(f"Result: {result}")


# ─── SUBTRACT ─────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def sub(numbers, use_float):
    """Subtract numbers left to right (e.g. 10 3 2 => 10 - 3 - 2)."""
    parsed = _parse_numbers(numbers, use_float)
    result = subtract(parsed)
    click.echo(f"Result: {result}")


# ─── MULTIPLY ─────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def mul(numbers, use_float):
    """Multiply numbers together."""
    parsed = _parse_numbers(numbers, use_float)
    result = multiply(parsed)
    click.echo(f"Result: {result}")


# ─── DIVIDE ───────────────────────────────────────────────────────────────────

@main.command()
@click.argument("numbers", nargs=-1, required=True)
@click.option("-f", "--float", "use_float", is_flag=True, help="Treat inputs as floating point numbers.")
def div(numbers, use_float):
    """Divide numbers left to right (e.g. 20 4 2 => 20 / 4 / 2)."""
    parsed = _parse_numbers(numbers, use_float)
    try:
        result = divide(parsed)
        click.echo(f"Result: {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)


# ─── POWER ────────────────────────────────────────────────────────────────────

@main.command()
@click.argument("base", type=float)
@click.argument("exponent", type=float)
def pow_cmd(base, exponent):
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
        raise SystemExit(1)

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def _parse_numbers(raw: tuple, use_float: bool) -> list:
    """Parse CLI string arguments into int or float."""
    try:
        if use_float:
            return [float(n) for n in raw]
        return [int(n) for n in raw]
    except ValueError:
        click.echo("Error: All arguments must be valid numbers.", err=True)
        raise SystemExit(1)