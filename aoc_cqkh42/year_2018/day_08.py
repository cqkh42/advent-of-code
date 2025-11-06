from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import more_itertools

def get_metadata(tree, metadata=None):
    metadata = metadata or []
    num_children, num_metadata, *tree = tree
    for child in range(num_children):
        tree, metadata = get_metadata(tree, metadata)
    metadata.append(tree[:num_metadata])
    return tree[num_metadata:], metadata

def get_metadata_two(tree, metadata=None):
    metadata = metadata or []
    num_children, num_metadata, *tree = tree
    children = []
    for child in range(num_children):
        tree, child_metadata = get_metadata_two(tree)
        children.append(child_metadata)
    this_meta = tree[:num_metadata]
    if num_children == 0:
        metadata.append(this_meta)
    else:
        for index in this_meta:
            try:
                metadata.append(children[index-1])
            except IndexError:
                continue
    return tree[num_metadata:], metadata

class Solution(BaseSolution):
    def part_a(self):
        _, metadata = get_metadata(self.numbers)
        return sum(more_itertools.collapse(metadata))

    def part_b(self):
        _, metadata = get_metadata_two(self.numbers)
        return sum(more_itertools.collapse(metadata))

if __name__ == "__main__":
    submit_answers(Solution,8 , 2018)
