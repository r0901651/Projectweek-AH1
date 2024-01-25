from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    naam = Column(String)

    informatie = relationship("Informatie", back_populates="students")

class Informatie(Base):
    __tablename__ = "informatie"
    id = Column(Integer, primary_key=True, index=True)
    incheck = Column(DateTime)
    uitcheck = Column(DateTime)
    student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student", back_populates="informatie")
