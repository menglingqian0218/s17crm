# class Foo(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
# obj = Foo('alex')
# print(obj,type(obj))

import re

db_url = "^/userinfo/$"

current_url = "/userinfo/"

result = re.match(db_url,current_url)
print(bool(result))