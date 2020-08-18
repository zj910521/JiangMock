import json


class Validator:
    '''
    验证方法
    '''
    @classmethod
    def check_data(cls,search_obj,data):
        check = ""
        for i in search_obj:
            check = True
            for j in data:
                try:
                    if j not in i.request_data or data.get(j) != json.loads(i.request_data)[j]:
                        check = False
                except KeyError:
                    check = False
            if check == True:
                return i.response_data
        if check == False:
            return "找不到相关返回配置"