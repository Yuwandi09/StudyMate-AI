
from strands import Agent
from strands.models.ollama import OllamaModel

from search_notes import search_notes
from study_history import save_study_question, get_study_history


SYSTEM_PROMPT = """
You are StudyMate AI, a helpful university study assistant.

Explain concepts in simple English for university students.

When a question is about lecture notes, use the search_notes
tool before answering.

Base answers about lecture notes on the information returned
by the tool. If the notes do not contain the answer, say so clearly.
Do not invent information from lecture notes.

You can also manage study history.

When the student asks to save or remember a study question,
use save_study_question to save the question and answer.

When the student asks to review or show previous questions,
use get_study_history to retrieve their study history.

Use this student ID for this demo: demo_student.

When saving a question, include the student's question and
the answer you provided. Confirm whether saving succeeded.
Do not claim something was saved unless the tool confirms it.
"""


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen2.5:3b"
)


agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[
        search_notes,
        save_study_question,
        get_study_history
    ]
)


if __name__ == "__main__":
    print("StudyMate AI is ready!")
    print("You can ask questions, save study history, or review it.")
    
    while True:
        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not question:
            continue

        response = agent(question)
        print("\nStudyMate:", response)
