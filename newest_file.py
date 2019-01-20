#encoding: utf-8
import os
from enum import Enum, unique

# 报告文件排序规则
class SortRule(Enum):
    MTIME = 0
    FNAME = 1

# 最新报告获取类
class NewestResult(object):
    """
    The NewestResult class.

    :param result_dir: 测试报告默认存放的目录

    :param sort_rule: 排序规则，默认按时间排序，取最新的文件
        SortRule.MTIME：报告生成或修改时间排序
        SortRule.FNAME：报告名称排序
    """
    def __init__(self, result_dir, sort_rule=SortRule.MTIME):
        
        self.result_dir = result_dir
        self.sort_rule = sort_rule
    
    def get_newest(self):
        lists = os.listdir(self.result_dir)
        if self.sort_rule == SortRule.FNAME:
            lists.sort(key=lambda fn: os.path.basename(self.result_dir+'\\'+fn))
        else:
            lists.sort(key=lambda fn: os.path.getmtime(self.result_dir+'\\'+fn))
        file = os.path.join(self.result_dir, lists[-1])
        return file
    
if __name__ == "__main__":
    newresult = NewestResult('D:\\Result', SortRule.FNAME)
    print newresult.get_newest()
