import click


@click.group(short_help="mytheme CLI.")
def mytheme():
    """mytheme CLI.
    """
    pass


@mytheme.command()
@click.argument("name", default="mytheme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [mytheme]
