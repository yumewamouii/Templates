from enum import Enum


from src.models.company import Company
from src.models.base_model import BaseModel


from src.utils.fields import ValidatedField


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat
from src.reports.csv_report import CsvReport
from src.reports.json_report import JsonReport
from src.reports.markdown_report import MarkdownReport
from src.reports.xml_report import XmlReport


from src.exceptions.validation import OperationException, ArgumentException



class Settings(BaseModel):
    _company: Company = Company()
    _default_report_format: ReportFormat = None
    _report_map: dict[ReportFormat, type] = {
        ReportFormat.CSV: CsvReport,
        ReportFormat.JSON: JsonReport,
        ReportFormat.XML: XmlReport,
        ReportFormat.MARKDOWN: MarkdownReport
    }


    def __init__(self, default_report_format: ReportFormat = ReportFormat.JSON):
        self.company = Company()
        self._default_report_format = default_report_format
    

    @property
    def default_report_format(self) -> ReportFormat:
        return self._default_report_format

    @default_report_format.setter
    def default_report_format(self, value: ReportFormat):
        if not isinstance(value, ReportFormat):
            raise InvalidTypeException(ReportFormat, type(value))
        self._default_report_format = value

    @property
    def report_map(self) -> dict:
        return self._report_map

    @report_map.setter
    def report_map(self, value: dict):
        if not isinstance(value, dict):
            raise InvalidTypeException(dict, type(value))
        for v in value.values():
            if not issubclass(v, BaseReport):
                raise OperationException(BaseReport, type(v))
        self._report_map = value


    def __str__(self):
        return f"Settings of company:\n{self.company}"


    def __repr__(self):
        return f"<Settings of company={repr(self.company)}>"