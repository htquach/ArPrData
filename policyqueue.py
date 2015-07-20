# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""Policy Queue module.  A collection of policies sorted by the next run time"""
from . import exc
from . import policy


class PolicyQueue(object):
    """A policy list sorted by policy's next run time"""
    def __init__(self, policies_csv=""):
        self.policy_list = []
        with open(policies_csv, "r") as csv_file:
            lines = csv_file.readlines()
        for line in lines:
            if line.strip().startswith("#"):
                continue
            if len(line.split(",")) == 6:
                raise RuntimeError("Each line in the policies CSV need to have "
                                   "at exactly %s commas separated fields.\n"
                                   "'%s' is incorrectly formed." % (6, line))
            self.policy_list.append(policy.Policy(*(line.split(","))))

    def enqueue(self, new_policy):
        """Insert new policy to the queue ordered by its next start time

        :param new_policy: A policy to be added
        :return: None
        """
        if new_policy.name in [p.name for p in self.policy_list]:
            raise exc.ArPrDataDuplicatePolicyNameException(
                "Policy with the name '%s' already exists" % new_policy.name)
        self.policy_list.append(new_policy)
        sorted(self.policy_list, key=policy.Policy.seconds_to_next_run)

    def dequeue(self):
        """Pop a policy off the queue which is the next policy to run.

        :return: The next policy in the queue to be executed
        """
        next_run_policy = self.policy_list[0]
        self.remove(next_run_policy)
        return next_run_policy

    def remove(self, existing_policy):
        """Remove an existing policy from the queue

        :param existing_policy: The existing policy to be removed
        :return: None
        """
        self.policy_list.remove(existing_policy)

    def show_policies(self):
        """Print the content of the policy queue

        :return: None
        """
        for policy_item in self.policy_list:
            policy_item.show()
