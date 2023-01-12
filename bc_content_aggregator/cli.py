"""Console script for bc_content_aggregator."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for bc_content_aggregator."""
    click.echo("Replace this message by putting your code into "
               "bc_content_aggregator.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
