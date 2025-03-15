# AWS Sentiment Analysis

A simple web-based sentiment analysis tool using **AWS Comprehend**.

## Features
- Users can input text to analyze sentiment (Positive, Negative, Neutral, Mixed).
- Uses AWS Lambda, API Gateway, and Comprehend for sentiment detection.
- Frontend built with HTML, CSS, and JavaScript.

## Setup Instructions

### 1. Deploy Backend (AWS Lambda & API Gateway)
1. Create a Lambda function in AWS.
2. Use the `boto3` library to call **AWS Comprehend**.
3. Expose the function via **API Gateway** as a REST API.
4. Enable **CORS** in API Gateway settings.

### 2. Setup Frontend
1. Create `index.html`, `style.css`, and `script.js`.
2. Use `fetch()` to send requests to API Gateway.
3. Deploy the frontend to **AWS Amplify**.


## API Endpoint
Replace `YOUR_API_URL` in `script.js` with your API Gateway URL:
```js
const response = await fetch("YOUR_API_URL", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ text })
```

## Example Usage
- **Input:** "I love this product! It's amazing."
- **Output:** `{ "sentiment": "POSITIVE" }`
