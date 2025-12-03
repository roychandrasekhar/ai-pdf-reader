# local AI assistant
This is a simple project that reads **text or PDF files** and answers your questions.  
It works completely on your local machine using Python and a virtual environment.
---

🚀 How to Run the Project

Follow the steps below:

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

---

## ❓ Example Questions You Can Ask

After the PDF/text is loaded, you can ask questions like:

- **What is the annual fee for class 2 ?**
- **Tell me total subjects in each class ?**
---

## 📝 Notes

- Store your PDF or text file inside the `data/` folder.
- Make sure you add your `GROQ_API_KEY` in a `.env` file.
- Supports **PDF** and **TXT** files.

---

## ✔ Requirements

Your `requirements.txt` must contain:

```
langchain
langchain-core
langchain-groq
python-dotenv
pypdf
```

