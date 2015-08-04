# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""A Policy module that define the Policy class"""
import datetime


class Policy(object):
    """A ArPrData Policy that contains the archive and purge statements along
    with other attributes"""
    def __init__(self, name, description, archive_statement, purge_statement,
                 run_every_n_second, start_datetime):
        """Create a new Policy

        :param name: The name of the policy
        :param description: The description of the policy
        :param archive_statement: The statement to be executed to archive data
        :param purge_statement: The statement to be executed to purge data
        :param run_every_n_second: The interval to run this policy
        :param start_datetime: The start date time to being counting the
        interval.  Date value is expected to be either a datetime data type or
        a string 'YYYY-MM-DD HH:mm:ss'

        :return: None
        """
        # too-many-arguments
        # pylint: disable=R0913
        self.name = name
        self.description = description
        self.ar_stmt = archive_statement
        self.pr_stmt = purge_statement
        self.interval = run_every_n_second
        if isinstance(start_datetime, datetime.datetime):
            self.start_datetime = start_datetime
        else:
            self.start_datetime = datetime.datetime.strptime(
                start_datetime, "YYYY-MM-DD HH:mm:ss")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise RuntimeError("Policy's name cannot be blank")
        self._name = value

    @property
    def next_start_datetime(self):
        """Get the next start datetime

        :return: the date time of next run
        """
        now = datetime.datetime.now()
        seconds_to_next_run = (self.interval - (
            (now - self.start_datetime).total_seconds() % self.interval))
        return now + datetime.timedelta(seconds=seconds_to_next_run)

    @property
    def seconds_to_next_run(self):
        """The section from now until next run

        :return: The total seconds from now to next run
        """
        return (self.next_start_datetime
                - datetime.datetime.now()).total_seconds()

    def __str__(self):
        """Print the Policy

        :return: A string with basic information of this policy
        """
        return ("Policy: %s, next run: %s" % (self.name,
                                              self.next_start_datetime))
