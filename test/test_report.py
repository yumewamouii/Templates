import unittest
import os


from src.reports.report_format import ReportFormat
from src.reports.report_factory import ReportFactory


from src.start_service import StartService


from src.dtos.nomenclature_dto import NomenclatureDTO


from src.mappers.nomenclature_mapper import NomenclatureMapper


from src.models.nomenclature import Nomenclature


class TestReport(unittest.TestCase):
    def setUp(self):
        self.factory = ReportFactory()
        self.start_service = StartService()


        self.data = self.start_service.load_settings()
        self.start_service.start()
        
        
        self.output_dir = 'reports'
        os.makedirs(self.output_dir, exist_ok = True)
    

    def test_generate_reports_in_all_formats(self):
        repo_data = self.start_service.data()
        nomenclatures = repo_data[self.start_service._repository.range_nomenclature_key()]
        for fmt in [ReportFormat.CSV, ReportFormat.MARKDOWN, ReportFormat.JSON, ReportFormat.XML]:
            print(fmt, type(fmt))
            with self.subTest(format = fmt.name):
                report_instance = self.factory.create(fmt)
                self.assertIsNotNone(report_instance)


                report_content = report_instance.create(nomenclatures)
                file_path = os.path.join(self.output_dir, f'report.{fmt.name.lower()}')
                with open(file_path, 'w', encoding = 'utf-8') as file:
                    file.write(report_content)