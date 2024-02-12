from orm_base import Base
from sqlalchemy import Column, Integer, UniqueConstraint, Identity
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


class Department(Base):
    """An individual who is currently enrolled or has explicitly stated an intent
    to enroll in one or more classes.  Said individuals may or may not be admitted
    to the university.  For instance, open enrollment students have not (yet) been
    admitted to the university, but they are still students."""
    __tablename__ = 'department'
    name = Column(String(50), primary_key=True)
    abbreviation = Column(String(6), nullable=False, unique=True)
    chair_name = Column(String(80), nullable=False, unique=True)
    building = Column(String(10), nullable=False)
    office = Column(Integer, nullable=False)
    description = Column(String(80), nullable=False, unique=True)

    __table_args__ = (
        UniqueConstraint('building', 'office', name='building_office_uc'),
    )

    def __init__(self, name, abbreviation, chair_name, building, office, description):
        self.name = name
        self.abbreviation = abbreviation
        self.chair_name = chair_name
        self.building = building
        self.office = office
        self.description = description

    def __str__(self):
        return f"Department(name={self.name}, abbreviation={self.abbreviation}, chair_name={self.chair_name}, building={self.building}, office={self.office}, description={self.description})"
