from vccweb.sampledata import SampleData


csv_data = [
    "library_id,participant_id,body_site,storage_buffer,sample_use\n",
    "s1,p1,invalid site,neat,experiment\n",
    "s2,p2,np swab,invalid buffer,invalid use\n",
]


def test_from_csv():
    s = SampleData.from_csv(csv_data)
    assert s.data == {
        "library_id": ["s1", "s2"],
        "participant_id": ["p1", "p2"],
        "body_site": ["invalid site", "np swab"],
        "storage_buffer": ["neat", "invalid buffer"],
        "sample_use": ["experiment", "invalid use"],
    }


def test_column_names():
    s = SampleData.from_csv(csv_data)
    assert s.column_names == [
        "library_id",
        "participant_id",
        "body_site",
        "storage_buffer",
        "sample_use",
    ]


def test_rows():
    s = SampleData.from_csv(csv_data)
    assert list(s.rows) == [
        ["s1", "p1", "invalid site", "neat", "experiment"],
        ["s2", "p2", "np swab", "invalid buffer", "invalid use"],
    ]
