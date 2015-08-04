# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""Policy Queue module.  A collection of policies sorted by the next run time"""
import Queue
import heapq
import yaml
import policy


class PolicyQueue(Queue.PriorityQueue):
    """A policy list sorted by policy's next run time"""
    def _init(self, policies_yml, maxsize=0):
        Queue.PriorityQueue._init(self, maxsize)
        with open(policies_yml, "r") as yml_file:
            policies = yaml.load(yml_file)
            for p in policies:
                print("Queuing up policy %s" % p)
                self._put(policy.Policy(**p))

    def show_policies(self):
        """Print the content of the policy queue"""
        for policy_item in self.policy_list:
            policy_item.show()

    def _put(self, new_policy, heappush=heapq.heappush):
        """Put the policy in the queue prioritized on its next start date"""
        Queue.PriorityQueue._put(self,
                                 (new_policy.next_start_datetime, new_policy),
                                 heappush)

    def _get(self, heappop=heapq.heappop):
        """get the policy in the queue prioritized on its next start date"""
        return Queue.PriorityQueue._get(self, heappop)[1]
