class Task:
    def __init__(self, task_id: str, name: str, priority: int):
        self.task_id = task_id
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"Task(ID='{self.task_id}', Name='{self.name}', Priority={self.priority})"


class MaxHeapScheduler:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _sift_up(self, i):
        while i > 0 and self.heap[self._parent(i)].priority < self.heap[i].priority:
            parent_idx = self._parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

    def _sift_down(self, i):
        max_idx = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < len(self.heap) and self.heap[left].priority > self.heap[max_idx].priority:
            max_idx = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[max_idx].priority:
            max_idx = right

        if i != max_idx:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self._sift_down(max_idx)

    def insert(self, task: Task):
        """إضافة مهمة جديدة إلى شجرة الـ Heap"""
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)
        print(f"[+] Task Added: {task}")

    def extract_max(self):
        """سحب وتنفيذ المهمة ذات الأولوية القصوى"""
        if not self.heap:
            print("[-] Scheduler is empty, no tasks to extract.")
            return None

        root = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return root

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    scheduler = MaxHeapScheduler()

    print("--- 1. Inserting Tasks ---")
    scheduler.insert(Task("T1", "System Backup", 3))
    scheduler.insert(Task("T2", "Antivirus Scan", 5))
    scheduler.insert(Task("T3", "Handle User Input", 10))
    scheduler.insert(Task("T4", "Render Frame", 8))
    scheduler.insert(Task("T5", "Background Update", 1))

    print("\n--- 2. Executing Tasks (EXTRACT-MAX) ---")
    while not scheduler.is_empty():
        current_task = scheduler.extract_max()
        print(f"Executing: {current_task}")