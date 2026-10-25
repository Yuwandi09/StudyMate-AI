
from search_notes import search_notes


def main():
    print("=" * 45)
    print("       STUDYMATE AI - BEFORE & AFTER")
    print("=" * 45)

    question = input("\nEnter a question about your lecture notes: ").strip()

    if not question:
        print("Please enter a question.")
        return

    print("\n--- BEFORE: Without the search tool ---")
    print("The program has no access to your lecture notes.")
    print("It cannot retrieve information from notes.txt.")

    print("\n--- AFTER: With the search tool ---")
    print("Searching lecture notes...")
    answer = search_notes(question)
    print("\nRetrieved information:")
    print(answer)


if __name__ == "__main__":
    main()
