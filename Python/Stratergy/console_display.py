from collections import namedtuple
from typing import List
import copy


from colorama import Back, Style, Fore


Marker = namedtuple("Marker", "label pos")


GRAPH_WIDTH = 5
FORMAT_TEXT = "{:^" + str(GRAPH_WIDTH) + "}"


class ConsoleDisplayParams:
    def __init__(
        self,
        nums: List[int] = [],
        markers: List[Marker] = [],
        water_array: List[int] = [],
    ) -> None:
        self.nums = nums
        self.markers = markers
        self.water_array = water_array


def place_numbers(params: ConsoleDisplayParams):
    nums = params.nums
    label = ""

    for num in nums:
        label += FORMAT_TEXT.format(num)
    return label


def display_markers(params: ConsoleDisplayParams):
    markers = copy.deepcopy(params.markers)
    arr = params.nums
    markers.sort(key=lambda item: item.pos)

    marker_str = ""
    for i in range(len(arr)):
        if markers and i == markers[0].pos:
            final_label = markers[0].label
            markers.pop(0)

            while markers and markers[0].pos == i:
                final_label += "," + markers[0].label
                markers.pop(0)
            marker_str += FORMAT_TEXT.format(final_label)
        else:
            marker_str += " " * GRAPH_WIDTH

    return marker_str


def display_buildings(params: ConsoleDisplayParams):
    original_arr: List[int] = params.nums
    water_arr: List[int] = params.water_array[:]

    arr = original_arr[:]
    max_val = max(arr)

    max_level = max_val

    res = ""

    while max_level > 0:
        out_str = ""
        for i in range(len(arr)):
            if arr[i] == max_level:
                if arr[i] == original_arr[i]:
                    out_str += (
                        Style.BRIGHT
                        + Fore.MAGENTA
                        + Back.WHITE
                        + "-" * GRAPH_WIDTH
                        + Style.RESET_ALL
                    )
                else:
                    out_str += (
                        Back.WHITE
                        + "|"
                        + (" " * (GRAPH_WIDTH - 2))
                        + "|"
                        + Style.RESET_ALL
                    )
                arr[i] -= 1
            elif water_arr[i] + original_arr[i] == max_level:
                out_str += Back.BLUE + "~" * GRAPH_WIDTH + Style.RESET_ALL
                water_arr[i] -= 1
            else:
                out_str += " " * GRAPH_WIDTH

        max_level -= 1
        if max_level != -1:
            res += out_str + "\n"

    res += "+" * (GRAPH_WIDTH * len(original_arr))

    return res


def display_array(params: ConsoleDisplayParams):
    arr = params.nums
    label = ""

    temp = ""
    for _ in arr:
        temp += "-" * (GRAPH_WIDTH - 1) + "+"

    for num in arr:
        label += "|" + ("{:^" + str(GRAPH_WIDTH - 1) + "}").format(num)
    label += "|"

    label = temp + "\n" + label + "\n" + temp
    return label


def place_indices(params: ConsoleDisplayParams):
    arr = params.nums
    temp = ConsoleDisplayParams()
    temp.nums = range(len(arr))
    return place_numbers(temp)
