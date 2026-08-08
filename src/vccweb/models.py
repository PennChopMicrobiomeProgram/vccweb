from __future__ import annotations

from datetime import date
from typing import Optional

from sqlalchemy import (
    create_engine, MetaData, Table, Column, String,
)

vcc_metadata = MetaData()
samples_table = Table(
    "samples",
    vcc_metadata,
    Column("library_id", String(100), primary_key=True),
    Column("sample_id_alias", String(100)),

    # Subject info
    Column("participant_id", String(100)),
    Column("cohort", String(100)),

    # Specimen info
    Column("timepoint", String(100)),
    Column("date_collected", String(100)),
    Column("anatomical_site", String(100)),
    Column("total_weight_grams", String(100)),
    Column("date_aliquoted", String(100)),
    Column("date_hvp_custody", String(100)),
    Column("scan_id", String(100)),

    # Methodological approach
    Column("method", String(100)),

    # Library prep
    Column("prep_type", String(100)),
    Column("virome_prep_type", String(100)),
    Column("prep_person", String(100)),
    Column("prep_count", String(100)),
    Column("prep_date", String(100)),
    Column("volume_ul", String(100)),
    Column("deviations", String(500)),

    # Sequencing info
    Column("index_i7", String(100)),
    Column("index_i5", String(100)),
    Column("run_id", String(100)),
    Column("barcode_plate", String(100)),
    Column("barcode_well", String(100)),
    Column("temp_library_id", String(100)),

    # Misc
    Column("SST", String(100)),
    Column("notes", String(500)),
)

def create_db(url):
    engine = create_engine(url, echo=True)
    vcc_metadata.drop_all(engine)
    vcc_metadata.create_all(engine)
