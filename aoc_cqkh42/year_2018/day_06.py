import numpy as np

from typing import Self,Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
# todo manhattan
# todo coords
# todo refactor
def manhattan(from_, to):
    return (from_-to).abs().sum()

class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        return np.array(self.line_numbers)

    def assigns(self, coords):
        centroids = np.reshape(self.parsed, (self.parsed.shape[0], 1, 2))
        distance = coords - centroids
        distance = np.abs(distance).sum(axis=2)
        distance = distance.T

        min_distances = distance.min(axis=1, keepdims=True)
        num_min_distances = (distance == min_distances).sum(axis=1)
        no_ties = distance[num_min_distances == 1]
        winner = np.argmin(no_ties, axis=1)
        return np.unique_counts(winner)

    def find_infinite(self):
        x= self.parsed[:, 0]
        y = self.parsed[:, 1]
        x_max = x.max()
        x_min = x.min()
        y_max = y.max()
        y_min = y.min()

        left = np.stack(np.meshgrid(x_min-1, np.arange(y_min, y_max+1)), axis=-1).reshape(-1,2)
        right = np.stack(np.meshgrid(x_max, np.arange(y_min, y_max+1)), axis=-1).reshape(-1,2)
        top = np.stack(np.meshgrid(np.arange(x_min, x_max+1),y_min-1),  axis=-1).reshape(-1,2)
        bottom = np.stack(np.meshgrid(np.arange(x_min, x_max+1), y_max),axis=-1).reshape(-1, 2)
        bad = set()
        for arr in [left, right, top, bottom]:
            numbers = self.assigns(arr)
            for num in numbers.values:
                bad.add(num)
        return bad


    def part_a(self):
        x= self.parsed[:, 0]
        y = self.parsed[:, 1]
        x_max = x.max()
        x_min = x.min()
        y_max = y.max()
        y_min = y.min()
        data = np.stack(np.meshgrid(np.arange(x_min, x_max + 1),
                                      np.arange(y_min, y_max + 1)),
                          axis=-1).reshape(-1, 2)
        output = self.assigns(data)
        output = dict(zip(output.values, output.counts))

        bad = self.find_infinite()
        for n in bad:
            del output[n]
        return max(output.values())





    def part_b(self, total=10_000):
        x = self.parsed[:, 0]
        y = self.parsed[:, 1]
        x_max = x.max()
        x_min = x.min()
        y_max = y.max()
        y_min = y.min()
        data = np.stack(np.meshgrid(np.arange(x_min, x_max + 1),
                                    np.arange(y_min, y_max + 1)),
                        axis=-1).reshape(-1, 2)
        centroids = np.reshape(self.parsed, (self.parsed.shape[0], 1, 2))
        distance = data - centroids
        distance = np.abs(distance).sum(axis=2)
        distance = distance.T
        summed = distance.sum(axis=1)
        return(summed<total).sum()

        return


if __name__ == "__main__":
    submit_answers(Solution,5 , 2018)
