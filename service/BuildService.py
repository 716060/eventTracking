from util.read import Read

class BuildService:

    def __init__(self, path):
        self.path = path

    def dict_initial(self, event):
        event_dict = {}
        module_dict = {}
        event_dict.setdefault(event["event"], [event])
        module_dict.setdefault(event["module_id"], event_dict)
        return module_dict

    def build(self):
        eventTrackingResult = Read().readCsv(self.path)
        tree_result = {}
        for event in eventTrackingResult:
            if not tree_result or event["page_id"] not in tree_result:
                tree_result.setdefault(event["page_id"], self.dict_initial(event))
            elif event["module_id"] not in tree_result[event["page_id"]]:
                tree_result[event["page_id"]].update(self.dict_initial(event))
            elif event["event"] not in tree_result[event["page_id"]][event["module_id"]]:
                tree_result[event["page_id"]][event["module_id"]].setdefault(event["event"], [event])
            else:
                tree_result[event["page_id"]][event["module_id"]][event["event"]].append(event)

        return tree_result

if __name__ == '__main__':
    print(BuildService(path='../file/EventTracking.csv').build())

