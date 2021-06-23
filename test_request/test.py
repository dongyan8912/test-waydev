# _*_
# coding: utf-8 _*_

import json
import os


# 测试添加注释

#test_json = [{"group": "1、安全组织、制度与流程", "title": "是否设立了首席安全官或同等职务的安全负责人？", "id":"q1", "check": true, "text": "这是说明"},{"group": "1、安全组织、制度与流程", "title": "是否设立了专门的信息安全部门或有同等职能的部门？是否配备了专职的信息安全人员？", "id": "q2", "check": false, "text": ""},{"group": "2、人员安全", "title": "人员录用、离职、调岗、解雇时，是否有明确的信息系统权限授权与撤销的制度？", "id": "q3", "check": true, "text": "这是说明"}]

# f = json.dumps(test_json)
# print(type(f))


a = 0

b = 1 and 0

c = 1 > 0


def read_gor():

    # file = open("/Users/dongyanyan/Desktop/goreplay/discovery-test.gor","r")

    file = open("/Users/dongyanyan/Desktop/goreplay/discovery-bt6pz-requests-6.22.gor", "r")
    data = file.read()
    data_list = data.split("🐵🙈🙉")
    dict_gor = {}
    print(len(data_list))
    for line_data in data_list:
        line_list = line_data.split("\n")
        for l in line_list:
            if l is not '' and (l[0] == '1' or l[0] == '2'):
                uuid = l[2:27]
                if uuid not in dict_gor:
                    dict_gor[uuid] = 1
                else:
                    dict_gor[uuid] += 1
                continue
    print(dict_gor)

    p_num = 0
    for key in dict_gor:
        if dict_gor[key] == 2:
            p_num += 1

    print('pi pei shu liang:', p_num)


read_gor()

