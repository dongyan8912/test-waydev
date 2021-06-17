# _*_
# coding: utf-8 _*_


import util

import requests


filename = "test.xlsx"
sheet_name = "Sheet"


def send_request_requests(request_obj):

    url = request_obj["url"] + "?" + "activity_id=" + str(request_obj["activity_id"])

    url = url.format(series=request_obj["series"])

    print(url)

    headers = {
        'appname': request_obj["app_name"],
        'apptoken': request_obj["app_token"]
    }

    data = {"avatar": request_obj["avatar"]}

    response = requests.post(url, data=data, headers=headers)

    print(response.status_code)
    print(response.json())

    return response.status_code

wb, sheet, row, request_obj = util.read_excel(filename, sheet_name)

row[7].value = send_request_requests(request_obj)

util.modify_file(wb, sheet, u"接口测试", filename)
