from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    naam = Column(String(50))

    inchecks = relationship("Incheck", back_populates="students")
    uitchecks = relationship("Uitcheck", back_populates="students")

class Incheck(Base):
    __tablename__ = "inchecks"
    id = Column(Integer, primary_key=True, index=True)
    incheck = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student", back_populates="inchecks")


class Uitcheck(Base):
    __tablename__ = "uitchecks"
    id = Column(Integer, primary_key=True, index=True)
    uitcheck = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student", back_populates="uitchecks")
