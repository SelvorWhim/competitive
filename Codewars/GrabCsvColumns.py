def csv_columns(csv, indices):
    rows = csv.split() # whitespace includes linebreak
    num_cols = rows[0].count(',') + 1 if rows else 0
    if all(i < 0 or i >= num_cols for i in indices): # if any invalid index
        return ''
    selected_rows = []
    for row in rows:
        row = row.split(',')
        new_row = ','.join([row[i] for i in indices if i>=0 and i<num_cols])
        selected_rows.append(new_row)
    return '\n'.join(selected_rows)
    '\n'.join(selected_rows)