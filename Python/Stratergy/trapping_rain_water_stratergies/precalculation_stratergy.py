from typing import List

from .base_startergy import BaseStratergy
from text_display_helpers import *

EXP = """Precalculation startegy pre-computes two arrays one that has maximum height 
on left and and one that has maximum height on right of any given index 
(pre computation is not shown in visualization).
These arrays are labled as left_max and right_max in the visualization
Then the algorithm for each index (i) takes maximum height on left by accessing
left_max array's i-1 and then takes right_max's i+1 to get maximum height on right.
The minimum of these two values minus the current height gives us the water that can
be collected at given height.

legend:
i -> Current index.
left_max -> Array containing maximum value on from left of 'i'.
right_max -> Array containing maximum value on from right of 'i'.
vol -> Computed water volume
cur_vol -> Current volume of water computed

SC: O(n)
TC: O(n)"""


class PreCalculationStratergy(BaseStratergy):
    def __init__(self, inp: List[int], adv: callable) -> None:
        super().__init__(inp, EXP, adv)
        self.left_max = [0] * self.n
        self.right_max = [0] * self.n
        self.pre_compute()
        self.i = 0
        self.vol = 0

    def add_all_pipeline_items(self):
        self.add_to_pipeline(display_buildings)
        self.add_to_pipeline(display_array)
        self.add_to_pipeline(place_indices)
        self.add_to_pipeline(self.add_marker_i)
        self.add_to_pipeline(display_markers)
        self.add_to_pipeline(self.add_left_max)
        self.add_to_pipeline(self.add_right_max)
        self.add_to_pipeline(self.add_comp)
        self.add_to_pipeline(self.add_vol)

    def add_marker_i(self, _):
        self._params.markers = [
            Marker("i", self.i),
        ]

    def add_vol(self, _):
        return "vol = " + str(self.vol)

    def add_left_max(self, _):
        self._params.markers = [
            Marker("i-1", self.i - 1),
        ]
        prev = self._params.nums
        self._params.nums = self.left_max
        out_txt = display_array(self._params)
        self._params.nums = prev
        return "left_max: \n" + out_txt + "\n" + display_markers(self._params)

    def add_right_max(self, _):
        self._params.markers = [
            Marker("i+1", self.i + 1),
        ]
        prev = self._params.nums
        self._params.nums = self.right_max
        out_txt = display_array(self._params)
        self._params.nums = prev
        return "right_max: \n" + out_txt + "\n" + display_markers(self._params)

    def add_comp(self, _):
        i = self.i
        cur_vol = self._water[i]
        txt = "cur_vol = NA"
        if cur_vol != 0:
            txt = f"cur_vol = min({self.left_max[i]}, {self.right_max[i]}) - {self._input_arr[i]} = {cur_vol}"

        return txt

    def pre_compute(self):
        self.left_max[0] = self._input_arr[0]
        max_so_far = self.left_max[0]
        for i in range(1, self.n):
            max_so_far = max(max_so_far, self._input_arr[i])
            self.left_max[i] = max_so_far

        max_so_far = self._input_arr[-1]
        self.right_max[-1] = max_so_far

        for i in range(self.n - 2, -1, -1):
            max_so_far = max(max_so_far, self._input_arr[i])
            self.right_max[i] = max_so_far

    def solve_step(self):
        for i in range(1, self.n - 1):
            vol_here = (
                min(self.left_max[i - 1], self.right_max[i + 1]) - self._input_arr[i]
            )
            if vol_here > 0:
                self._water[i] = vol_here
                self.vol = self.vol + self._water[i]
            self.i = i
            yield
