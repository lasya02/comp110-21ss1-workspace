from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open("survey", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return a column's values."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert a table of rows to a table of columns."""
    result: dict[str, list[str]] = {}
    keys = table[0].keys()
    for key in keys:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Get the first n rows."""
    result: dict[str, list[str]] = {}
    for key in table:
        result[key] = table[key][:rows]
    return result


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Select only a subset of columns."""
    result: dict[str, list[str]] = {}
    for col in cols:
        result[col] = table[col]
    return result


def count(list: list[str]) -> dict[str, int]: 
    """Counts items in a list."""
    result: dict[str, int] = {}
    for keys in list: 
        if keys not in result: 
            result[keys] = 1 
        else: 
            result[keys] += 1
    return result 


DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/survey.csv"

table = read_csv_rows(DATA_FILE_PATH)

data_cols: dict[str, list[str]] = columnar(table)

for keys in data_cols: 
    print(keys)

import select
column_interest: dict[str,list[str]] = select(data_cols, ["row_number", "section", "ls_effective"])


from tabulate import tabulate
printing = head(column_interest, 5)
tabulate(printing, printing.keys(), "html")


synch: list[str] = []
i: int = 0
sync_values: list[str] = select[data_cols,"section"]
effective_values: list[str] = select[data_cols,"effective"]
while i < len(sync_values):
    if sync_values[i] == "Section 1 - 3:30pm - Sync + Async":
        synch.append(effective_values[i])
        i += 1

print(head(synch,8))


# diffculties_no_prior_exp: list[str] = [ ]
# i = 0
# # extract the experience column from parameter data
# experience_values: list[str] = data["prior_exp"]
# # extract the difficulty column from parameter data
# difficulty_values: list[str] = data["difficulty"]
# while i < len(experience_values):
#     if experience_values[i] == "None to less than one month!":
#         diffculties_no_prior_exp.append(difficulty_values[i]
#     i += 1

# return diffculties_no_prior_exp