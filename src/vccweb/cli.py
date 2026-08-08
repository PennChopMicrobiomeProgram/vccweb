import argparse

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from vccweb.csvdata import SampleData
from vccweb.app import create_app
from vccweb.models import create_db, samples_table
from sqlalchemy import inspect


def load_data(url, input_data):
    engine = create_engine(args.url, echo=True)
    rows = list(input_data.row_dicts())
    stmt = insert(samples_table)
    with engine.begin() as connection:
        connection.execute(stmt, rows)


def main(argv=None):
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--url", help="database URL", default="sqlite:///hvp.db")
    p.add_argument("--password", help="shared login password", default="12345")
    p.add_argument("--samplecsv", help="sample data CSV", default="data/samples.csv")

    args = p.parse_args(argv)

    with open(args.samplecsv) as f:
        data = SampleData.from_csv(f)

        for requirement, result in data.check():
            print(requirement.description())
            print(result.message())

    # create_db(args.url)
    # load_data(args.url, input_data)

    app = create_app(data, args.password)
    app.run(debug=True)


