
import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = []
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input":
            self.inputs.append(attrs)

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True

        if tag == "input" and attrs.get("type") == "submit":
            self.submit_found = True


class TestHTMLForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        html_path = Path(__file__).parent.parent / "index.html"
        html = html_path.read_text(encoding="utf-8")

        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_name_field(self):
        self.assertTrue(any(
            item.get("type") == "text"
            for item in self.parser.inputs
        ))

    def test_email_field(self):
        self.assertTrue(any(
            item.get("type") == "email"
            for item in self.parser.inputs
        ))

    def test_contact_number_field(self):
        self.assertTrue(any(
            item.get("type") == "tel"
            for item in self.parser.inputs
        ))

    def test_required_fields(self):
        for field_type in ["text", "email", "tel"]:
            field = next(
                (item for item in self.parser.inputs
                 if item.get("type") == field_type),
                None
            )
            self.assertIsNotNone(field)
            self.assertIn("required", field)

    def test_submit_button(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main()
