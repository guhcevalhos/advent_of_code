from typing import List

# Find the two entries that sum to 2020 and then multiply those two numbers together.
# Ex: input = [1721, 979, 366, 299, 675, 1456]

def day1_part1(input: List[int]) -> int:

    # Approach 1: Brute Force
    # Time: O(N**2)
    # Space: O(1)
    '''
    for index, item1 in enumerate(input):
        for item2 in input[index:]:
            if item1 + item2 == 2020: return item1 * item2
    '''

    # Approach 2: Two-sum
    # Time: O(N)
    # Space: O(N)
    '''
        - With a dictionary we can make the Time Complexity drop, however at cost of space.
        - We can go over each entry in the list and see if we have already found someone that is looking for this number (the complement) in the dictionary.
            - If yes, we have already found our number.
            - If not, we just need to store the complement to our current number.
    '''
    lookup = {}

    for index, number in enumerate(input):
        if number in lookup: return number * input[lookup[number]]
        lookup[2020 - number] = index

def day1_part2(input: List[int]) -> int:

    # Approach 1: Brute Force
    # Time: O(N**3)
    # Space: O(1)
    '''
    for i, item1 in enumerate(input):
        for j, item2 in enumerate(input[i:]):
            for item3 in input[j:]:
                if item1 + item2 + item3 == 2020: return item1 * item2 * item3
    '''
    # Approach 2: Three-sum
    # Time: O(N**2)
    # Space: O(1)
    '''
        - When we have three numbers, the approach is a bit different, instead of a dictionary, we will sort our input and use two-pointer to find the target number.
        - After sorting, we start by fixing our first element and then using two pointers, left and right (each at each extreme of the remaining sub-array)
        - If the sum of fixed + left + right < 2020, it means we need to increase it, so we move left one position to the right.
        - If the sum of fixed + left + right > 2020, it means we need to decrease it, so we move right one position to the left.
    '''

    input.sort()

    for index, fixed_number in enumerate(input):
        
        left = index + 1
        right = len(input) - 1

        while left < right:

            if fixed_number + input[left] + input[right] == 2020: return fixed_number * input[left] * input[right]
            elif fixed_number + input[left] + input[right] < 2020: left += 1
            else: right -= 1


input = [1713,1281,1185,1501,1462,1752,1363,1799,1071,1446,1685,1706,1726,1567,1867,1376,1445,1971,1429,1749,438,1291,1261,1585,1859,1835,1630,1975,1467,1829,1669,1638,1961,1719,1238,1751,1514,1744,1547,1677,1811,1820,1371,740,1925,1803,1753,1208,1772,1642,1140,1838,1444,1321,1556,1635,1687,688,1650,1580,1290,1812,1814,1384,1426,1374,1973,1791,1643,1846,1676,1724,1810,1911,1765,945,1357,1919,1994,1697,1632,1449,1539,1725,1963,1879,1731,1904,1392,1823,1420,1504,204,1661,1575,1401,1806,1417,1965,1960,1990,1409,1649,1566,1957,514,1464,1352,1841,1601,1473,1309,1421,1190,1582,1825,655,1666,1878,1891,1579,1176,1557,1910,1747,1388,1493,1372,1522,1515,1745,1494,1763,1147,1364,1469,1165,1901,1368,1234,1308,1416,1678,1541,1509,1427,1223,1496,1600,1383,1295,1415,1890,1694,1793,1529,1984,1576,1244,1348,1085,1770,1358,1611,1159,1964,1647,818,1246,1458,1936,1370,1659,1923,1619,1604,1354,1118,1657,1945,1898,1948,798,769,1689,1821,1979,1460,1832,1596,1679,1818,1815,1977,1634,1828,1386,1284,1569,1970]
print(day1_part1(input))
print(day1_part2(input))