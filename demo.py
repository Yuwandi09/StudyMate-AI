from search_notes import search_notes


def main():
    print("=" * 40)
    print("       STUDYMATE AI - TOOL DEMO")
    print("=" * 40)
    print("Ask questions about your lecture notes.")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYour question: ").strip()

        if question.lower() == "exit":
            print("Good luck with your studies!")
            break

        if not question:
            print("Please enter a question.")
            continue

        answer = search_notes(question)

        print("\nInformation found in your notes:")
        print(answer)


if __name__ == "__main__":
    main()