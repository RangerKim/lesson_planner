from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

# Step 2 HTML conversion prompt (boilerplate)
HTML_PROMPT = """You are an expert lesson plan formatter and web designer. Take the following raw lesson plan text and convert it into a **fully styled, semantic HTML document**. Follow these rules exactly:

1. Use <h1> for the lesson title and <h2> for all major sections (Objectives, Materials, Procedure, Assessment, etc.).
2. Use <ul> for all lists such as objectives, vocabulary, materials, and assessment items.
3. Convert the lesson procedure into a <table> with columns: Time, Activity, Instructional Role, Details / Ranger Notes.
4. Apply classes for instructional roles:
   - .ido → green background (I Do)
   - .wedo → yellow background (We Do)
   - .youdo → blue background (You Do)
5. Ranger notes sections should use class .ranger-section with yellow background.
6. Include **fixed-minute timing** (e.g., 5 min, 10 min) rather than ranges, so educators can follow transitions precisely.
7. Include **example leading questions** in each lesson procedure block to guide student discussion and thinking.
8. Preserve all content exactly, including times, activities, teacher notes, and discussion prompts.
9. Keep the HTML semantic, readable, and structured; do not use inline styles except for body defaults.
10. Include CSS in a <style> block in the head for:
    - Instructional role background colors (.ido, .wedo, .youdo)
    - Ranger note backgrounds
    - Table styling
    - Any legend or color-coded boxes needed for the lesson
11. Include all sections of the lesson plan:
    - Title
    - Grade Band
    - Duration
    - Learning Setting
    - Phenomenon / Topic
    - NGSS Alignment
    - Learning Objectives
    - Key Vocabulary
    - Materials
    - Lesson Procedure (with fixed minutes, leading questions, indoor alternatives)
    - Assessment / Evaluation
    - Extensions / Adaptations
    - Educator Cheat Sheet
    - Deeper Concepts / Extension Notes
12. Ensure outdoor activities **always include an indoor alternative** in case of weather or limited access.
13. Ensure the HTML includes **clear semantic structure**, color-coded instructional roles, and ranger notes so it is ready for teachers to use directly.

"""

@app.route("/", methods=["GET", "POST"])
def index():
    prompt_text = ""
    if request.method == "POST":
        # Gather form inputs
        topic = request.form.get("topic", "Your topic here")
        grade_band = request.form.get("grade_band", "5-8")
        duration = request.form.get("duration", "60 minutes")
        setting = request.form.get("setting", "Indoor/Outdoor")
        place = request.form.get("place", "Local context")
        activity_style = request.form.get("activity_style", "Movement-Based")
        student_output = request.form.get("student_output", "Discussion & explanation")
        key_vocab = request.form.get("key_vocab", "")
        key_concept = request.form.get("key_concept", "")
        
        # Build custom AI prompt (Step 1)
        prompt_lines = [
            f"Create a detailed lesson plan for the following:",
            f"- Topic/Phenomenon: {topic}",
            f"- Grade Band: {grade_band}",
            f"- Duration: {duration}",
            f"- Learning Setting: {setting}",
            f"- Place-Based Context: {place}",
            f"- Primary Activity Style: {activity_style}",
            f"- Expected Student Output: {student_output}"
        ]
        if key_vocab:
            prompt_lines.append(f"- Include key vocabulary: {key_vocab}")
        if key_concept:
            prompt_lines.append(f"- Include key concepts: {key_concept}")

        prompt_lines.append(
            "Follow best practices for upper elementary lesson planning, NGSS alignment, and place-based education. "
            "Do NOT create the lesson plan yet; just provide an AI-ready prompt."
        )

        prompt_text = "\n".join(prompt_lines)

    return render_template("index.html", prompt_text=prompt_text, html_prompt=HTML_PROMPT)

@app.route("/download", methods=["POST"])
def download():
    prompt_content = request.form.get("prompt_text", "")
    return send_file(
        io.BytesIO(prompt_content.encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name="lesson_plan_prompt.txt"
    )

if __name__ == "__main__":
    app.run(debug=True)
