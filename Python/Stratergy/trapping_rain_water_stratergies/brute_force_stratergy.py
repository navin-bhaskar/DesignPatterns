from .base_startergy import BaseStratergy
from text_display_helpers import *
from typing import List

EXP = """Brute force solution looks for maximum height towrads left (indicted by l)
and maximum height towards right (indicated by r) around each current index (indicated by i)
to compute the volume of water (vol)
legend:

i -> Current index
l -> Index for finding the max on left of index 'i'
r -> Index for finding the max on right of index 'i'  
left_max -> Max value found on left
right_max -> Max value found on right
vol -> Computed water volume

SC: O(1)
TC: O(nXn)"""


class BruteForceStratergy(BaseStratergy):
    def __init__(self, inp: List[int], adv: callable) -> None:
        super().__init__(inp, EXP, adv)
        self.left = 0
        self.right = 0
        self.l_i = 0
        self.r_i = 0
        self.i = 1

        self.left_max = 0
        self.right_max = 0

    def add_all_pipeline_items(self):
        self.add_to_pipeline(display_buildings)
        self.add_to_pipeline(display_array)
        self.add_to_pipeline(place_indices)
        self.add_to_pipeline(self.add_markers)
        self.add_to_pipeline(display_markers)
        self.add_to_pipeline(self.add_left_max)
        self.add_to_pipeline(self.add_right_max)
        self.add_to_pipeline(self.add_vol)

    def add_markers(self, _):
        self._params.markers = [
            Marker("l", self.l_i),
            Marker("r", self.r_i),
            Marker("i", self.i),
        ]

    def add_left_max(self, _):
        return "left_max = " + str(self.left)

    def add_right_max(self, _):
        return "right_max = " + str(self.right)

    def add_vol(self, _):
        return "vol = " + str(self.vol)

    def solve_step(self):
        for i in range(1, self.n - 1):
            self.i = i
            self.left = self._input_arr[i]
            for j in range(self.i):
                self.left = max(self.left, self._input_arr[j])
                self.l_i = j
                yield

            self.right = self._input_arr[self.i]

            for j in range(self.i + 1, self.n):
                self.right = max(self.right, self._input_arr[j])
                self.r_i = j
                yield

            self._water[i] = min(self.left, self.right) - self._input_arr[self.i]
            self.vol = self.vol + self._water[i]
            yield
