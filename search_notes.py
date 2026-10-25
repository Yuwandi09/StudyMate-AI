
import re
import boto3
from botocore.exceptions import ClientError
from strands import tool

BUCKET_NAME = "studymate-lecture-notes"
FILE_NAME = "notes.txt"
AWS_REGION = "ap-southeast-1"


@tool
def search_notes(query: str) -> str:
    """Search lecture notes stored in Amazon S3 and return relevant lines."""

    try:
        s3 = boto3.client("s3", region_name=AWS_REGION)

        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=FILE_NAME
        )

        notes = response["Body"].read().decode("utf-8")

    except ClientError as error:
        print("AWS S3 error:", error.response["Error"]["Code"])
        return "I could not access the lecture notes in S3. Please check AWS access and the file."

    stop_words = {
        "what", "is", "the", "a", "an", "in", "of", "to",
        "for", "and", "does", "how", "are", "was", "were",
        "it", "this", "that", "with", "on", "about",
        "my", "according", "lecture", "notes"
    }

    keywords = [
        word.lower()
        for word in re.findall(r"\b\w+\b", query)
        if len(word) > 2 and word.lower() not in stop_words
    ]

    if not keywords:
        return "Please enter a more specific question."

    scored_lines = []

    for line in notes.splitlines():
        line = line.strip()

        if not line:
            continue

        line_words = set(re.findall(r"\b\w+\b", line.lower()))
        score = sum(1 for word in keywords if word in line_words)

        if score > 0:
            scored_lines.append((score, line))

    if not scored_lines:
        return "No matching information was found in the lecture notes."

    scored_lines.sort(key=lambda item: item[0], reverse=True)
    highest_score = scored_lines[0][0]

    results = [
        line for score, line in scored_lines
        if score == highest_score
    ]

    return "\n".join(results)
