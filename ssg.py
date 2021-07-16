import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dist": dest
    }

    Site(**config).build()


typer.run(main)
