
from study_history import save_study_question, get_study_history

student_id = "demo_student"

print("Saving a test question...")

result = save_study_question(
    student_id,
    "What is SDLC?",
    "SDLC is the process of developing software through stages."
)

print(result)

print("\nRetrieving study history...")
print(get_study_history(student_id))
