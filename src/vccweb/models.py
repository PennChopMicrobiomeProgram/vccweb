from __future__ import annotations

from datetime import date
from typing import Optional

from sqlalchemy import Date, Enum, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


class Library(Base):
    """Table describing the processing history of a sequencing library."""
    __tablename__ = "library"

    library_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    sample_id_alias: Mapped[Optional[str]] = mapped_column(String(100))

    # Subject info
    participant_id: Mapped[Optional[str]] = mapped_column(String(100))
    cohort: Mapped[Optional[str]] = mapped_column(String(100))

    # Specimen info
    timepoint: Mapped[Optional[str]] = mapped_column(String(100))
    date_collected: Mapped[Optional[str]] = mapped_column(String(100))
    anatomical_site: Mapped[Optional[str]] = mapped_column(String(100))
    total_weight_grams: Mapped[Optional[str]] = mapped_column(String(100))
    date_aliquoted: Mapped[Optional[str]] = mapped_column(String(100))
    date_hvp_custody: Mapped[Optional[str]] = mapped_column(String(100))
    scan_id: Mapped[Optional[str]] = mapped_column(String(100))

    # Methodological approach
    method: Mapped[Optional[str]] = mapped_column(String(100))

    # Library prep
    prep_type: Mapped[Optional[str]] = mapped_column(String(100))
    virome_prep_type: Mapped[Optional[str]] = mapped_column(String(100))
    prep_person: Mapped[Optional[str]] = mapped_column(String(100))
    prep_count: Mapped[Optional[str]] = mapped_column(String(100))
    prep_date: Mapped[Optional[str]] = mapped_column(String(100))
    volume_ul: Mapped[Optional[str]] = mapped_column(String(100))
    deviations: Mapped[Optional[str]] = mapped_column(String(500))

    # Sequencing info
    index_i7: Mapped[Optional[str]] = mapped_column(String(100))
    index_i5: Mapped[Optional[str]] = mapped_column(String(100))
    run_id: Mapped[Optional[str]] = mapped_column(String(100))
    barcode_plate: Mapped[Optional[str]] = mapped_column(String(100))
    barcode_well: Mapped[Optional[str]] = mapped_column(String(100))
    temp_library_id: Mapped[Optional[str]] = mapped_column(String(100))

    # Misc
    SST: Mapped[Optional[str]] = mapped_column(String(100))
    notes: Mapped[Optional[str]] = mapped_column(String(500))
