from service.track import Track
from util.log import Log

class FieldTrackImpl(Track):
    """
    验证必填字段值是否上报
    """

    def handleRequest(self, event, results):
        if not len(event['fields']):
            return

        Nan = ["", 'null', 'NULL', 'Null', 'nan', 'Nan', 'NAN']

        for result in results:
            for key, value in event['fields'].items():
                if result[key] in Nan:
                    Log().error("page_id={}, module_id={}, event={}, field={}未上报".format(event['page_id'], event['module_id'], event['event'], key))
                    continue
                if value == 1:
                    continue
                if str(result[key]) not in value:
                    Log().error("page_id={}, module_id={}, event={}, field={}, value={} 字段值上报错误".format(event['page_id'], event['module_id'], event['event'], key, result[key]))