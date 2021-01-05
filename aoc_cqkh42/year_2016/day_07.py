import re

tls = re.compile(r'(\w)(?!\1)(\w)\2\1')


def is_tls(ip):
    outside = re.sub(r'\[.*?\]', ' ', ip)
    outside_match = re.search(tls, outside)
    inside = re.search(r'\[\w*{}\w*\]'.format(tls.pattern), ip)

    return outside_match and not inside


def find_abas(string):
    abas = [string[index:index+3] for index in range(len(string)-2) if string[index] == string[index+2]]
    abas = {aba for aba in abas if ' ' not in aba}
    return abas

def is_ssl(ip):
    inside = ' '.join(re.findall(r'\[(\w+?)\]', ip))
    outside = re.sub(r'\[.*?\]', ' ', ip)
    inside_abas = find_abas(inside)
    inside_babs = {'{1}{0}{1}'.format(*string) for string in inside_abas}
    return inside_babs.intersection(find_abas(outside))


def part_a(data):
    ips = data.split('\n')
    good = [ip for ip in ips if is_tls(ip)]
    return len(good)


def part_b(data, **_):
    ips = data.split('\n')

    good = [ip for ip in ips if is_ssl(ip)]
    return len(good)
