# 🔗 Link Simplifier

A smart web application that uses AI to summarize articles and web content in seconds. Simply paste a URL and get an intelligent summary with key points, reading time estimates, and a verdict on whether it's worth reading.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **AI-Powered Summaries**: Uses OpenAI's GPT-4o-mini to generate intelligent summaries
- **Quick Mode**: Get a rapid 3-point summary with a verdict in seconds
- **Full Analysis Mode**: Comprehensive breakdown including:
  - 2-3 sentence summary
  - 5 key points
  - Estimated reading time
  - Target audience level (Beginner/Intermediate/Advanced)
  - Read/Skip/Optional verdict with reasoning
  - Key takeaway
- **Clean UI**: Modern, responsive interface with smooth animations
- **Copy to Clipboard**: Easily copy summaries for later reference
- **Smart Content Extraction**: Removes navigation, scripts, and styling to focus on actual content

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Shivang1109/Link-Simplifier.git
cd Link-Simplifier
```

2. Install dependencies:
```bash
cd link-simplifier
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-api-key-here
```

### Running the Application

1. Start the FastAPI server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:8000
```

3. Paste any article URL and click "Simplify"!

## 📖 Usage

### Basic Usage

1. Enter a URL in the input field (must start with `http://` or `https://`)
2. Choose your mode:
   - **Quick Mode** (⚡): Fast 3-point summary
   - **Full Mode**: Comprehensive analysis
3. Click "Simplify" or press Enter
4. View your AI-generated summary
5. Click "Copy" to save the summary to your clipboard

### API Endpoint

You can also use the API directly:

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article", "quick": false}'
```

**Request Body:**
```json
{
  "url": "https://example.com/article",
  "quick": false
}
```

**Response:**
```json
{
  "result": "Summary:\n...\n\nKey Points:\n...",
  "quick": false
}
```

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI**: OpenAI GPT-4o-mini
- **Web Scraping**: BeautifulSoup4, Requests
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Server**: Uvicorn

## 📁 Project Structure

```
Link-Simplifier/
├── link-simplifier/
│   ├── main.py              # FastAPI backend
│   ├── index.html           # Frontend UI
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment template
│   └── .env                 # Your API keys (not in git)
└── README.md
```

## ⚙️ Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Customization

You can modify the prompts in `main.py`:
- `QUICK_PROMPT`: Controls quick mode output format
- `FULL_PROMPT`: Controls full analysis output format

Adjust token limits and temperature in the OpenAI API call:
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5,  # Adjust for creativity (0-1)
    max_tokens=900,   # Adjust for response length
)
```

## 🔒 Security Notes

- Never commit your `.env` file with real API keys
- The `.env` file is already in `.gitignore`
- Keep your OpenAI API key secure
- Consider adding rate limiting for production use

## 🐛 Troubleshooting

**"Could not reach the backend"**
- Make sure the server is running on port 8000
- Check if another application is using port 8000

**"Failed to fetch URL"**
- Verify the URL is accessible
- Some websites block automated requests
- Check your internet connection

**"OpenAI error"**
- Verify your API key is correct in `.env`
- Check your OpenAI account has credits
- Ensure you have access to GPT-4o-mini model

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 👤 Author

**Shivang Pathak**
- GitHub: [@Shivang1109](https://github.com/Shivang1109)

## 🙏 Acknowledgments

- OpenAI for the GPT-4o-mini API
- FastAPI for the excellent web framework
- BeautifulSoup for web scraping capabilities

---

Made with ❤️ by Shivang Pathak
