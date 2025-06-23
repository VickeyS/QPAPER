import os
import sys
import json
import requests
from PyPDF2 import PdfReader
import re
import ast

API_KEY = "AIzaSyC065w0Pxj6kH-2yiVokqSDk02oIKLzquw"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with open(pdf_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                print(f"Warning: No text extracted from page {page_num+1}", file=sys.stderr)
    return text.strip()

def generate_questions(text, one_marker, two_marker, five_marker):
    """Generates questions using Gemini API via HTTP request."""
    if not text.strip():
        print("Error: No text extracted from PDF. Check your PDF file.", file=sys.stderr)
        return []

    prompt = (
        f"Generate {one_marker} one-markers, {two_marker} two-markers, {five_marker} five-markers questions based on the following text to test my studies that can be asked in examination. "
        f"No need to provide answers. No need to add any additional information or note or any advice. "
        f"Do not add any numbering, serial numbers, or bullet points to the questions. Just output the questions as plain text, one per line. "
        f"No need to write headings for 2 markers, 3 markers, or 5 markers. "
        f"Just generate the questions in order. "
        f"**Here's the content**: {text}"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        # Extract the generated text
        gen_text = result["candidates"][0]["content"]["parts"][0]["text"]
        # Remove any leading numbering or bullet points from each question
        questions = [re.sub(r"^([0-9]+[.)\-\s]+|[•\-*]\s*)", "", q.strip()) for q in gen_text.strip().split('\n') if q.strip()]
        return questions
    except Exception as e:
        print(f"Gemini API error: {e}", file=sys.stderr)
        return []

def generate_mcqs(text, mcq_count):
    """Generates MCQs using Gemini API via HTTP request."""
    if not text.strip():
        print("Error: No text extracted from PDF. Check your PDF file.", file=sys.stderr)
        return []

    prompt = (
        f"Generate {mcq_count} multiple choice questions (MCQs) based on the following text. "
        f"For each MCQ, provide: 1. The question, 2. Four options labeled A, B, C, D, 3. The correct answer (just the letter). "
        f"Format the output as a JSON array, where each item is an object with 'question', 'options' (list), and 'answer' (A/B/C/D). "
        f"Do not add any explanations or extra text. "
        f"Here is the content: {text}"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        gen_text = result["candidates"][0]["content"]["parts"][0]["text"]
        # Extract JSON array from the output
        match = re.search(r'\[.*\]', gen_text, re.DOTALL)
        if match:
            mcqs = json.loads(match.group(0))
        else:
            mcqs = ast.literal_eval(gen_text)
        return mcqs
    except Exception as e:
        print(f"Gemini API error: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    print(json.dumps({"debug_args": sys.argv}), file=sys.stderr)
    # If MCQs are requested, allow 5 arguments: pdf_path, one_marker, two_marker, five_marker, mcq_count
    if len(sys.argv) == 6:
        pdf_path = sys.argv[1]
        one_marker = int(sys.argv[2])
        two_marker = int(sys.argv[3])
        five_marker = int(sys.argv[4])
        mcq_count = int(sys.argv[5])
        text = extract_text_from_pdf(pdf_path)
        mcqs = generate_mcqs(text, mcq_count) if mcq_count > 0 else []
        questions = generate_questions(text, one_marker, two_marker, five_marker)
        with open("debug_python_questions.txt", "w", encoding="utf-8") as dbg:
            dbg.write(json.dumps({"questions": questions, "mcqs": mcqs}, ensure_ascii=False, indent=2))
        print(json.dumps({"questions": questions, "mcqs": mcqs}))
        sys.exit(0)
    # MCQ only mode
    if len(sys.argv) == 4 and sys.argv[2] == "mcq":
        pdf_path = sys.argv[1]
        mcq_count = int(sys.argv[3])
        text = extract_text_from_pdf(pdf_path)
        mcqs = generate_mcqs(text, mcq_count)
        with open("debug_python_mcqs.txt", "w", encoding="utf-8") as dbg:
            dbg.write(json.dumps({"mcqs": mcqs}, ensure_ascii=False, indent=2))
        print(json.dumps({"mcqs": mcqs}))
        sys.exit(0)
    # Standard question mode
    if len(sys.argv) != 5:
        print(json.dumps({"error": "Usage: trial.py <pdf_path> <one_marker> <two_marker> <five_marker> [mcq_count]", "received_args": sys.argv}))
        sys.exit(1)
    pdf_path = sys.argv[1]
    one_marker = int(sys.argv[2])
    two_marker = int(sys.argv[3])
    five_marker = int(sys.argv[4])

    text = extract_text_from_pdf(pdf_path)
    questions = generate_questions(text, one_marker, two_marker, five_marker)
    with open("debug_python_questions.txt", "w", encoding="utf-8") as dbg:
        dbg.write(json.dumps({"questions": questions}, ensure_ascii=False, indent=2))
    print(json.dumps({"questions": questions}))
