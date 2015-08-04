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
        if self.policy_queue.empty():
            print("No policy to run.")
            return
        while True:
            current_policy = self.policy_queue.get()
            if current_policy.name == "Purge Table1":
                prefix = "11111"
            else:
                prefix = "22222"
            print("Next policy is '%s' in %d seconds" %
                  (current_policy, current_policy.seconds_to_next_run))
            time.sleep(current_policy.seconds_to_next_run)
            print("%s Executing archive statement at %s" %
                  (prefix, datetime.datetime.now()))
            # self.execute_archive_statement(current_policy)
            print("%s Executing   purge statement at %s" %
                  (prefix, datetime.datetime.now()))
            # self.execute_purge_statement(current_policy))
            self.policy_queue.put(current_policy)

