from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    uid = Column(Integer)
    naam = Column(String(50))

    inchecks = relationship("Incheck", back_populates="students")
    uitchecks = relationship("Uitcheck", back_populates="students")


class Examen(Base):
    __tablename__ = "examens"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    naam = Column(String(50))

    inchecks = relationship("Incheck", back_populates="examens")
    uitchecks = relationship("Uitcheck", back_populates="examens")


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
