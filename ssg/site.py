from pathlib import Path


class Site:
    ''' Site Class which accepts a source and destination Path object'''

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exists_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
