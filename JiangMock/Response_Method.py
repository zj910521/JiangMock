import json
import re
from random import *


class Responst_Method:

    @classmethod
    def Traverse_response(cls,response_data):
        data = json.loads(response_data)
        for i in data:
            data[i] = cls.Replace_data(data[i])
        return data

    @classmethod
    def Replace_data(cls,data):
        if re.search("random",data):
            ret = re.search("random(.*)", data)
            start = data[0:ret.start()]
            end = data[ret.end()::]
            ret1 = re.search(r"\(.*\)",data)
            randomParameter = ret1.group()[1:-1].split(",")
            if len(randomParameter)>1 :
                return start+str(randint(int(randomParameter[0]),int(randomParameter[1])))+end

        return data
