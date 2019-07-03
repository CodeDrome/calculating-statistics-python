import statistics
import random


def main():

    """
    Create a set of random data
    and use the statistics class to calculate and print statistics.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Statistics    |")
    print("-----------------\n")

    s = statistics.Statistics()

    data = []
    for i in range(0, 12):
        data.append(random.randint(1, 128))

    s.data = data

    s.calculate()

    s.output_data()

    s.output_statistics()


main()
