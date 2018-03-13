# coding: utf-8
import pandas as pd

one_df = pd.DataFrame({
    'record': [2, 3, 4, 5]
})

two_df = pd.DataFrame({
    'record': [2.0, 3.0],
    'you': ["ccc", "8787"]
})

three_df = pd.DataFrame({
    'record': [4, 5],
    'you': ["ccc", "ooooo"]
})

# print(one_df.dtypes)
# print(two_df.dtypes)



c_df = pd.merge(one_df, three_df)
print(c_df)

f_df = pd.merge(one_df, two_df)
print(f_df)

k_df = pd.concat([c_df, f_df])
print(k_df)

should_columns = list(k_df.columns.values)
print(should_columns)
should_columns = should_columns + ["value"]
final_field_data = pd.DataFrame(columns=should_columns)
print(final_field_data)
