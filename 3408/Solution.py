import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # Global heap storing (-priority, -taskId)
        self.heap = []
        # Map taskId -> priority
        self.prios = {}
        # Map taskId -> userId
        self.idmap = {}

        # Initialize with given tasks
        for userId, taskId, priority in tasks:
            heapq.heappush(self.heap, (-priority, -taskId))
            self.prios[taskId] = priority
            self.idmap[taskId] = userId
            
    def add(self, userId, taskId, priority):
        """
        Add a new task for a user.
        """
        heapq.heappush(self.heap, (-priority, -taskId))
        self.prios[taskId] = priority
        self.idmap[taskId] = userId

    def edit(self, taskId, newPriority):
        """
        Update the priority of an existing task.
        (We push a new entry and let the old one be lazily removed.)
        """
        self.add(self.idmap[taskId], taskId, newPriority)

    def rmv(self, taskId):
        """
        Remove a task by marking it invalid.
        """
        self.prios[taskId] = None
        self.idmap[taskId] = None

    def execTop(self):
        """
        Execute the task with the highest priority.
        If multiple tasks have the same priority, execute the one with the highest taskId.
        Return the userId of that task, or -1 if no tasks exist.
        """
        prio, tid = None, None
        while self.heap:
            # Peek top of heap
            prio, tid = self.heap[0]
            prio, tid = -prio, -tid

            # If this task is stale (priority doesn’t match), pop and continue
            if prio != self.prios[tid]:
                prio, tid = None, None
                heapq.heappop(self.heap)
                continue
            break  # Found a valid task
            
        if tid is not None:
            userId = self.idmap[tid]
            self.rmv(tid)  # Mark executed task as removed
            return userId
        else:
            return -1