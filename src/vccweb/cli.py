import argparse

from vccweb.sampledata import SampleData
from vccweb.app import create_app


def main(argv=None):
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--password", help="shared login password", default="12345")
    p.add_argument("--datafile", help="sample data CSV", default="data/samples.csv")

    args = p.parse_args(argv)

    with open(args.datafile) as f:
        data = SampleData.from_csv(f)

    app = create_app(data, args.password)
    app.run(debug=True)
