# coding: utf-8

import random

names = ["CRC岗位培训", "CDISC之SDTM", "数据管理", "数据管理", "监查员岗位培训", "项目经理岗位培训", "稽查员岗位培训", "待定", "临床试验统计学基础", "临床研究基础",
         "临床研究基础", "项目管理", "统计分析", "医学写作", "CRA培训", "SOP"]

print(random.sample(names, 5))
print([random.choice(names) for i in range(1, 100)])
