
# Banking AI Bot

This project is a Python-based AI assistant designed to answer questions related to banking information in Sri Lanka. It leverages OpenAI's GPT-3/4 models to generate responses using context extracted from various Sri Lankan banking websites. The bot can be used to answer general banking questions by utilizing a custom scraper to collect data and a language model to generate appropriate responses.

## Features

- **Context-Based Responses:** The AI bot answers banking-related questions based on context gathered from Sri Lankan bank websites.
- **Web Scraping:** A Scrapy-based scraper fetches the necessary data from the banking websites.
- **Natural Language Processing:** The assistant generates human-like responses based on the prompt provided by the user.
- **Environment Variable Configuration:** Store your OpenAI API keys and other sensitive data securely using `.env` files.

## Requirements

- Python 3.8+
- Install dependencies using `pip` from the `requirements.txt` file.
- Create an OpenAI account to get an API key and configure it in the `.env` file.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/banking-ai-bot.git
   cd banking-ai-bot
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the environment variables:**

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

6. **Run the script:**

   After setting up, you can run the `main.py` script to interact with the banking AI bot.

   ```bash
   python main.py
   ```

## File Structure

```
banking-ai-bot/
│
├── bank_scraper/                # Directory for the scraper and response generator
│   ├── main.py                  # Main script to generate responses based on the prompt
│   ├── response_generator.py    # Function that interacts with OpenAI API to generate responses
│   └── .env                     # Environment variables for OpenAI API keys
│
├── requirements.txt             # List of Python dependencies
└── README.md                    # Project documentation (this file)
```

## Dependencies

- `openai` – For interacting with OpenAI's GPT models.
- `dotenv` – To load environment variables from the `.env` file.
- `scrapy` – To scrape banking websites and gather relevant data.
- `requests` – To make HTTP requests.

## Example Usage

```python
from response_generator import generate_response

context = "The interest rates for fixed deposits at Bank X are higher for longer terms."
question = "What is the interest rate for a 6-month fixed deposit?"
prompt = f"Answer this question: {question}\nUsing only this context:\n{context}"

response = generate_response(prompt)
print(response)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

