from dataclasses import dataclass

import regex

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class IP:
    PARSER = regex.compile(r"(\w)(?!\1)(\w)\1")
    abba = regex.compile(r"(\w)(?!\1)(\w)\2\1")
    def __init__(self, ip):
        self.ip = ip
        self.outside = regex.sub(r"\[.*?]", " ", ip)
        self.inside = " ".join(regex.findall(r"\[(\w+?)\]", ip))

    def tls(self):
        outside_match = bool(self.abba.search(self.outside))
        inside_match = bool(self.abba.search(self.inside))
        return outside_match and not inside_match

    def ssl(self):
        i = set(self.PARSER.findall(self.inside, overlapped=True))
        o = set(self.PARSER.findall(self.outside, overlapped=True))
        o = {(b, a) for a, b in o}
        return bool(i.intersection(o))


class Solution(BaseSolution):
    def _parse_line(self, line: str):
        return IP(line)

    def part_a(self):
        return sum(ip.tls() for ip in self.parsed_lines)

    def part_b(self):
        return sum(ip.ssl() for ip in self.parsed_lines)
