from __future__ import annotations


class Period:
    """
    Period class handling time periods. A period consists of a start and end time. The n_sats counter will be increased,
    if two time periods overlaps, which means, that another satellite is visible during this time.
    """

    def __init__(self, start: float, end: float, n_sats: int = 1):
        self.start = start
        self.end = end
        self.n_sats = n_sats

    def __str__(self):
        return f"{self.start}-{self.end};{self.n_sats}"

    def overlap(self, other: Period) -> bool:
        """
        Checks if current period has an overlap with another period.
        :param other: Period
        :return: bool
            True, if two periods overlap
        """
        if self.start <= other.end and other.start <= self.end:
            return True
        else:
            return False

    def overlap_period(self, other: Period) -> Period:
        """
        Generates the overlapping time period of two periods. It instantiates another Period object with an increased
        counter for the number of overlapping time slots merged in this period.
        :param other: Period
        :return: Period
        """
        start, end = self.start, self.end
        if self.start <= other.start:
            start = other.end
        if self.end >= other.end:
            end = other.end
        return Period(start, end, self.n_sats + 1)

    @classmethod
    def find_slots(cls, periods: "deque", slots: list):
        """
        Recursive algorithm to find overlapping periods.

        If there is more than one period in the periods deque, the first two elements of the deque are taken from the
        deque.
        If these two periods are overlapping, they will be merged. This merged Period, with the overlapping time window,
        will then be appended to the left side of the deque and the function is called again with the updated deque.
        If the first two Periods do not overlap, the first of these two will be written written into the Slots list.
        The other will be appended back to the left side of the deque.

        Once the deque is empty, all Periods, merged or not, should be in the Slots list.

        The intuitive solution of comparing and merging overlapping periods emerges from a graphical solution of finding
        the longest vertical path through a set of time windows.

        ===

        The graphic below shows the result after two iterations. Three Periods were merged due to the overlap in time
        windows. The vertical path from A to C is the longest possible vertical path originating from time slot A.

        A=============|======================|A\n
        \tB==========|======================|========B\n
        \t\tC=======|======================|===C\n



        :param periods: deque
        :param slots: list
        :return:
        """
        if len(periods) > 1:
            # take first two elements
            p1, p2 = periods.popleft(), periods.popleft()
            if p1.overlap(p2):
                # merge periods
                periods.appendleft(p1.overlap_period(p2))
                return cls.find_slots(periods, slots)
            else:
                # put second period back
                periods.appendleft(p2)
                # append the other to slots
                slots.append(p1)
                return cls.find_slots(periods, slots)
        else:
            # put the last element to the slots, as well
            slots.append(periods.pop())
            return slots
