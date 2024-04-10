from langchain_together import Together
from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
from os import environ
import pandas as pd
import random
import ast

load_dotenv()
together_api_key ="5d0252b0d81297e52de455304330a01d2f935d1e273e9a12a8d2c7dd2c72080e"


# Define schema for plate number extraction
plate_number_schema = Object(
    id="platenumber",
    description="Plate number information extraction",
    attributes=[
        Text(
            id="plate_number",
            description="The plate number of the vehicle.",
            examples=[
                
                 (
                    "Find the time between 12AM and 3PM when a blue truck with the plate number MH09X4587 entered the parking area.",
                    ["MH09X4587"],
                ),
                (
                    "Retrieve the duration between 5PM and 7PM during which a red motorcycle without a plate was present in the parking lot.",
                    [""],
                ),
                (
                    "Find the time between 12AM and 3PM when a blue SUV and a red motorcycle, both without plates, entered the parking area.",
                    ["", ""],
                ),
                (
                    "Retrieve the duration between 5PM and 7PM during which a silver van with the plate TN27G7896 and a black sedan without a plate were present in the parking lot.",
                    ["TN27G7896", ""],
                ),
                (
                    "Find the time when a blue SUV and a red motorcycle, both without plates, entered the parking area.",
                    ["", ""],
                ),
                (
                    "Provide me with timestamps for a green truck with the plate AP14Y6210 and a white motorcycle with plate WB05Z1234 entering and exiting the parking premises.",
                    ["AP14Y6210", "WB05Z1234"],
                ),
                (
                    "Identify the time range for a green sedan with no visible plate and a purple SUV with plate KA08P5678 being present in the parking zone.",
                    ["", "KA08P5678"],
                ),
                (
                    "Retrieve the time range for a white pickup truck without a plate and a black convertible car with plate GJ12Q7890 entering and leaving the parking area.",
                    ["", "GJ12Q7890"],
                ),
                (
                    "Find the moments when a blue pickup truck without a visible plate and a silver hatchback with tinted windows were present in the parking zone.",
                    ["", ""],
                ),
                (
                    "Identify the time range for a brown SUV without a plate and a yellow convertible car with a convertible top down being present in the parking zone.",
                    ["", ""],
                ),
                (
                    "Find the time between 12PM and 3PM when a blue SUV with plate ABC123 and a red motorcycle without a plate entered the parking area.",
                    ["ABC123", ""],
                ),
                (
                    "Find the time between 1PM and 3PM when a blue SUV with plate ABC123, a red motorcycle without a plate, and a silver sedan with plate XYZ789 were present in the parking area.",
                    ["ABC123", "", "XYZ789"],
                ),
                (
                    "When did a black convertible car without a plate, a green pickup truck with plate MNO456, and a yellow sedan with plate STU789 access the parking facility between 5PM and 7PM?",
                    ["", "MNO456", "STU789"],
                ),
                (
                    "Provide timestamps between 10PM and 12AM for when a blue SUV without a plate, a white motorcycle with plate TUV456, and a black pickup truck without a plate were present in the parking space.",
                    ["", "TUV456", ""],
                ),
                (
                    "Find the moments when a blue hatchback with plate PQR567, a yellow minivan without a plate, and a green convertible car with plate STU789 were present in the parking zone between 4AM and 6AM.",
                    ["PQR567", "", "STU789"],
                ),
                (
                    "Tell me between 6AM and 8AM when a green sedan without a plate, a red SUV with plate XYZ789, and a brown convertible car without a plate were present in the parking premises.",
                    ["", "XYZ789", ""],
                ),
                (
                    "Find the time between 9AM and 11AM when a blue sedan with plate ABC123, a red convertible car without a plate, a white pickup truck with plate DEF456, and a black SUV without a plate were present in the parking area.",
                    [
                        "ABC123",
                        "",
                        "DEF456",
                        "",
                    ],
                ),
            ],
        ),
    ],
)

# Define schema for characteristics extraction
characteristics_schema = Object(
    id="characteristic",
    description="Characteristics of the vehicle",
    attributes=[
        Text(
            id="characteristics",
            description="The characteristics of the vehicle.",
            examples=[
(
                    "Find the time between 12AM and 3PM when a blue truck with the plate number MH09X4587 entered the parking area.",
                    ["blue truck"],
                ),
                (
                    "Retrieve the duration between 5PM and 7PM during which a red motorcycle without a plate was present in the parking lot.",
                    ["red motorcycle"],
                ),
                (
                    "Find the time between 12AM and 3PM when a blue SUV and a red motorcycle, both without plates, entered the parking area.",
                    ["blue SUV", "red motorcycle"],
                ),
                (
                    "Retrieve the duration between 5PM and 7PM during which a silver van with the plate TN27G7896 and a black sedan without a plate were present in the parking lot.",
                    ["silver van", "black sedan"],
                ),   
                
                (
                "Characteristics: [['blue truck', 'MH09X4587']]",
                ["blue truck"]
                ),         
            ],
        ),
    ],
)

