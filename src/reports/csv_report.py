import csv
import io


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat


from src.models.base_model import BaseModel


class CsvReport(BaseReport):
    def create_from_serialized(self, serialized: list[dict], original: list[BaseModel]):
        flattened_dicts = [self._flatten_dict(item) for item in serialized]
        fieldnames = flattened_dicts[0].keys()


        output = io.StringIO()


        writer = csv.DictWriter(output, fieldnames = fieldnames)
        writer.writeheader()
        for flatten_dict in flattened_dicts:
            writer.writerow(flatten_dict)
        

        return output.getvalue()
    

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.CSV