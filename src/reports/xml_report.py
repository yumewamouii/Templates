from xml.etree.ElementTree import Element, tostring, SubElement


from src.models.base_model import BaseModel


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat


class XmlReport(BaseReport):
    def create_from_serialized(self, serialized: list[dict], original: list[BaseModel]) -> str:
        root = Element('root')


        class_name = original[0].__class__.__name__


        for i, item in enumerate(serialized, start = 1):
            object_element = SubElement(root, f'{class_name}_{i}')
            self._dict_to_xml(item, object_element)
        

        return tostring(root, encoding = 'unicode', xml_declaration = True)
    

    def _dict_to_xml(self, data: dict, parent: Element):
        for key, value in data.items():
            child = SubElement(parent, key)
            if isinstance(value, dict):
                self._dict_to_xml(value, child)
            else:
                child.text = str(value)
    

    @property
    def format(self) -> ReportFormat:
        return ReportFormat.XML