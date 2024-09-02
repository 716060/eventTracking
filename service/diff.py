from util.read import Read
from service.BuildService import BuildService
from service.impl.pageTrackImpl import PageTrackImpl
from service.impl.moduleTrackImpl import ModuleTrackImpl
from service.impl.eventTrackImpl import EventTrackImpl
from service.impl.fieldsTrackImpl import FieldTrackImpl


class Diff:
    def __init__(self, path):
        self.path = Read().readYaml(path)

    def submit(self, track, excel, csv_result):
        track.handleRequest(excel, csv_result)

    def handle(self, excel, csv_results):
        page_track = PageTrackImpl()
        module_track = ModuleTrackImpl()
        event_track = EventTrackImpl()
        field_track = FieldTrackImpl()
        page_track.set_superior(module_track)
        module_track.set_superior(event_track)
        event_track.set_superior(field_track)
        self.submit(page_track, excel, csv_results)

    def diff_testCase_event_service(self):
        csv_results = BuildService(self.path['path']['csv']).build()
        excel_results = Read().readExcel(self.path['path']['excel'])

        for excel in excel_results:
            self.handle(excel, csv_results)


