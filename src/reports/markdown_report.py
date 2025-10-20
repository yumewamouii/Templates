from src.models.base_model import BaseModel


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat


class MarkdownReport(BaseReport):
    def create_from_serialized(self, serialized: list[dict], original: list[BaseModel]) -> str:
        markdown_lines = []
        flatten_dicts = [self._flatten_dict(item) for item in serialized]
        class_name = original[0].__class__.__name__


        for i, flatten_dict in enumerate(flatten_dicts, start = 1):
            markdown_lines.append(f'### {class_name} {i}')
            for key, value in flatten_dict.items():
                markdown_lines.append(f'**{key}**: {value}')
            markdown_lines.append('\n---\n')
        

        return '\n'.join(markdown_lines)
    

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.MARKDOWN