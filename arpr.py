# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""This module is the Archive and Purge engine"""
import time
import datetime
import db
import policyqueue


class ArPr(object):
    """The main archive and purge engine"""
    def __init__(self, policies_yml, db_url=""):
        if db_url:
            self.db_engine = db.get_engine(db_url)
        else:
            self.db_engine = db.get_engine(db.get_db_url_from_env())
        self.policy_queue = policyqueue.PolicyQueue(policies_yml)

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
        if policy.ar_stmt:
            return self._execute_stmt(policy.ar_stmt)

    def execute_purge_statement(self, policy):
        """Execute the purge statement of a given policy

        :param policy: The plicy to have its purge statement executed.
        :return: None
        """
        if policy.pr_stmt:
            return self._execute_stmt(policy.pr_stmt)

    def run(self):
        """Run the Archive and Purge scheduler

        :return: None
        """
        if self.policy_queue.empty():
            print("No policy to run.")
            return
        while True:
            start_date, current_policy = self.policy_queue.get()
            second_to_next = (start_date - datetime.datetime.now()).total_seconds()

            if second_to_next < 0:
                second_to_next = 0
            print("Next run: '%s' in %d second%s" %
                  (current_policy, second_to_next,
                   "" if second_to_next < 2 else "s"))
            time.sleep(second_to_next)
            print("\tExecuting archive statement at %s" %
                  (datetime.datetime.now()))
            self.execute_archive_statement(current_policy)
            print("\tExecuting   purge statement at %s" %
                  (datetime.datetime.now()))
            self.execute_purge_statement(current_policy)
            self.policy_queue.put(current_policy)

