# between every 2 nearest rows with security devices, there are n1*n2 laser beams,
# where n1 is the number of devices on the earlier row and n2 the number on the later row.
# so just remember the number for the last row that had devices and keep a running total.

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_lasers = 0
        last_nonblank_row_count = 0
        for row in bank:
            curr_row_count = row.count('1')
            if curr_row_count > 0:
                # on the first nonblank row it'll add 0 but that's fine
                total_lasers += curr_row_count * last_nonblank_row_count
                last_nonblank_row_count = curr_row_count
        return total_lasers
