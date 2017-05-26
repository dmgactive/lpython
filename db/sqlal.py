# coding: utf-8

import sqlalchemy
import inspect
from inspect import ArgSpec
from sqlalchemy import MetaData
from sqlalchemy import (Enum, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint, UniqueConstraint, Table,
                        Column)
from sqlalchemy.engine.reflection import Inspector

from sqlalchemy.orm import sessionmaker

m = 'mysql+mysqlconnector://root:123456@192.168.1.139/temp'

mysql_engine = sqlalchemy.create_engine(m)

mysql_meta = MetaData(bind=mysql_engine)

mysql_columns = []
# column = Column("what", sqlalchemy.dialects.mysql.INTEGER(11), comment="这是什么")
# mysql_columns.append(column)
#
# mysql_table = Table("t_comment", mysql_meta,
#                     *mysql_columns, mysql_engine='InnoDB', mysql_charset='utf8')
#
# mysql_table.create(mysql_engine)

connection = mysql_engine.connect()
Session = sessionmaker(bind=connection)
session = Session()
conn = session.connection().connection
cursor = conn.cursor()

for result in cursor.execute('''
create table if not exists pv_report (
           hub_pv_report_id  varchar(50) NOT NULL,
           company_tm_id  varchar(50) NOT NULL,
           pv_report_tm_id  varchar(50) NOT NULL,
           report_type varchar(50) comment '企业报告类型',
           source_type varchar(50) comment '企业信息来源',
           is_new varchar(20) comment '是否新的',
           is_invalid int comment'是否无效',
           is_delete int comment '是否删除',
           report_number varchar(200) comment '报告号码',
           serial_number varchar(50) comment '报告序列号',
           receive_date datetime comment '收到报告日期',
           drug_name_cn varchar(500) comment '药品名',
           generic_name_cn varchar(500) comment '通用名（中文）',
           brand_name_cn varchar(500) comment '商品名（中文）',
           brand_name_en varchar(500) comment '商品名（英文）',
           active_ingredients varchar(500) comment '活性成分',
           formulation varchar(500) comment '剂型',
           adverse_event_name_cn varchar(200) comment '不良事件名称',
           adverse_event_name_soc  varchar(200) ,
           adverse_event_name_pt  varchar(200) ,
           gender varchar(10) comment '性别',
           birthday varchar(20) comment '生日',
           project_number varchar(500) comment '项目编号',
           project_name varchar(300) comment '研究方案名称'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        create table if not exists hub_company
        (
            hub_company_id varchar(50) primary key not null,
            company_tm_id varchar(50) not null,
            load_dts datetime not null,
            record_source varchar(100) not null
        )engine=InnoDB default charset=utf8;
''', multi=True):
    pass

session.close()
