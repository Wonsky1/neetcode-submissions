from collections import defaultdict
class Solution:
    def is_empty(item: str) -> bool:
        if item == ".":
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = {
            # ROW_ID: {}
        }
        columns_dict = {
            # COLUMN_ID: {}
        }
        square_dict = defaultdict(set)
        # for row_index, row in enumerate(board):
        #     for column_index, item in enumerate(row):
        #         board_dict[(column_index, row_index)] = item
        # print(board_dict)
        
        # for row_index in range(9):
        #     for column_index in range(9):
        #         if 
        for row_index, row in enumerate(board):
            # rows_dict[index] = {}
            # columns_dict[index] = {}
            for column_index, item in enumerate(row):
                if item == ".":
                    continue
                if not rows_dict.get(row_index):
                    rows_dict[row_index] = {item}
                else:
                    # rows_dict[row_index].add(item)
                    
                    if item in rows_dict[row_index]:
                        return False

                    rows_dict[row_index].add(item)
                # columns
                if not columns_dict.get(column_index):
                    columns_dict[column_index] = {item}
                else:
                    if item in columns_dict[column_index]:
                        return False
                    
                    columns_dict[column_index].add(item)
                
                # squares
                item_square_id = (row_index // 3) * 3 + (column_index // 3)
                if item in square_dict[item_square_id]:
                    return False
                
                square_dict[item_square_id].add(item)


                # print(index, item_index)
                # print(item_square_id)
                # board_dict[(item_index, index)] = item
        # print(rows_dict)
        # print("--------")
        # print(columns_dict)
        # print(board_dict)

        # for item_coords, item in board_dict.items():

        return True




