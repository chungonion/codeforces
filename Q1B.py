import re
import string


def q2(size, list):
    regex_1 = "R(\d+)C(\d+)"
    regex_2 = "([A-Z]+)(\d+)"

    for _ in range(0, size):
        element = input()
        regex_obj = re.match(regex_1, element)
        if regex_obj:  # in R1C1 format
            row_column = re.findall(r'\d+', element)
            row = int(row_column[0])
            column = int(row_column[1])
            # print("Row: {}, Column: {}".format(row, column))
            new_row_column = ""

            iter_column = column

            while iter_column > 0:
                letter_index = iter_column % 26
                new_row_column = "{}{}".format(
                    string.ascii_uppercase[letter_index-1], new_row_column)
                iter_column -= 1
                iter_column //= 26

            new_row_column = "{}{}".format(new_row_column, row)

            # result append
            list.append(new_row_column)
            # print(list)

        else:  # already in XYZ123 format
            regex_obj = re.match(regex_2, element)

            if regex_obj:
                column_letters = re.findall(r"[a-zA-Z]+", element)[0]
                row_numbers = re.findall(r'\d+', element)[0]
                column_number = 0
                column_letters = column_letters[::-1]
                # print(str(column_letters))
                exponent = 0
                for i in column_letters:
                    column_number += (string.ascii_uppercase.index(i)+1) * (26**exponent)
                    # print("column number: {}".format(column_number))
                    exponent += 1
                new_row_column = "{}{}{}{}".format(
                    "R", row_numbers, "C", column_number)
                list.append(new_row_column)
                # while True:
                # print(new_row_column)
            else:
                pass  # result ignore


def q2print(list):
    for element in list:
        print(element)


input_size = int(input())
list = []
q2(input_size, list)
q2print(list)
