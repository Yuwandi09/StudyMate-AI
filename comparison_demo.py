
from search_notes import search_notes


def main():
    question = input("Ask a study question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    print("\n--- BEFORE: Without the S3 search tool ---")
    print("StudyMate cannot retrieve your lecture notes.")
    print("No lecture information was retrieved.")

    print("\n--- AFTER: With the S3 search tool ---")
    print("StudyMate is searching Amazon S3...")

    answer = search_notes(question)

    print("\nInformation retrieved from your notes:")
    print(answer)


if __name__ == "__main__":
    main()
