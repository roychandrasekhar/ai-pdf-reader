import os
import textwrap
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from pypdf import PdfReader

load_dotenv()
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        if self.file_path.lower().endswith(".pdf"):
            return self._read_pdf()
        else:
            return self._read_text()

    def _read_text(self):
        with open(self.file_path, "r") as f:
            return f.read()

    def _read_pdf(self):
        reader = PdfReader(self.file_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text

class GroqAssistant:
    def __init__(self):
        self.model = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL_NAME"),
            temperature=0
        )

    def ask(self, file_content, question):
        prompt = textwrap.dedent(f"""
            You are an assistant that reads documents.
            Here is the extracted document content:
            {file_content}
            User question: {question}
        """)

        response = self.model.invoke([HumanMessage(content=prompt)])
        return response.content

class App:
    def __init__(self, file_path):
        self.reader = FileReader(file_path)
        self.assistant = GroqAssistant()

    def run(self):
        content = self.reader.read()
        question = input("\nAsk question related to this document: ")
        answer = self.assistant.ask(content, question)
        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    app = App("data/FEES-STURCTURE.pdf")
    app.run()
