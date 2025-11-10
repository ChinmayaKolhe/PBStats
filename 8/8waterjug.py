from collections import deque
from math import gcd
from typing import List, Tuple, Optional, Dict

State = Tuple[int, int]

class WaterJugProblem:
    def __init__(self, capA: int, capB: int, target: int, start: State = (0, 0)):
        self.capA = capA
        self.capB = capB
        self.target = target
        self.start = start

    def is_goal(self, s: State) -> bool:
        # Target is considered met if either jug has exactly target liters
        return s[0] == self.target or s[1] == self.target

    def solvable(self) -> bool:
        # Classic condition: target <= total capacity and target % gcd(capA, capB) == 0
        if self.target < 0 or self.target > max(self.capA, self.capB) and self.target > (self.capA + self.capB):
            return False
        if self.target == 0:
            return True
        return self.target % gcd(self.capA, self.capB) == 0 and self.target <= (self.capA + self.capB)

    def successors(self, s: State) -> List[Tuple[State, str]]:
        x, y = s
        A, B = self.capA, self.capB
        nxt = []

        # 1) Fill A
        if x < A:
            nxt.append(((A, y), f"Fill A to {A}"))

        # 2) Fill B
        if y < B:
            nxt.append(((x, B), f"Fill B to {B}"))

        # 3) Empty A
        if x > 0:
            nxt.append(((0, y), "Empty A"))

        # 4) Empty B
        if y > 0:
            nxt.append(((x, 0), "Empty B"))

        # 5) Pour A -> B
        if x > 0 and y < B:
            pour = min(x, B - y)
            nxt.append(((x - pour, y + pour), f"Pour {pour} from A->B"))

        # 6) Pour B -> A
        if y > 0 and x < A:
            pour = min(y, A - x)
            nxt.append(((x + pour, y - pour), f"Pour {pour} from B->A"))

        return nxt

    def bfs(self) -> Optional[List[Tuple[State, str]]]:
        """Return path as list of (state, action_taken_to_reach_it). First step has action 'Start'."""
        if not self.solvable():
            return None

        q = deque([self.start])
        parent: Dict[State, State] = {self.start: self.start}
        act: Dict[State, str] = {self.start: "Start"}
        visited = {self.start}

        while q:
            s = q.popleft()
            if self.is_goal(s):
                # Reconstruct path
                path: List[Tuple[State, str]] = []
                cur = s
                while True:
                    path.append((cur, act[cur]))
                    if cur == parent[cur]:
                        break
                    cur = parent[cur]
                path.reverse()
                return path

            for ns, a in self.successors(s):
                if ns not in visited:
                    visited.add(ns)
                    parent[ns] = s
                    act[ns] = a
                    q.append(ns)

        return None


def print_solution(path: List[Tuple[State, str]]):
    print("Solution (state: (A, B)):")
    for i, (st, action) in enumerate(path):
        prefix = f"Step {i:02d}:"
        print(f"{prefix:<9} {action:<18} -> {st}")

if __name__ == "__main__":
    # === Example 1 ===
    # Problem: Jug A=4L, Jug B=3L, target=2L (classic)
    # problem = WaterJugProblem(capA=4, capB=3, target=2, start=(0,0))
    # path = problem.bfs()
    # if path is None:
    #     print("No solution exists.")
    # else:
    #     print_solution(path)

    # === Example 2 (change caps/target easily) ===
    problem2 = WaterJugProblem(capA=5, capB=7, target=6)
    path2 = problem2.bfs()
    if path2: print_solution(path2)
