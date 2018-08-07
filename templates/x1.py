#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/18

import re

db_url = "^/userinfo/$"
current_url = "/userinfo/add/"

result = re.match(db_url,current_url)
print (bool(result))
