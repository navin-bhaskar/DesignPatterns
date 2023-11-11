from .base_startergy import BaseStratergy
from console_display import *
from typing import List

EXP = """Pointer solution first takes maximum height (indicated as p) in the 
array and then starts iterating from left to the (p)eak index, recording the maximum height
encountered from this direction, tracked by l in visualization. The volume at the curent height can be obtained by
subtracting the current height at i from the minimum of peak and value at 'l'.
Once we reach the peak, the same procedure is applied from right to left, the maximum on right is
indicated by index 'r' in the visualization.

Legend:
i -> Current index 
p -> Index where the peak/max element was found
l -> Index of max value on left of 'p'
r -> Index of max value on right of 'p'
max_from_left -> maximum value from left
max_from_right -> Maximum value from right
peak -> Peak value
vol -> Computed water volume

SC: O(1)
TC: O(n)"""


class PointerStratergy(BaseStratergy):
    def __init__(self, inp: List[int], adv: callable) -> None:
        super().__init__(inp, EXP, adv)
        self._max_val = max(inp)
        self._max_idx = inp.index(self._max_val)

        self.max_from_left_idx = 0
        self.max_from_right_idx = self.n - 1

    def add_all_pipeline_items(self):
        self.add_to_pipeline(display_buildings)
        self.add_to_pipeline(display_array)
        self.add_to_pipeline(place_indices)
        self.add_to_pipeline(self.add_markers)
        self.add_to_pipeline(display_markers)
        self.add_to_pipeline(self.add_all_legends)

    def add_markers(self, _):
        self._params.markers = [
            Marker("i", self.i),
            Marker("l", self.max_from_left_idx),
            Marker("r", self.max_from_right_idx),
            Marker("p", self._max_idx),
        ]

    def add_all_legends(self, _):
        out_txt = f"max_from_left = {self._input_arr[self.max_from_left_idx]} @ idx={self.max_from_left_idx}\n"
        out_txt += f"max_from_right = {self._input_arr[self.max_from_right_idx]} @ idx={self.max_from_right_idx}\n"
        out_txt += f"peak = {self._input_arr[self._max_idx]} @ idx={self._max_val}\n"
        out_txt += f"Vol = {self.vol}"
        return out_txt

    def solve_step(self):
        for i in range(1, self._max_idx):
            cur_num = self._input_arr[i]

            max_from_left = self._input_arr[self.max_from_left_idx]
            vol_here = min(max_from_left, self._max_val) - cur_num
            if vol_here > 0:
                self._water[i] = vol_here
                self.vol = self.vol + self._water[i]
            if max_from_left < cur_num:
                self.max_from_left_idx = i

            self.i = i
            yield

        for i in range(self.n - 1, self._max_idx, -1):
            cur_num = self._input_arr[i]

            max_from_right = self._input_arr[self.max_from_right_idx]
            vol_here = min(max_from_right, self._max_val) - cur_num
            if vol_here > 0:
                self._water[i] = vol_here
                self.vol = self.vol + self._water[i]

            if max_from_right < cur_num:
                self.max_from_right_idx = i

            self.i = i
            yield
