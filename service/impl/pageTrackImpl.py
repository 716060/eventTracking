from service.track import Track
from util.log import Log

class PageTrackImpl(Track):
    """
    处理page_id是否上报
    """
    def handleRequest(self, excel, csv_results):
        if excel['page_id'] not in csv_results:
            Log().error("page_id={}未上报".format(excel['page_id']))
        else:
            return self.superior.handleRequest(excel, csv_results[excel['page_id']])



