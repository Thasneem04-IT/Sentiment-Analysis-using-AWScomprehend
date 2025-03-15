import json
import boto3

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')

    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  
                'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            },
            'body': json.dumps({'message': 'CORS preflight response'})
        }

    if 'body' not in event or event['body'] is None:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Request body is missing'})
        }

    body = json.loads(event['body'])
    text = body.get('text', '').strip()
    
    if not text:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Text input is required'})
        }

    # Call Amazon Comprehend
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Allow requests from any domain
            'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        },
        'body': json.dumps(response)
    }





# Test with:

# {
#   "httpMethod": "POST",
#   "body": "{\"text\": \"I don't like this product! It is not good.\"}"
# }