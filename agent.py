
from strands import Agent
from strands.models.ollama import OllamaModel
from search_notes import search_notes

SYSTEM_PROMPT = """
You are StudyMate AI, a helpful university study assistant.

Explain concepts in simple English for university students.

When a question is about lecture notes, use the search_notes
tool to find relevant information before answering.

Base your answer on the information returned by the tool.
If the notes do not contain the answer, say so clearly.
Do not invent information from the lecture notes.
"""

model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen2.5:3b"
)

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[search_notes]
)

if __name__ == "__main__":
    print("StudyMate AI is ready!")
    question = input("Ask a question about your lecture notes: ")
    response = agent(question)
    print("\nStudyMate:", response)
