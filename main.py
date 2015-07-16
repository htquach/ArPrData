# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
import datetime


class Policy(object):
    """A ArPrData Policy that contains the archive and purge statements along
    with other attributes of a """
    def __init__(self, name, description, archive_statement, purge_statement,
                 run_every_n_second, start_datetime):
        self.name = name
        self.description = description
        self.ar_stmt = archive_statement
        self.pr_stmt = purge_statement
        self.interval = run_every_n_second
        self.next_run = start_datetime

    def next_start_datetime(self):
        now = datetime.datetime.now()
        #TODO:  Handle case "if now < self.next_run"
        seconds_to_next_run = (self.interval - (
            (now - self.next_run).total_seconds() % self.interval))
        return now + datetime.timedelta(seconds=seconds_to_next_run)

    def __repr__(self):
        return "Policy: %s, next run: %s"


class DuplicatePolicyNameException(Exception):
    """Policy name already exists in the ProlicyList"""
    pass


class PoliciesList(object):
    """A policy list sorted by policy's next run time"""
    def __init__(self, policies_csv=""):
        self.policies_list = []

    def add(self, policy):
        if policy.name in [p.name for p in self.policies_list]:
            raise DuplicatePolicyNameException("Policy with the name '%s' "
                                               "already exists" % policy.name)
        self.policies_list.append(policy)

    def remove(self, policy):
        self.policies_list.remove(policy)

    def update(self, policy):
        for p in self.policies_list:
            if p.name == policy.name:
                self.policies_list.remove(p)
                self.policies_list.add(policy)

    def show_policies(self):
        for p in self.policies_list:
            p.show()


class ArPr(object):
    def __init__(self, policies_csv="policies.csv"):
        self.policies = PoliciesList(policies_csv)

    def _execute_stmt(self, statement):
        raise NotImplemented

    def execute_archive_statement(self, policy):
        raise NotImplemented

    def execute_purge_statement(self, policy):
        raise NotImplemented

    def run(self):
        raise NotImplemented


def main():
    ap = ArPr()
    ap.run()


if __name__ == "__main__":
    main()


