# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
import datetime
import db
import exc


class Policy(object):
    """A ArPrData Policy that contains the archive and purge statements along
    with other attributes"""
    def __init__(self, name, description, archive_statement, purge_statement,
                 run_every_n_second, start_datetime):
        self.name = name
        self.description = description
        self.ar_stmt = archive_statement
        self.pr_stmt = purge_statement
        self.interval = run_every_n_second
        self.start_datetime = datetime.datetime.strptime(
            start_datetime, "YYYY-MM-DD HH:mm:ss")

    def next_start_datetime(self):
        now = datetime.datetime.now()
        #TODO:  Handle case "if now < self.next_run"
        seconds_to_next_run = (self.interval - (
            (now - self.start_datetime).total_seconds() % self.interval))
        return now + datetime.timedelta(seconds=seconds_to_next_run)

    def __repr__(self):
        return ("Policy: %s, next run: %s" % (self.name,
                                              self.next_start_datetime()))


class PoliciesQueue(object):
    """A policy list sorted by policy's next run time"""
    def __init__(self, policies_csv=""):
        self.policies_list = []
        with open(policies_csv, "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.strip().startswith("#"):
                continue
            if len(line.split(",")) == 6:
                raise RuntimeError("Each line in the policies CSV need to have "
                                   "at exactly %s commas separated fields.\n"
                                   "'%s' is incorrectly formed." % (6, line))
            self.policies_list.append(Policy(*(line.split(","))))

    def add(self, policy):
        if policy.name in [p.name for p in self.policies_list]:
            raise exc.DuplicatePolicyNameException("Policy with the name '%s' "
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
    """The main archive and purge engine"""
    def __init__(self, policies_csv="policies.csv", db_url=""):
        self.policies = PoliciesQueue(policies_csv)
        if db_url:
            self.db_engine = db.setup(db_url)
        else:
            self.db_engine = db.setup(db.get_db_url_from_env())

    def _execute_stmt(self, statement):
        raise NotImplemented

    def execute_archive_statement(self, policy):
        return self._execute_stmt(policy.ar_stmt)

    def execute_purge_statement(self, policy):
        return self._execute_stmt(policy.pr_stmt)

    def run(self):
        raise NotImplemented


def main():
    ap = ArPr()
    ap.run()


if __name__ == "__main__":
    main()


