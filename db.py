# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.

"""This module handles database connection tasks"""
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
import constant
import exc

__author__ = 'htquach'


class DB(object):
    def get_db_url_from_env(self):
        """Get the DB URL from the environment variable.  Return the DB URL o
        :raise exc.ArPrDataDBURLEnvironmentVariableEmptyException:
        :rtype : str
        """
        db_url = os.getegid(constant.DB_URL_ENV_NAME)
        if db_url:
            self.check_db_url(db_url)
            return db_url
        else:
            raise exc.ArPrDataDBURLEnvironmentVariableEmptyException(
                "The DB URL environment variable '%s' is empty or not defined." %
                constant.DB_URL_ENV_NAME)

    @staticmethod
    def check_db_url(db_url):
        """Check for the correct format of the DB URL.  Return none if check
        passed.  Raise exception otherwise.
        :param db_url: The DB URL to be checked
        :raise exc.ArPrDataBadDBURLFormatException:
        :rtype : None
        """
        try:
            make_url(db_url)
        except Exception:
            raise exc.ArPrDataBadDBURLFormatException(
                "Incorrect DB URL Format.  Check http://docs.sqlalchemy.org"
                "/en/latest/core/engines.html?highlight=url#database-urls")

    def setup(self, db_url):
        return create_engine(self.check_db_url(db_url))

