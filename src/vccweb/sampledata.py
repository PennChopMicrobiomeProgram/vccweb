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

class SampleData(Table):
    spec = spec

    def check(self):
        return self.spec.check(self)

    @property
    def column_names(self):
        return list(self.data.keys())

    @property
    def rows(self):
        for row in zip(*self.data.values()):
            yield list("" if x is None else x for x in row)
