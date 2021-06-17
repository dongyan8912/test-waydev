# _*_
# coding: utf-8 _*_


import urllib
from urllib import request
import util
from urllib import error


filename = "test2.xlsx"
sheet_name = "Sheet"


def send_request_urllib(request_obj):

    activity = {
        "activity_id": request_obj["activity_id"]
    }

    query = urllib.parse.urlencode(activity)

    url = request_obj["url"] + "?" + query

    url = url.format(series=request_obj["series"])

    headers = {
        'appname': request_obj["app_name"],
        'apptoken': request_obj["app_token"]
    }

    data = {"avatar": request_obj["avatar"]}
    data = bytes(urllib.parse.urlencode(data), 'utf8')

    req = request.Request(url=url, data=data, headers=headers)

    code = ""

    try:
        response = request.urlopen(req)
    except error.HTTPError as e:
        print(e.code)

        code = e.code
        print(e.read().decode('utf8'))

    return code


wb, sheet, row, request_obj = util.read_excel(filename, sheet_name)
send_request_urllib(request_obj)

row[7].value = send_request_urllib(request_obj)

util.modify_file(wb, sheet, u"接口测试", filename)