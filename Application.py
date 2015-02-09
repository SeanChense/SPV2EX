# -*- coding: utf-8 -*-
from account import *
from AutoBBS import AutoBBS
from Domain import Domain
from get_job_on_v2ex import JobInfo


# 登录河畔
domain = Domain(hostname = 'bbs.uestc.edu.cn')
autobbs = AutoBBS(domain = domain, userName = AccountDict["username"], passWord = AccountDict["pwd"])
autobbs.login()

#获取信息
ji = JobInfo("http://v2ex.com/?tab=jobs")
content = ji.scrapyInfoFromV2ex()
postList = ji.getPostList(content)
postContent = ji.getPostContent(postList[0]["url"])


#发帖
# autobbs.new(fid = "214", subject = postList[0]["title"], message = postContent)
