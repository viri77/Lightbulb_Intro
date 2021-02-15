from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    vremja = 0
    k = els
    # от 6-5, от 4-3, от 2-1
    for i in range(1, len(k), 2):
        vremja += ((k[i] - k[i - 1]).seconds)
        vremja += ((k[i] - k[i - 1]).days) * 86400
    return vremja
