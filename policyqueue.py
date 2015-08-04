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
        print("Loading policies from '%s' file" % policies_yml)
        with open(policies_yml, "r") as yml_file:
            policies = yaml.load(yml_file)
            for p in policies:
                self._put(policy.Policy(**p))
                print("\tQueued up policy %s" % p)
        queue_size = self._qsize()

        print("Queued %s %s" % (queue_size,
                                "policy" if queue_size < 2 else "policies"))
        print("=" * 30)

    def show_policies(self):
        """Print the content of the policy queue"""
        for next_run, policy_item in list(self.queue):
            print(next_run, policy_item)

    def _put(self, new_policy, heappush=heapq.heappush):
        """Put the policy in the queue prioritized on its next start date"""
        Queue.PriorityQueue._put(self,
                                 (new_policy.next_start_datetime,
                                  new_policy),
                                 heappush)
