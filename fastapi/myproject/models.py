from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    uid = Column(Integer)
    naam = Column(String)
    r_nummer = Column(String)

    inchecks = relationship("Incheck", back_populates="students")
    uitchecks = relationship("Uitcheck", back_populates="students")


class Examen(Base):
    __tablename__ = "examens"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    naam = Column(String)

    inchecks = relationship("Incheck", back_populates="examens")
    uitchecks = relationship("Uitcheck", back_populates="examens")
    manuals = relationship("Manual", back_populates="examens")


class Incheck(Base):
    __tablename__ = "inchecks"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    incheck = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))
    examen_id = Column(Integer, ForeignKey("examens.id"))

    students = relationship("Student", back_populates="inchecks")
    examens = relationship("Examen", back_populates="inchecks")


class Uitcheck(Base):
    __tablename__ = "uitchecks"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    uitcheck = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))
    examen_id = Column(Integer, ForeignKey("examens.id"))

    students = relationship("Student", back_populates="uitchecks")
    examens = relationship("Examen", back_populates="uitchecks")


class Manual(Base):
    __tablename__ = "manuals"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    naam = Column(String)
    r_nummer = Column(String)
    examen_id = Column(Integer, ForeignKey("examens.id"))

    examens = relationship("Examen", back_populates="manuals")


class Inschrijving(Base):
    __tablename__ = "inschrijvingen"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    examen_id = Column(Integer, ForeignKey("examens.id"))

    students = relationship("Student", back_populates="inschrijvingen")
    examens = relationship("Examen", back_populates="inschrijvingen")