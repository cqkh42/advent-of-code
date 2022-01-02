from dataclasses import dataclass

import regex

from aoc_cqkh42 import BaseSolution


@dataclass
class IP:
    def __init__(self, ip):
        self.ip = ip
        self.outside = regex.sub(r'\[.*?]', ' ', ip)
        self.inside = ' '.join(regex.findall(r'\[(\w+?)\]', ip))

    def tls(self):
        outside_match = bool(abba.search(self.outside))
        inside_match = bool(abba.search(self.inside))
        return outside_match and not inside_match

    def ssl(self):
        i = set(regex.findall(r'(\w)(?!\1)(\w)\1', self.inside, overlapped=True))

        o = set(regex.findall(r'(\w)(?!\1)(\w)\1', self.outside, overlapped=True))
        o = {(b, a) for a, b in o}
        return bool(i.intersection(o))


class Solution(BaseSolution):
    def parse_data(self):
        ips = [IP(ip) for ip in self.lines]
        return ips

    def part_a(self):
        return sum(ip.tls() for ip in self.parsed_data)

    def part_b(self):
        return sum(ip.ssl() for ip in self.parsed_data)


abba = regex.compile(r'(\w)(?!\1)(\w)\2\1')

abba_inside_pattern = r'\[\w*{}\w*\]'.format(abba.pattern)
abba_inside = regex.compile(abba_inside_pattern)

def find_abas(string):
    abas = regex.findall(r'(\w)(?!\1)(\w)(\1)', string, overlapped=True)
    new_abas = {''.join(i) for i in abas}
    return new_abas
