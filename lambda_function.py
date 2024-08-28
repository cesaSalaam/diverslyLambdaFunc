import json
import openai

# Initialize the OpenAI client
openai.api_key = "your-openai-api-key"


def lambda_handler(event, context):
    # Extract the sentence from the event body
    body = json.loads(event['body'])
    sentence = body['sentence']

    # Prepare the content for the completion
    completion = openai.ChatCompletion.create(
        model="model-id",
        messages=[
            {
                "role": "system",
                "content": "You are a bias and offensive content correction agent. You help to label and correct biases in writing. You label biases based on 7 categories."
            },
            {
                "role": "user",
                "content": f"Identify and correct the biases in [TEXT]. If there is more than one bias identified in the text, label both. TEXT= " + sentence
            }
        ]
    )

    # Extract the response
    response_text = completion.choices[0].message['content']

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps({'response': response_text})
    }