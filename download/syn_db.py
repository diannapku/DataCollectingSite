import os
from .models import ProjectInfo


class SynDB:

    @staticmethod
    def get_dir_size(file_path, size=0):
        for root, dirs, files, in os.walk(file_path):
            for file in files:
                size += os.path.getsize(os.path.join(root, file))
        return size

    @staticmethod
    def get_file_cnt(file_path, flag_str, length=0):
        for root, dirs, files, in os.walk(file_path):
            for file in files:
                if file.find(flag_str) >= 0:
                    length += 1
        return length

    @staticmethod
    def syn_db():
        ProjectInfo.objects.all().delete()

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.BugzillaCrawler'
        pro_list = os.listdir(path)
        for proj in pro_list:
            size = SynDB.get_dir_size(path+'/'+proj) // (1024*1024)
            file_cnt = SynDB.get_file_cnt(path+'/'+proj, '.xml')
            ProjectInfo.objects.create(name=proj.lower(), type='BUGZILLA', path=path+'/'+proj,
                                       files_cnt=file_cnt, size=size)

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.GitCrawler'
        pro_list = os.listdir(path)
        for proj in pro_list:
            dir = os.listdir(path + '/' + proj)
            for dir_name in dir:
                ProjectInfo.objects.create(name=dir_name, type='GIT', path=path + '/' + proj + '/' + dir_name)
                ProjectInfo.objects.create(name=dir_name, type='CODE',
                                           path='{0}/{1}/{2}/{3}GIT'.format(path, proj, dir_name, dir_name))

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.JiraIssueCrawler'
        pro_list = os.listdir(path)
        for proj in pro_list:
            size = SynDB.get_dir_size(path + '/' + proj) // (1024 * 1024)
            file_cnt = SynDB.get_file_cnt(path + '/' + proj, '.json') + SynDB.get_file_cnt(path + '/' + proj, '.patch')
            proj_name = proj
            if proj.startswith('Apache '):
                proj_name = proj[7:]
            ProjectInfo.objects.create(name=proj_name.lower(), type='JIRAISSUE', path=path + '/' + proj,
                                       files_cnt=file_cnt, size=size)

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.MboxCrawler'
        pro_list = os.listdir(path)
        for proj in pro_list:
            size = SynDB.get_dir_size(path + '/' + proj) // (1024 * 1024)
            file_cnt = SynDB.get_file_cnt(path + '/' + proj, '.mbox')
            ProjectInfo.objects.create(name=proj.lower(), type='MBOX', path=path + '/' + proj,
                                       files_cnt=file_cnt, size=size)






