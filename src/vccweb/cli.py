import argparse

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from vccweb.csvdata import InputData
from vccweb.models import Library, Base
from vccweb.app import main as run_web_app


def main(argv=None):
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--url", help="database URL", default="sqlite:///hvp.db")
    p.add_argument("--password", help="shared login password", default="12345")
    p.add_argument("--samplecsv", help="sample data CSV", default="data/samples.csv")

    args = p.parse_args(argv)

    with open(args.samplecsv) as f:
        input_data = InputData.from_csv(f)

        for requirement, result in input_data.check():
            print(requirement.description())
            print(result.message())

    engine = create_engine(args.url, echo=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    rows = list(input_data.row_dicts())
    with Session() as session:
        try:
            # High-performance bulk insert using the Core insert() construct
            session.execute(insert(Library), rows)
            session.commit()
            print(f"Successfully loaded {len(rows)} records.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            raise

    # run_web_app(args.url, args.password)

