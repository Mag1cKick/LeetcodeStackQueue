from collections import defaultdict, deque
#використав дефолт дікт, бо стало цікаво як зробити його оптимально, натикнувся на дікт у відповідях інших і вирішив переробити
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group_dict = defaultdict(deque)
        self.max_f = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_f = max(self.max_f, self.freq[val])
        self.group_dict[self.freq[val]].append(val)

    def pop(self) -> int:
        element = self.group_dict[self.max_f].pop()
        self.freq[element] -= 1
        if not self.group_dict[self.max_f]:
            self.max_f -= 1
        return element