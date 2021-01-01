class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_by_first = {piece[0]: piece for piece in pieces} # TODO: handle empty pieces
        in_piece = False # go in peace
        curr_piece = []
        curr_piece_i = 0
        for num in arr:
            if in_piece:
                if num != curr_piece[curr_piece_i]:
                    return False
                curr_piece_i += 1
            elif num in pieces_by_first:
                curr_piece = pieces_by_first[num]
                curr_piece_i = 1
                in_piece = True
            else:
                return False
            if curr_piece_i >= len(curr_piece):
                in_piece = False
        return True # given lengths match
