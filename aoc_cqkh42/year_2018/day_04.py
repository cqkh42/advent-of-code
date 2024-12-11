from typing import Self, Any

import more_itertools
import parse
from collections import defaultdict, Counter
from more_itertools.more import split_before

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    GUARD_PARSER = parse.compile('Guard #{:d}')
    MINUTE_PARSER = parse.compile(r":{:d}]")
    def _parse(self: Self) -> Any:
        guards = defaultdict(list)
        a = sorted(self.lines)
        b = list(split_before(a, lambda x: 'begins shift' in x))
        for i in b:
            guard = self.GUARD_PARSER.search(i[0])[0]
            times = [i[0] for i in self.MINUTE_PARSER.findall(' '.join(i))]
            for pair in more_itertools.chunked(times[1:], 2):
                guards[guard].extend(range(pair[0], pair[1]))
        guards = {k: Counter(v) for k, v in guards.items()}
        return guards

    def part_a(self):
        most_guard = max(self.parsed, key=lambda x: self.parsed[x].total())
        return self.parsed[most_guard].most_common(1)[0][0] * most_guard

    def part_b(self):
        most_minute = max(self.parsed, key=lambda x: self.parsed[x].most_common(1)[0][1])
        return most_minute * self.parsed[most_minute].most_common(1)[0][0]

if __name__ == "__main__":
    submit_answers(Solution, 4, 2018)
