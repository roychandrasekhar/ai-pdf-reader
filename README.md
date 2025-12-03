
# 📘 AI Document Question Answering (Groq + LangChain)

This is a simple project that reads **text or PDF files** and answers your questions.  
It works completely on your local machine using Python and a virtual environment.

---

## 🚀 How to Run the Project

Follow the steps below:

### 1️⃣ Create Virtual Environment

```bash
python3 -m venv venv
```

### 2️⃣ Activate Virtual Environment

#### Linux/macOS:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

## ❓ Example Questions You Can Ask

After the PDF/text is loaded, you can ask questions like:

- **What is the annual fee for class 2 ?**
- **Tell me total subjects in each class ?**

Feel free to modify the questions based on your document.

---

## 📝 Notes

- Store your PDF or text file inside the `data/` folder.
- Make sure you add your `GROQ_API_KEY` in a `.env` file.
- Supports **PDF** and **TXT** files automatically.

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

---

Enjoy building your local AI assistant! ✨
