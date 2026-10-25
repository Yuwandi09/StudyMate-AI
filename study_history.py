
import boto3
from botocore.exceptions import ClientError
from strands import tool

TABLE_NAME = "StudyMateHistory"
AWS_REGION = "ap-southeast-1"


@tool
def save_study_question(student_id: str, question: str, answer: str) -> str:
    """Save a study question and answer for later review."""

    try:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name=AWS_REGION
        )
        table = dynamodb.Table(TABLE_NAME)

        response = table.update_item(
            Key={"student_id": student_id},
            UpdateExpression=(
                "SET history = list_append("
                "if_not_exists(history, :empty), :entry)"
            ),
            ExpressionAttributeValues={
                ":empty": [],
                ":entry": [{
                    "question": question,
                    "answer": answer
                }]
            }
        )

        return "Study question and answer saved successfully."

    except ClientError as error:
        return (
            "Could not save study history: "
            + error.response["Error"]["Code"]
        )


@tool
def get_study_history(student_id: str) -> str:
    """Retrieve previously saved study questions and answers."""

    try:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name=AWS_REGION
        )
        table = dynamodb.Table(TABLE_NAME)

        response = table.get_item(
            Key={"student_id": student_id}
        )

        item = response.get("Item")

        if not item or not item.get("history"):
            return "No study history found for this student."

        result = []

        for number, entry in enumerate(item["history"], start=1):
            result.append(
                f"{number}. Question: {entry['question']}\n"
                f"Answer: {entry['answer']}"
            )

        return "\n\n".join(result)

    except ClientError as error:
        return (
            "Could not retrieve study history: "
            + error.response["Error"]["Code"]
        )
