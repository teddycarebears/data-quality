#!/usr/bin/env python
"""Tables definitions for indicator objects."""
from .base import Base, Dictionary
from sqlalchemy import Column, Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class ModelIndicatorType(Base, Dictionary):
    """Types of indicators."""

    __tablename__ = 'indicator_type'

    id = Column('indicator_type_id', Integer, primary_key=True)
    name = Column('indicator_type', String, nullable=False, unique=True)
    function = Column('function', String, nullable=False)
    createdDate = Column('created_date', DateTime, server_default=func.now())
    updatedDate = Column('updated_date', DateTime, server_default=func.now(), onupdate=func.now())

    indicators = relationship('ModelIndicator', backref='indicatorType')


class ModelIndicator(Base, Dictionary):
    """Data quality indicators."""

    __tablename__ = 'indicator'

    id = Column('indicator_id', Integer, primary_key=True)
    name = Column('indicator', String, nullable=False, unique=True)
    description = Column('indicator_description', String, nullable=False)
    indicatorTypeId = Column('indicator_type_id', Integer, ForeignKey('indicator_type.indicator_type_id'), nullable=False)
    batchOwnerId = Column('batch_owner_id', Integer, ForeignKey('batch_owner.batch_owner_id'), nullable=False)
    executionOrder = Column('execution_order', Integer, nullable=False, default=0)
    active = Column('flag_active', Boolean, nullable=False, default=True)
    createdDate = Column('created_date', DateTime, server_default=func.now())
    updatedDate = Column('updated_date', DateTime, server_default=func.now(), onupdate=func.now())

    indicatorParameters = relationship('ModelIndicatorParameter', backref='indicator', passive_deletes=True)
    indicatorResults = relationship('ModelIndicatorResult', backref='indicator', passive_deletes=True)
    sessions = relationship('ModelSession', backref='indicator', passive_deletes=True)


class ModelIndicatorParameterType(Base, Dictionary):
    """Indicator parameter types."""

    __tablename__ = 'indicator_parameter_type'

    id = Column('indicator_parameter_type_id', Integer, primary_key=True)
    name = Column('indicator_parameter_type', String, nullable=False, unique=True)
    description = Column('indicator_parameter_type_description', String, nullable=False)
    createdDate = Column('created_date', DateTime, server_default=func.now())
    updatedDate = Column('updated_date', DateTime, server_default=func.now(), onupdate=func.now())

    indicatorParameters = relationship('ModelIndicatorParameter', backref='parameterType')


class ModelIndicatorParameter(Base, Dictionary):
    """Indicator parameters."""

    __tablename__ = 'indicator_parameter'

    id = Column('indicator_parameter_id', Integer, primary_key=True)
    indicatorId = Column('indicator_id', Integer, ForeignKey('indicator.indicator_id', ondelete='CASCADE'), nullable=False)
    parameterTypeId = Column('indicator_parameter_type_id', Integer, ForeignKey('indicator_parameter_type.indicator_parameter_type_id', ondelete='CASCADE'), nullable=False)
    value = Column('indicator_parameter_value', String, nullable=False)
    createdDate = Column('created_date', DateTime, server_default=func.now())
    updatedDate = Column('updated_date', DateTime, server_default=func.now(), onupdate=func.now())


class ModelIndicatorResult(Base, Dictionary):
    """Indicator results."""

    __tablename__ = 'indicator_result'

    id = Column('indicator_result_id', Integer, primary_key=True)
    indicatorId = Column('indicator_id', Integer, ForeignKey('indicator.indicator_id', ondelete='CASCADE'), nullable=False)
    sessionId = Column('session_id', Integer, ForeignKey('session.session_id', ondelete='CASCADE'), nullable=False)
    alertOperator = Column('alert_operator', String, nullable=False)
    alertThreshold = Column('alert_threshold', Float, nullable=False)
    nbRecords = Column('nb_records', Integer, nullable=False)
    nbRecordsAlert = Column('nb_records_alert', Integer, nullable=False)
    nbRecordsNoAlert = Column('nb_records_no_alert', Integer, nullable=False)
    createdDate = Column('created_date', DateTime, server_default=func.now())
