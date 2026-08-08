import os
from vccweb.cli import main

DATAFILE = os.environ.get("VCCWEB_DATA", "data/samples.csv")
PASSWORD = os.environ.get("VCCWEB_PASSWORD", "12345")

main(["--datafile", DATAFILE, "--password", PASSWORD])
