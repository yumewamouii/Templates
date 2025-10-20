import json


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat
from src.models.base_model import BaseModel


class JsonReport(BaseReport):
    def create_from_serialized(self, serialized: list[dict], original: list[BaseModel]) -> str:
        return json.dumps(serialized, indent = 4, sort_keys = True,
                          default = str, ensure_ascii = False)
    

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.JSON