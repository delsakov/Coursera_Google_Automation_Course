#!/usr/bin/env python3

import re
import operator
import csv

er_dict = {}
er_lst = []
er_sorted_dict = {}
user_dict = {}
user_dict_sorted = {}
users_list = []
user_error = {}
user_info = {}

def main():
    with open("syslog.log", "r") as log_file:
        lines = log_file.readlines()
        for line in lines:
            print('line: ', line.strip())
            pattern = r"ERROR ([\w ']*) "
            result = re.search(pattern, line.strip())
            if result is not None:
                if result.group(1) in er_dict.keys():
                    er_dict[result.group(1)] += 1
                else:
                    er_dict[result.group(1)] = 1
            pattern_2 = r"ticky: (ERROR|INFO) ([\w \[\]#']*) \(([\w.]*)\)$"
            result_2 = re.search(pattern_2, line.strip())
            if result_2 is not None:
               # print('result_2.group(1): ', result_2.group(1))
               # print('result_2.group(2): ', result_2.group(2))
               # print('result_2.group(3): ', result_2.group(3))
                if result_2.group(3) not in user_error.keys() and result_2.group(1) == 'ERROR':
                    user_error[result_2.group(3)] = 1
                elif result_2.group(3) not in user_info.keys() and result_2.group(1) == 'INFO':
                    user_info[result_2.group(3)] = 1
                elif result_2.group(3) in user_error.keys() and result_2.group(1) == 'ERROR':
                    user_error[result_2.group(3)] += 1
                elif result_2.group(3) in user_info.keys() and result_2.group(1) == 'INFO':
                    user_info[result_2.group(3)] += 1

    for k,v in user_error.items():
        if k not in user_dict.keys():
            user_dict[k] = {'INFO': 0, 'ERROR': v}
        else:
            user_dict[k]['ERROR'] = v

    for k,v in user_info.items():
        if k not in user_dict.keys():
            user_dict[k] = {'INFO': v, 'ERROR': 0}
        else:
            user_dict[k]['INFO'] = v

   # print('user_dict: ', user_dict)
    user_dict_sorted = sorted(user_dict.items(), key = operator.itemgetter(0))

   # print('user_dict_sorted: ', user_dict_sorted)
    users_list.append(['Username', 'INFO', 'ERROR'])
    for k,v in user_dict_sorted:
        users_list.append([k, v['INFO'],  v['ERROR']])

    er_sorted_dict = sorted(er_dict.items(), key = operator.itemgetter(1), reverse=True)
    log_file.close()
    er_lst.append(['Eror', 'Count'])
    for k,v in er_sorted_dict:
        er_lst.append([k,v])
    with open("error_message.csv", "w") as error_file:
        writer = csv.writer(error_file)
        writer.writerows(er_lst)
    with open("user_statistics.csv", "w") as users_file:
        writer = csv.writer(users_file)
        writer.writerows(users_list)
    error_file.close()


main()
