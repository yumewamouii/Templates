from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat
from src.reports.csv_report import CsvReport
from src.reports.json_report import JsonReport
from src.reports.markdown_report import MarkdownReport
from src.reports.xml_report import XmlReport


from src.exceptions.validation import ArgumentException


class ReportFactory:
    def __init__(self):
        self._report_map = {
            ReportFormat.CSV: CsvReport,
            ReportFormat.MARKDOWN: MarkdownReport,
            ReportFormat.JSON: JsonReport,
            ReportFormat.XML: XmlReport
        }
    

    def create(self, report_format: ReportFormat) -> BaseReport:
        report = self._report_map[report_format]


        if report is None:
            raise ArgumentException('Unknown report format: {}'.format(report_format))
        

        return report()