# Define schema for time interval extraction
time_interval_schema = Object(
    id="timeinterval",
    description="Time interval information",
    attributes=[
        Text(
            id="time_interval",
            description="The time interval when the event occurred.",
            examples=[
                (
                    "Find the time between 12AM and 3PM when a blue SUV and a red motorcycle, both without plates, entered the parking area.",
                    ["12AM","3PM"],
                    # ["{'from': '12PM', 'to': '3PM'} "],
                ),
                (
                    "Retrieve the duration between 9AM and 11AM during which a white van with plate ABC123 was parked in the lot.",
                    ["9AM","11AM"]
                    # ["{'from': '9AM', 'to': '11AM'} "]
                    ,
                ),
                (
                    "Identify the time range for a black sedan without a visible plate and a red convertible car with plate XYZ789 being present in the parking zone from 2PM to 5PM.",
                    ["2PM","5PM"]
                    # ["{'from': '2PM', 'to': '5PM'} "]
                    ,
                ),
                (
                    "Provide timestamps for when a gray minivan with plate MP07U8765 and a blue SUV without a visible plate entered and left the parking area between 4PM and 7PM.",
                    ["4PM","7PM"]
                    #  ["{'from': '4PM', 'to': '7PM'} "]
                    ,
                ),
                (
                    "Find the moments when a blue hatchback with plate PQR567, a yellow minivan without a plate, and a green convertible car with plate STU789 were present in the parking zone between 10AM and 12PM.",
                    ["10AM","12PM"]
                    # ["{'from': '10AM', 'to': '12PM'} "]
                    ,
                ),
                (
                    "Tell me between 6AM and 8AM when a green sedan without a plate, a red SUV with plate XYZ789, and a brown convertible car without a plate were present in the parking premises.",
                    ["6AM","8AM"]
                    # ["{'from': '6M', 'to': '8AM'} "]
                    ,
                ),
                (
                    "Provide timestamps for when a gray minivan with plate MP07U8765 and a blue SUV without a visible plate entered and left the parking area",
                    ["",""],
                    # ["{'from': '', 'to': ''} "],
                    ),
            ],
        ),
    ],
)

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    together_api_key=together_api_key,
)

def extract_plate_number_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, plate_number_schema, encoder_or_encoder_class="json")
    response = chain.invoke(prompt)
    plate_numbers = response.get("text", {}).get("data", {}).get("platenumber", [])
    if plate_numbers:
        plate_number = plate_numbers.get("plate_number", "")
        print("Plate Number:", plate_number)
        return plate_number
    else:
        print("Plate number not found in the response.")
        return None

def extract_plate_number_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, plate_number_schema, encoder_or_encoder_class="json")
    data = chain.invoke((prompt))["text"]["data"]["platenumber"]["plate_number"]
    print(data)
    return data


def extract_Characteristics_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, characteristics_schema, encoder_or_encoder_class="json")
    response = chain.invoke(prompt)
    characteristics = response.get("text", {}).get("data", {}).get("characteristic", [])
    if characteristics:
        characteristics_data = characteristics.get("characteristics", [])
        if characteristics_data:
            first_characteristic = characteristics_data
            print("Characteristics:", first_characteristic)
            return first_characteristic
        else:
            print("No characteristics found in the response.")
            return None
    else:
        print("Characteristics not found in the response.")
        return None


def extract_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, characteristics_schema, encoder_or_encoder_class="json")
    data = chain.invoke((prompt))["text"]["data"]["characteristic"]["characteristics"]
    print(data)
    return data


def extract_time_interval_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, time_interval_schema, encoder_or_encoder_class="json")
    response = chain.invoke(prompt)
    time_intervals = response.get("text", {}).get("data", {}).get("timeinterval", [])
    if time_intervals:
        time_interval = str(time_intervals.get("time_interval", ""))
        tokens = time_interval.split()  # Split the string into tokens
        # Extracting start_time and end_time
        start_time = tokens[1].replace("'", "").replace(",", "").replace("{", "")  # Remove unnecessary characters
        end_time = tokens[3]  # Remove unnecessary characters
        end_time= end_time.replace("'", "").replace(",", "").replace("}", "").replace("]", "")
        timestamps="[{'from': '"+start_time+"', 'to': '"+end_time+"'}]"
        print(timestamps)
        return start_time, end_time
    else:
        print("Time interval not found in the response.")
        return None

def extract_time_interval_prompt_data(prompt: str):
    chain = create_extraction_chain(llm, time_interval_schema, encoder_or_encoder_class="json")
    data = chain.invoke(prompt)["text"]["data"]["timeinterval"]["time_interval"]
    # Check if data is a list
    if isinstance(data, list) and len(data) == 2:
        start_time, end_time = data
        timestamps="[{'from': '"+start_time+"', 'to': '"+end_time+"'}]"
        print("Time-Stamps:"+timestamps)
        return timestamps
    else:
        print("Invalid interval format. Expected a list with two elements.")
        return None


# prompt1="Find the time between 12PM and 3PM when a blue SUV with plate ABC123 and a red motorcycle without a plate entered the parking area."
# prompt2="Provide timestamps for when a gray minivan with plate MP07U8765 and a blue SUV without a visible plate entered and left the parking area"
# prompt3 ="Find the time between 1PM and 3PM when a blue SUV with plate ABC123, a red motorcycle without a plate, and a silver sedan with plate XYZ789 were present in the parking area"
# prompt4="Find the time between 12AM and 3PM when a blue truck with the plate number MH09X4587 entered the parking area"


df = pd.read_csv("dataset.csv")
random_row = df.sample(n=1)
random_question = random_row["question"].values[0]
# print("-----------1-------------")
print(random_question)
extract_plate_number_prompt_data(random_question)
extract_prompt_data(random_question)
extract_Characteristics_prompt_data(random_question)
extract_time_interval_prompt_data(random_question)
