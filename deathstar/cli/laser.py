import typer

from ..laser import fire

laser_cmd = typer.Typer(no_args_is_help=True)


@laser_cmd.command(name="fire")
def fire_cmd(planet: str):
    """Fire the deathstar laser at a planet

    Args:
        planet : Name of the planet to obliterate
    """
    fire(planet)
