from tablemusthave import (
    Table,
    MustHave,
    columns_named,
    unique_values_for,
    values_matching,
)

required_columns = [
    "library_id",
]

date_pattern = r"\d{4}(-\d{2}-\d{2})?"

spec = MustHave(
    columns_named(required_columns),
    unique_values_for("library_id"),
    values_matching("date_hvp_custody", date_pattern),
    values_matching("prep_date", date_pattern),
    values_matching("virome_prep_date", date_pattern),
)

class InputData(Table):
    spec = spec

    def check(self):
        return self.spec.check(self)

    def row_dicts(self):
        colnames = self.data.keys()
        rows = zip(*self.data.values())
        for row in rows:
            yield dict(zip(colnames, row))
