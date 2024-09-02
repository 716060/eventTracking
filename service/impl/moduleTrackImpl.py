from service.track import Track
from util.log import Log
from util.match import Match

class ModuleTrackImpl(Track):
    """
    处理module_id是否上报
    """

    def handleRequest(self, event, results):
        if event['module_id'] not in results:
            for result in list(results.keys()):
                if Match().fuzzy_matching(event['module_id'], result) > 0.8:
                    Log().warning("page_id={}, module_id={}存在模糊匹配情况，请手动回归下".format(event['page_id'], event['module_id']))
                    return self.superior.handleRequest(event, results[result])
                else:
                    continue
            Log().error("page_id={}, module_id={}未上报".format(event['page_id'], event['module_id']))
        else:
            return self.superior.handleRequest(event, results[event['module_id']])