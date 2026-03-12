# Humbot Humanizer - OpenClaw Skill

Transform AI-generated text into natural, human-like writing using the Humbot API.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

### 1. Install the Skill

```bash
# If using ClawHub
clawhub install humbot-humanizer

# Or clone manually
git clone https://github.com/hopo84/humbot-humanizer-skill.git ~/.openclaw/workspace/skills/humbot-humanizer
```

### 2. Get Humbot API Credentials

Visit [Humbot.ai](https://humbot.ai) to:
1. Sign up for an account
2. Get your API key
3. Get your authorization header

### 3. Configure Environment Variables

```bash
# Add to your ~/.bashrc or ~/.zshrc
export HUMBOT_API_KEY="api_key_xxxxxxxxxxxxx"
export HUMBOT_AUTH_HEADER="Basic xxxxxxxxxxxx"

# Or create a .env file (not tracked by git)
cp .env.example .env
# Edit .env with your credentials
source .env
```

### 4. Use the Skill

Just ask your OpenClaw agent:

```
"Humanize this text: [your AI-generated text]"
"Make this sound more natural: [text]"
"Rewrite this to avoid AI detection: [text]"
```

## 📖 What It Does

This skill:
- ✅ Removes AI-typical patterns and phrases
- ✅ Adds natural variation and flow
- ✅ Makes text sound conversational and authentic
- ✅ Helps content pass AI detection tools
- ✅ Provides detection scores (0-100)

## 🎯 Model Types

- **Quick** (default) - Fast, good for most content
- **Standard** - Balanced quality and speed  
- **Advanced** - Highest quality, slower

## 🔧 Manual Usage

### Create a humanization task:

```bash
cd ~/.openclaw/workspace/skills/humbot-humanizer

# From text
python scripts/create_task.py "Your AI text here" --model-type Standard

# From file
python scripts/create_task.py --file input.txt --model-type Advanced
```

This returns a task ID.

### Retrieve results:

```bash
python scripts/retrieve_result.py <task_id> --wait
```

## 📊 Example Output

```
============================================================
HUMANIZED TEXT
============================================================
AI has been one of the most disruptive technologies in the world
over the last several years, radically changing our views...

============================================================
STATISTICS
============================================================
Original:    111 words
Humanized:   124 words
Detection:   HUMAN (score: 82/100)
Model:       Advanced
```

## 🛡️ Security

**⚠️ This skill does NOT include API credentials in the code.**

You must configure your own credentials via environment variables. Never commit your `.env` file or credentials to version control.

## 📋 Requirements

- Python 3.7+
- `requests` library
- Valid Humbot API credentials

## 📁 Project Structure

```
humbot-humanizer-skill/
├── SKILL.md              # Skill definition for OpenClaw
├── README.md             # This file
├── LICENSE               # MIT License
├── .env.example          # Example environment configuration
├── .gitignore           # Git ignore rules
├── scripts/
│   ├── create_task.py   # Submit text for humanization
│   └── retrieve_result.py # Retrieve humanized results
├── references/
│   └── (documentation)
└── evals/
    └── evals.json       # Test cases
```

## 🧪 Testing

Test the skill with sample text:

```bash
export HUMBOT_API_KEY="your_key"
export HUMBOT_AUTH_HEADER="your_header"

cd scripts
python create_task.py "This is a test of the humanization system." --model-type Quick
# Returns: task_xxxxx

python retrieve_result.py task_xxxxx --wait
```

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Issues

Found a bug? Have a feature request? Please open an issue on [GitHub](https://github.com/hopo84/humbot-humanizer-skill/issues).

## 💬 Support

- **OpenClaw Docs**: [docs.openclaw.ai](https://docs.openclaw.ai)
- **Humbot**: [humbot.ai](https://humbot.ai)
- **Discussions**: [GitHub Discussions](https://github.com/hopo84/humbot-humanizer-skill/discussions)

## 🌟 Star History

If you find this skill useful, please give it a star on GitHub!

---

Made with 🪄 for [OpenClaw](https://openclaw.ai)
