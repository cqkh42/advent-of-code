from typing import Self

import parse
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from dataclasses import dataclass
from string import ascii_uppercase

@dataclass
class Worker:
    task: str | None = None
    time: int = 0


class Solution(BaseSolution):
    PARSER = parse.compile(
        r'Step {:w} must be finished before step {:w} can begin.'
    )
    def _parse(self: Self) -> dict[str, set[str]]:
        dependencies = {}
        for dependency, step in self.PARSER.findall(self.input_):
            if step in dependencies:
                dependencies[step].add(dependency)
            else:
                dependencies[step] = {dependency}
            if dependency not in dependencies:
                dependencies[dependency] = set()
        return dependencies

    def part_a(self):
        completed = ""
        while len(completed) < len(self.parsed):
            incomplete = set(self.parsed).difference(completed)
            valid = {step for step in incomplete if self.parsed[step].issubset(completed)}
            completed+=min(valid)

        return ''.join(completed)

    def part_b(self, num_workers=5, fixed=60):
        workers = [Worker() for _ in range(num_workers)]
        completed = set()
        in_progress = set()
        time = -1
        while len(completed) < len(self.parsed):
            for worker in workers:
                if worker.task:
                    if worker.time == fixed+ascii_uppercase.index(worker.task):
                        completed.add(worker.task)
                        in_progress.remove(worker.task)
                        worker.task = None
                        worker.time = 0
                    else:
                        worker.time += 1
            for worker in workers:
                if not worker.task:
                    valid = {
                        step for step in self.parsed if
                             self.parsed[step].issubset(completed)
                    }.difference(completed | in_progress)
                    if valid:
                        task = min(valid)
                        worker.task = task
                        in_progress.add(task)
            time += 1
        return time

if __name__ == "__main__":
    submit_answers(Solution,5 , 2018)
