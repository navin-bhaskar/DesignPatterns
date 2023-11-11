from typing import List

from trapping_rain_water_stratergies import (
    BaseStratergy,
    PointerStratergy,
    BruteForceStratergy,
    PreCalculationStratergy,
)

BRUTE_FORCE = 1
PRE_CALCULATION = 2
POINTER = 3


class SolutionsFactory:
    def __init__(self) -> None:
        self._solutions_map = {
            # key               desc                      startergy
            BRUTE_FORCE: ("Uses brute force solution", BruteForceStratergy),
            PRE_CALCULATION: (
                "Uses pre-calculated array to arrive at dolution",
                PreCalculationStratergy,
            ),
            POINTER: ("Uses pointers to compute the solution", PointerStratergy),
        }

    def get_options_with_desc_text(self) -> str:
        out_txt = ""
        for item_key in sorted(self._solutions_map.keys()):
            out_txt += f"{item_key}. " + self._solutions_map[item_key][0] + "\n"
        return out_txt

    def get_solution(
        self, solution_option: int, input_array: List[int], adv_option: callable
    ) -> BaseStratergy:
        if solution_option in self._solutions_map:
            return self._solutions_map[solution_option][1](input_array, adv_option)
        else:
            raise ValueError("Invalid solution option was passed")
