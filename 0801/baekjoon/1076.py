table = {"black": [0, 1], 
            "brown": [1, 10],
            "red": [2, 100],
            "orange": [3, 1000],
            "yellow": [4, 10000],
            "green": [5, 100000],
            "blue": [6, 1000000],
            "violet": [7, 10000000],
            "grey": [8, 100000000],
            "white": [9, 1000000000]
        }

ret = (table[input()][0] * 10 + table[input()][0]) * table[input()][1]
print(ret)