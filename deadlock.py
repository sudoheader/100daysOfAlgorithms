from collections import defaultdict
from time import sleep
from threading import Thread, Lock

# algorithm
class SharedState:

    def __init__(self, n):
        self._lock = Lock()
        self._state = defaultdict(int)
        self._resources = [Lock() for _ in range(n)]

    def atomic(self, key, value=0):
        with self._lock:
            self._state[key] += value
            return self._state[key]

    def resource(self, i):
        return self._resources[i]

    def kill(self):
        resources = self._resources
        self._resources = None
        for i in resources:
            i.release()

def worker(pid, state):
    try:
        while True:
            state.atomic('waiting', 1)
            with state.resource(pid):
                state.atomic('waiting', 1)
                with state.resource(pid - 1):
                    state.atomic('waiting', -2)
                    state.atomic('tasks', 1)

    except RuntimeError:
        pass

def deadlock(n):
    state = SharedState(n)

    for i in range(n):
        Thread(target=worker, args=(i, state)).start()

    while state.atomic('waiting') < 2 * n:
        sleep(1)

    print(n, 'workers; deadlock after', state.atomic('tasks'), 'tasks')
    state.kill()

# run
for i in range(1, 10):
    deadlock(10 * i)
