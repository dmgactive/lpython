# coding: utf-8
import pandas as pd
import random
import sqlalchemy

# pandas print显示不换行
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)
pd.options.display.max_colwidth = 0

# 创建pandas dataframe，初始化有值

family_names = ["李", "王", "张", "刘", "陈", "杨", "黄", "赵", "吴", "周", "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "罗", "郑",
                "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹", "彭", "曾", "萧", "田", "董", "潘", "袁", "于", "蒋", "蔡", "余", "杜",
                "叶", "程", "苏", "魏", "吕", "丁", "任", "沈", "姚", "卢", "姜", "崔", "钟", "谭", "陆", "汪", "范", "金", "石", "廖", "贾",
                "夏", "韦", "傅", "方", "白", "邹", "孟", "熊", "秦", "邱", "江", "尹", "薛", "阎", "段", "雷", "侯", "龙", "史", "陶", "黎",
                "贺", "顾", "毛", "郝", "龚", "邵", "万", "钱", "严", "覃", "河", "戴", "莫", "孔", "向", "汤"]

names = ["采", "用", "中", "流", "作", "堰", "的", "方", "法", "在", "岷", "江", "峡", "内", "用", "石", "块", "砌", "成", "石", "埂", "叫",
         "都", "江", "鱼", "嘴", "都", "江", "堰", "也", "叫", "分", "水", "鱼", "嘴", "鱼", "嘴", "是", "一", "个", "分", "水", "的", "建",
         "筑", "工", "程", "把", "岷", "江", "水", "流", "一", "分", "为", "二", "东", "边", "的", "叫", "内", "江", "供", "灌", "溉", "渠",
         "用", "水", "西", "边", "的", "叫", "外", "江", "是", "岷", "江", "的", "正", "流", "又", "在", "灌", "县", "城", "附", "近", "的",
         "岷", "江", "南", "岸", "筑", "了", "离", "碓", "同", "堆", "离", "碓", "就", "是", "开", "凿", "岩", "石", "后", "被", "隔", "开",
         "的", "石", "堆", "夹", "在", "内", "外", "江", "之", "间", "离", "碓", "的", "东", "侧", "是", "内", "江", "的", "水", "口", "称",
         "宝", "瓶", "口", "具", "有", "节", "制", "水", "流", "的", "功", "用", "夏", "季", "岷", "江", "水", "涨", "都", "江", "鱼", "嘴",
         "淹", "没", "了", "离", "碓", "就", "成", "为", "第", "二", "道", "分", "水", "处", "内", "江", "自", "宝", "瓶", "口", "以", "下",
         "进", "入", "密", "布", "于", "川", "西", "平", "原", "之", "上", "的", "灌", "溉", "系", "统", "", "", "旱", "则", "引", "水",
         "浸", "润", "雨", "则", "杜", "塞", "水", "门", "华", "阳", "国", "志", "蜀", "志", "保", "证", "了", "大", "约", "万", "亩", "良",
         "田", "的", "灌", "溉", "使", "成", "都", "平", "原", "成", "为", "旱", "涝", "保", "收", "的", "天", "府", "之", "国", "都", "江",
         "堰", "的", "规", "划", "设", "计", "和", "施", "工", "都", "具", "有", "比", "较", "好", "的", "科", "学", "性", "和", "创", "造",
         "性", "工", "程", "规", "划", "相", "当", "完", "善", "分", "水", "鱼", "嘴", "和", "宝", "瓶", "口", "联", "合", "运", "用", "能",
         "按", "照", "灌", "溉", "防", "洪", "的", "需", "要", "分", "配", "洪", "枯", "水", "流", "量"]

companys = ["嘉兴太美医疗科技有限公司", "ABC", "龙湖公司"]

course_cats = ["CRC岗位培训", "CDISC之SDTM", "数据管理", "数据管理", "监查员岗位培训", "项目经理岗位培训", "稽查员岗位培训", "待定", "临床试验统计学基础", "临床研究基础",
               "临床研究基础", "项目管理", "统计分析", "医学写作", "CRA培训", "SOP"]

courses = ["临床试验体系培训/通用基础知识培训", "临床试验进阶课程", "临床试验岗位培训", "医学专员初级课程", "医学专员中级课程", "医学专员高级课程", "药物警戒培训课程第I级课程",
           "药物警戒培训课程第II级课程", "药物警戒培训课程第III级课程", "药物警戒培训课程第IV级课程", "药物警戒培训课程第V级课程", "监测流程—调查和统计", "UMC信号检测流程", "药物警戒的意义",
           "ADR处理", "编码术语", "自发报告", "疫苗的安全性监测"]

occupations = ["运维", "项目经理", "产品经理", "助理"]

parts = ["临床研究事业部", "研发部", "药物检测部"]

tms_data = pd.DataFrame(
    {'name': [random.choice(family_names) + random.choice(names) for i in range(1, 100)],
     'gender': [random.randint(1, 300) for i in range(1, 100)],
     'phone': [random.random() for i in range(1, 100)],
     'company': [random.choice(companys) for i in range(1, 100)],
     'part': [random.choice(parts) for i in range(1, 100)],
     'occupation': [random.choice(occupations) for i in range(1, 100)],
     'course_category': [random.choice(course_cats) for i in range(1, 100)],
     'course': [random.choice(courses) for i in range(1, 100)],
     'rate': [random.random() for i in range(1, 100)],
     }
)

# pandas dataframe 0 行
one_row_df = pd.DataFrame({
    "Id": "kjk",
    "IdCreateUser": "cc",
    "CreateTime": "kjk",
    "IdHospital": "99",
    "IdEnvironment": "hhh",
    "IdCRFVersion": "6",
    "IdPatientStatusType": "000",
    "IsDelete": 0,
    "EntryStatus": 1,
    "IsQuery": 0,
    "IsSignature": 0,
    "IsChecked": 0,
    "IsLocked": 0,
    "IsVerification": 0,
    "IsFreeze": 0
}, index=[0])

# 空的 pandas dataframe
should_columns = ["IdCreateUser", "EntryStatus", "IsQuery"]
final_field_data = pd.DataFrame(columns=should_columns)

# 获得某行某列数据
one_name = tms_data.ix[0]["name"]
print(one_name)

# 重命名某列
tms_rename_data = tms_data.rename(index=str, columns={"Phone": "phone_number"})

# padans to sql 定义类型
report_engine = ""
user_csv_df = pd.DataFrame({
    "user_id": "kjk",
    "UserId": "cc"
}, index=[0])
user_csv_df.to_sql("user_data", report_engine, if_exists='replace', index=False,
                   chunksize=5000,
                   dtype={'user_id': sqlalchemy.sql.sqltypes.INT, 'UserId': sqlalchemy.sql.sqltypes.VARCHAR(50)})

# pandas 字典话，迭代
tms_dict = {row["name"]: row for index, row in tms_data.iterrows()}
