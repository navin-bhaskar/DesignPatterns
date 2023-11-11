import time

DELAY = 1


def adv_with_input():
    print("Press enter to continue")
    input()


class SolutionAdvancingFactory:
    def __init__(self) -> None:
        self._solution = {
            1: (f"Uses a delay of {DELAY}s after each step", lambda: time.sleep(DELAY)),
            2: (f"Waits for enter key to be pressed after each step", adv_with_input),
        }

    def get_options_with_desc_text(self):
        return "\n".join(
            [
                f"{key}. {self._solution[key][0]}"
                for key in sorted(self._solution.keys())
            ]
        )

    def get_advancement_option(self, option):
        if option not in self._solution:
            raise ValueError("Invalid option for advancement of steps in visualization")
        return self._solution[option][1]
