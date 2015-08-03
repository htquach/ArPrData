# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""This module is the Archive and Purge engine"""
import time
import db
import policyqueue


class ArPr(object):
    """The main archive and purge engine"""
    def __init__(self, policies_csv, db_url=""):
        if db_url:
            self.db_engine = db.get_engine(db_url)
        else:
            self.db_engine = db.get_engine(db.get_db_url_from_env())
        self.policies = policyqueue.PolicyQueue(policies_csv)

    def _execute_stmt(self, statement):
        """Helper function to execute statement on the engine

        :param statement: statement to be executed
        :return: None
        """
        self.db_engine.execute(statement)

    def execute_archive_statement(self, policy):
        """Execute the archive statement of a given policy

        :param policy: The policy to have its archive statement executed.
        :return: None
        """
        return self._execute_stmt(policy.ar_stmt)

    def execute_purge_statement(self, policy):
        """Execute the purge statement of a given policy

        :param policy: The plicy to have its purge statement executed.
        :return: None
        """
        return self._execute_stmt(policy.pr_stmt)

    def run(self):
        """Run the Archive and Purge scheduler

        :return: None
        """
        if not self.policies:
            print("No policy to run.")
            return
        while True:
            current_policy = self.policies.dequeue()
            time.sleep(current_policy.seconds_to_next_run)
            self.execute_archive_statement(current_policy)
            self.execute_purge_statement(current_policy)
            self.policies.enqueue(current_policy)

