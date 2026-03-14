# Humbot Humanizer Skill

Transform AI-generated text into natural, human-like writing using the Humbot API.

## 🚀 Quick Start

### 1. Get Your API Key

Before using this skill, you need a Humbot API key:

1. Visit **https://humbot.ai/ai-humanizer-api**
2. Register for an account
3. Navigate to the API section in your dashboard
4. Copy your API key

### 2. Configure the API Key

Set the API key as an environment variable:

```bash
# Permanent (recommended)
echo 'export HUMBOT_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# Or temporary (current session only)
export HUMBOT_API_KEY="your_api_key_here"
```

**Important:** Replace `your_api_key_here` with your actual API key from Humbot.

### 3. Test the Setup

Verify everything works:

```bash
cd ~/.openclaw/workspace/skills/humbot-humanizer
python scripts/create_task.py "This is a test sentence to humanize."
```

If successful, you'll get a task ID. You can then retrieve the result:

```bash
python scripts/retrieve_result.py <task_id> --wait
```

## 📖 Usage

### Basic Usage

**Humanize text directly:**
```bash
python scripts/create_task.py "Your AI-generated text here"
```

**Humanize from a file:**
```bash
python scripts/create_task.py --file input.txt
```

**Choose quality mode:**
```bash
python scripts/create_task.py "Text here" --model-type Advanced
```

Model types:
- `Quick` - Fast processing (default)
- `Standard` - Balanced quality and speed
- `Advanced` - Highest quality, slower

### Retrieve Results

**Get result by task ID:**
```bash
python scripts/retrieve_result.py <task_id>
```

**Auto-wait for completion:**
```bash
python scripts/retrieve_result.py <task_id> --wait
```

**JSON output:**
```bash
python scripts/retrieve_result.py <task_id> --json
```

## 🤖 AI Assistant Usage

When using this skill through the OpenClaw AI assistant, simply say:

- "Humanize this text: [paste text]"
- "Make this sound more natural: [text]"
- "Rewrite this to pass AI detection: [text]"
- "Use Humbot to humanize [file/text]"

The AI will:
1. Check if your API key is configured
2. If not, guide you through the setup process
3. Submit your text to Humbot
4. Wait for results and show you the humanized output with statistics

## 🔧 Troubleshooting

### "HUMBOT_API_KEY not set" error

**Solution:** Follow the setup steps above to configure your API key.

### API returns authentication error

**Possible causes:**
- Invalid API key
- Expired API key
- Account not activated

**Solution:** Log into https://humbot.ai and verify your API key is active.

### Task takes too long

**Normal behavior:** 
- Quick mode: 5-15 seconds
- Standard mode: 15-30 seconds  
- Advanced mode: 30-60 seconds

For very long texts, processing may take longer. The scripts will automatically wait and poll for results.

### Network timeout

**Solution:** Check your internet connection and try again. The API endpoints are:
- Create: `https://humbot.ai/api/humbot/v1/create`
- Retrieve: `https://humbot.ai/api/humbot/v1/retrieve`

## 🔒 Security

- **Never share your API key** in conversations, logs, or public channels
- Store it as an environment variable, not in code
- The skill scripts automatically read from `HUMBOT_API_KEY` environment variable
- Revoke and regenerate your key if you suspect it's been compromised

## 📊 What You Get

The humanized output includes:

- **Humanized text** - The rewritten, natural-sounding version
- **Word count** - Original vs humanized word counts
- **Detection score** - AI detection likelihood (0-100, higher = more human-like)
- **Detection result** - Pass/Fail for AI detection
- **Model used** - Which quality tier was used

## 💡 Tips for Best Results

1. **Longer is better** - 100+ words produce better results than short snippets
2. **Clean input** - Remove code blocks, special formatting before submitting
3. **Start with Quick** - Test with Quick mode first, upgrade to Advanced for important content
4. **Review output** - Always review the humanized text; it may need minor tweaks
5. **Try again** - If not satisfied, try a different model tier

## 🆘 Support

- **Humbot API docs:** https://humbot.ai/ai-humanizer-api
- **OpenClaw docs:** https://docs.openclaw.ai
- **Skill issues:** Report in the OpenClaw Discord or GitHub

## 📝 License

This skill is provided as-is for use with OpenClaw. The Humbot API is a commercial service - check their pricing and terms at https://humbot.ai
