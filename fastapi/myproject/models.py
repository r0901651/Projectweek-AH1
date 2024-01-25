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

class Incheck(Base):
    __tablename__ = "inchecks"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    incheck = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student", back_populates="inchecks")


class Uitcheck(Base):
    __tablename__ = "uitchecks"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    uitcheck = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student", back_populates="uitchecks")
