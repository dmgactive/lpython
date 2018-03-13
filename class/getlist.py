# coding: utf-8

import pandas as pd
import random

num = 5

test_data = pd.DataFrame(
    {
        'company_guid': [2, 4, 9, 2, 3],
        'rereview_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'answer_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'close_query_query_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'allocate_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'first_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'second_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        # 'judge_avg_duration': [random.randint(1, 2880) for i in range(0, num)]
    }
)
print(test_data)

dict = {row["company_guid"]: row["rereview_avg_duration"] for index, row in test_data.iterrows()}

print(dict)
