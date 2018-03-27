import os
from .models import ProjectInfo


class SynDB:

    @staticmethod
    def get_meta_info(path, source):
        size = 0
        count = 0
        preview_file = ''
        ret_list = []

        if source == 'BUGZILLA':
            for root, dirs, files, in os.walk(path):
                for file in files:
                    if file.find('.xml') >= 0:
                        size += os.path.getsize(os.path.join(root, file))
                        count += 1
                for file in files:
                    if file.find('.xml') >= 0:
                        preview_file = os.path.join(root, file)
                        break
        elif source == 'GIT':
            for root, dirs, files, in os.walk(path):
                for file in files:
                    if (file.find('commit') >= 0 and file.find('txt') < 0):
                        size += os.path.getsize(os.path.join(root, file))
                        count += 1
                for file in files:
                    if (file.find('commit') >= 0 and file.find('txt') < 0):
                        preview_file = os.path.join(root, file)
                        break
        elif source == 'CODE':
            for root, dirs, files, in os.walk(path):
                for file in files:
                    size += os.path.getsize(os.path.join(root, file))
                    count += 1
        elif source == 'JIRAISSUE':
            for root, dirs, files, in os.walk(path):
                for file in files:
                    if file.find('.json') >= 0:
                        size += os.path.getsize(os.path.join(root, file))
                        count += 1
                for file in files:
                    if file.find('.json') >= 0:
                        preview_file = os.path.join(root, file)
                        break
        elif source == 'MAILBOX':
            for root, dirs, files, in os.walk(path):
                for file in files:
                    if file.find('.mbox') >= 0:
                        size += os.path.getsize(os.path.join(root, file))
                        count += 1
                for file in files:
                    if file.find('.mbox') >= 0:
                        preview_file = os.path.join(root, file)
                        break

        size = size // (1024*1024) + 1
        ret_list.append(size)
        ret_list.append(count)
        ret_list.append(preview_file)
        return ret_list




    @staticmethod
    def syn_db():
        ProjectInfo.objects.all().delete()

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.BugzillaCrawler'
        source = 'BUGZILLA'
        project_list = os.listdir(path)
        for project in project_list:
            project_path = path + '/' + project
            meta_list = SynDB.get_meta_info(project_path, source)
            ProjectInfo.objects.create(name=project.lower(), source=source, path=project_path,
                                       files_cnt=meta_list[1], size=meta_list[0], preview_path=meta_list[2])

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.GitCrawler'
        project_list = os.listdir(path)
        for project in project_list:
            dir = os.listdir(path + '/' + project)
            project_name = dir[0]
            project_path = path + '/' + project + '/' + project_name
            source = 'GIT'
            meta_list = SynDB.get_meta_info(project_path, source)
            ProjectInfo.objects.create(name=project_name.lower(), source=source, path=project_path,
                                       files_cnt=meta_list[1], size=meta_list[0], preview_path=meta_list[2])

            source = 'CODE'
            project_path = project_path + '/' + project_name + 'GIT'
            meta_list = SynDB.get_meta_info(project_path, source)
            ProjectInfo.objects.create(name=project_name.lower(), source=source, path=project_path,
                                       files_cnt=meta_list[1], size=meta_list[0])

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.JiraIssueCrawler'
        project_list = os.listdir(path)
        source = 'JIRAISSUE'
        for project in project_list:
            project_name = project
            if project.startswith('Apache '):
                project_name = project[7:]
            project_path = path + '/' + project
            meta_list = SynDB.get_meta_info(project_path, source)
            ProjectInfo.objects.create(name=project_name.lower(), source=source, path=project_path,
                                       files_cnt=meta_list[1], size=meta_list[0], preview_path=meta_list[2])

        path = 'E:/Apache/cn.edu.pku.EOSCN.crawler.MboxCrawler'
        project_list = os.listdir(path)
        source = 'MAILBOX'
        for project in project_list:
            project_path = path + '/' + project
            meta_list = SynDB.get_meta_info(project_path, source)
            ProjectInfo.objects.create(name=project.lower(), source=source, path=project_path,
                                       files_cnt=meta_list[1], size=meta_list[0], preview_path=meta_list[2])






