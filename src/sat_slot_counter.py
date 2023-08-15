import os

from importer import File
from slots import Period
from collections import deque
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
        usage="\nThis program finds the most used time slots in a given list of time intervals. "
        "\n\nEnter the relative filepath to load the datafile containing time intervals."
    )
    parser.add_argument(
        "file", help="Enter relative filepath to satellite timestamp data"
    )
    args = parser.parse_args()

    # split given filepath in path and name
    *fpath, fname = args.file.split("/")

    data = File.load(filepath="/".join(fpath), filename=fname)

    data = data.sort_values(by=["start"], ascending=True)

    # create periods object from sorted start and end time data
    # use deque for simpler recursion
    periods = deque(
        [Period(start, end) for start, end in zip(data["start"], data["end"])]
    )
    # for future improvement:
    # cluster data before next step, to find clusters of data that dont overlap at all
    # parallelize calculation of overlapping and merged time windows

    # automatically increase python maximum recursion limit depending on length of timestamp data
    sys.setrecursionlimit(len(periods) * 2)

    # find all time slots and number of satellites visible during this time
    slots = Period.find_slots(periods, slots=[])
    for s in slots:
        print(s)


if __name__ == "__main__":
    main()
