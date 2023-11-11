from solutions_factory import SolutionsFactory
from solution_advancing_factory import SolutionAdvancingFactory


def main():
    samples_array = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [3, 0, 2, 0, 4], [2, 0, 2]]
    solution_factory = SolutionsFactory()
    solution_advancing_factory = SolutionAdvancingFactory()

    print(
        "Visualize different solution approaches to trapping rin water problem from comfort of you console"
    )

    print(
        "To begin with select a sample array by enetring "
        + " ".join(list(str(i) for i in range(1, len(samples_array) + 1)))
    )
    i = 0
    while True:
        try:
            print("Sample inputs:")
            for arr in samples_array:
                print(arr)

            i = int(input())
            if i <= 0 or i > len(samples_array):
                raise ValueError()
            break
        except ValueError:
            print(
                f"Invalid option, please enter a number between {1}-{len(samples_array)} both ends included"
            )
            pass
    i = i - 1
    print(f"Selected array {samples_array[i]}")

    options_text = solution_advancing_factory.get_options_with_desc_text()

    print("select how the visulization should advnce (defaults to option 1)")
    print(options_text)
    opt = input()
    try:
        opt = int(opt)
        advancing_method = solution_advancing_factory.get_advancement_option(opt)
    except ValueError:
        advancing_method = solution_advancing_factory.get_advancement_option(1)

    options_text = solution_factory.get_options_with_desc_text()
    while True:
        print("Select a startegy to visualize")
        print(options_text)
        option = input()
        if option.lower() == "q":
            break
        try:
            option = int(option)
            solution = solution_factory.get_solution(
                option, samples_array[i], advancing_method
            )
            solution.solve()
            print("Enter q to quit, anything else to exit")
            quit_option = input()
            if quit_option.lower() == "q":
                break
        except ValueError:
            print(
                "Invalid option was passed, plase select a valid option or enter q to exit"
            )


main()
