from service.track import Track
from util.log import Log

class EventTrackImpl(Track):
    """
    处理event是否上报
    """
    def handleRequest(self, event, results):
        if event['event'] not in results:
            Log().error("page_id={}, module_id={}, event={}未上报".format(event['page_id'], event['module_id'], event['event']))
        else:
            return self.superior.handleRequest(event, results[event['event']])