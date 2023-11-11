from abc import ABC, abstractmethod
import time
import os
from typing import List
from text_display_helpers import DisplayParams


class BaseStratergy:
    def __init__(
        self,
        inp: List[int],
        explanation,
        advancing_option: callable = lambda: time.sleep(1),
    ) -> None:
        """Ctor or the rain water trapping solutions

        Args:
            inp (List[int]): Array of ints containing the heights of the buildings
            explanation (_type_): An explanation of the solution
            advancing_option (_type_, optional): Optional arg to step after each visualization.
            Defaults to lambda:time.sleep(1).

        Raises:
            ValueError: If input list length or value is grater than 15 or if the data in
            list is not integer tpe

        Returns:
            None
        """
        if not isinstance(inp, List):
            raise ValueError("Only lists of ints are supported")
        if len(inp) > 15 or max(inp) > 15:
            raise ValueError("Do not support array greater than 15")

        for num in inp:
            if not isinstance(num, int):
                raise ValueError("Solver accepts only array of integeres")
        self._input_arr = inp
        self._water = [0] * len(inp)
        self.n = len(inp)
        self._display_pipeline = []
        self._params = DisplayParams(self._input_arr, self._water, self._water)
        self.vol = 0
        self._adv_method = advancing_option
        self._explanation = explanation + "\n"

    def solve(self):
        """Calls the visualization piple line and displays each
        step on the console
        """
        self.add_all_pipeline_items()
        os.system("cls")
        print(self._explanation)
        print("Enter to continue")
        input()
        for _ in self.solve_step():
            out = self.execute_display_pipleine()
            os.system("cls")
            print(self._explanation)
            print(out)
            self._adv_method()

        print("Done.")

    def combine_text(self, **texts):
        return "\n".join(**texts)

    def display_text(self, text):
        print(text + "\n")

    def add_to_pipeline(self, method: callable):
        """Adds a method to pipeline that will be called in the course of
        visualization

        Args:
            method (callable): Function to be called as a step to add output to visualization
        """
        self._display_pipeline.append(method)

    def execute_display_pipleine(self) -> None:
        """Executes the list of pipeline items"""
        res = ""
        for item in self._display_pipeline:
            out_text = item(self._params)
            if out_text:
                res = res + out_text + "\n"

        return res

    @abstractmethod
    def solve_step(self):
        """Derived class should implement this as a generator function to allow for
        the solve() to get outpt of each step and print them on console
        """
        pass

    @abstractmethod
    def add_all_pipeline_items(self):
        """The derived class should implement this to add all items to display pipleine"""
        pass
