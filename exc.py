# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.

"""This module defines all exceptions used in this application."""
__author__ = 'htquach'


class ArPrDataDuplicatePolicyNameException(Exception):
    """Policy name already exists in the ProlicyList"""
    pass


class ArPrDataBadDBURLFormatException(Exception):
    """DB URL is incorrectly formatted.  Check http://docs.sqlalchemy.org
    /en/latest/core/engines.html?highlight=url#database-urls"""
    pass


class ArPrDataDBURLEnvironmentVariableEmptyException(Exception):
    """The Environment variable that contain the DB URL is empty or not
    defined"""
    pass
