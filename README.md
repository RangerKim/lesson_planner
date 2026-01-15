

---

````markdown
# Lesson Planner Flask App

A simple Flask app to generate structured lesson plan prompts.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/RangerKim/lesson_planner.git
cd lesson_planner
````

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the app.

## Usage

1. Fill out the form fields with your lesson information (topic, grade band, duration, etc.).
2. Click **Generate Prompt** – this creates a detailed **AI prompt** describing the lesson you want to generate.
3. Click **Download Prompt** to save it as a text file.

**Next steps with an LLM:**

1. Take the downloaded prompt and input it into your favorite LLM (like ChatGPT or another AI model) to **generate a full lesson plan**.
2. Copy the resulting lesson plan text.
3. Return to the app and paste it into the HTML conversion section (or use the second prompt in the app) to **convert the generated lesson plan into a fully formatted HTML document**.
4. The HTML will include **semantic headings, tables for procedures, color-coded instructional roles, and structured content** ready for teachers to use.

---

## Notes

* Keep `index.html` inside the `templates/` folder.
* This app runs locally; to make it available online, deploy to a service like Render, Railway, or PythonAnywhere.
* Ensure Python and Flask are installed before running the app.

```

---

This makes it **very clear for a user** that:  

1. The first prompt generates a structured lesson plan via an LLM.  
2. The second prompt (built into your app) converts that lesson plan text into **usable HTML**.  

---

