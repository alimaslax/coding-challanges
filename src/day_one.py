# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'plusMinus' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #
#
# def plusMinus(arr):
#     size = len(arr)
#     countPos = 0;
#     countNeg = 0;
#     countZero = 0;
#     for i in range(size):
#         if 0 < arr[i]:
#             countPos += 1
#         if 0 > arr[i]:
#             countNeg += 1;
#         if 0 == arr[i]:
#             countZero += 1;
#     # Write your code here
#     print(format(countPos / size, ".6f"))
#     print(format(countNeg / size, ".6f"))
#     print(format(countZero / size, ".6f"))
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)

# !/bin/python3

# import math
# import os
# import random
# import re
# import sys


# #
# # Complete the 'miniMaxSum' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #
#
# def miniMaxSum(arr):
#     min = 0;
#     max = 0;
#     arr.sort()
#     for i in range(0, 4):
#         min += arr[i]
#         max += arr[4 - i]
#     print(f"{min} {max}")
#
#
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
#
#     miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # [hour, minute, second AM/PM]
    time = s.rsplit(':')
    if len(time) != 3:
        return;
    isPM = time[2][-2:] == "PM"
    # seconds reformat
    time[2] = time[2][:2]
    hour = int(time[0])
    min = time[1]
    sec = time[2]
    if isPM and hour != 12:
        hour += 12;
    if not isPM and hour == 12:
        hour -= 12;
    if hour >= 10:
        return f"{hour}:{min}:{sec}"
    else:
        return f"0{hour}:{min}:{sec}"

if __name__ == '__main__':
    print ( timeConversion("01:40:22AM"))