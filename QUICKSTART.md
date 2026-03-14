# 🚀 Quick Start Guide

Get started with Humbot Humanizer in 3 easy steps!

## Step 1: Get Your API Key (2 minutes)

1. Open your browser: **https://humbot.ai/ai-humanizer-api**
2. Click "Sign Up" or "Log In"
3. Go to your dashboard and copy your API key

## Step 2: Configure the Key (30 seconds)

Open your terminal and run:

```bash
echo 'export HUMBOT_API_KEY="paste_your_key_here"' >> ~/.bashrc
source ~/.bashrc
```

> 💡 **Tip:** Replace `paste_your_key_here` with your actual API key from Step 1

## Step 3: Test It! (30 seconds)

Try humanizing your first text:

```bash
cd ~/.openclaw/workspace/skills/humbot-humanizer
python scripts/create_task.py "AI-generated text often sounds robotic and unnatural." --model-type Quick
```

You'll get a task ID. Then run:

```bash
python scripts/retrieve_result.py <task_id> --wait
```

That's it! 🎉

## Usage with OpenClaw AI

Just talk to the AI naturally:

- "Humanize this: [paste your text]"
- "Make this sound more human: [text]"
- "Rewrite to avoid AI detection: [text]"

The AI will handle the rest!

## Common Commands

**Humanize text:**
```bash
python scripts/create_task.py "Your text here"
```

**Humanize a file:**
```bash
python scripts/create_task.py --file document.txt
```

**Use high quality mode:**
```bash
python scripts/create_task.py "Text" --model-type Advanced
```

**Get results:**
```bash
python scripts/retrieve_result.py <task_id> --wait
```

## Need Help?

- Check if your key is set: `echo $HUMBOT_API_KEY`
- Read the full guide: See `README.md`
- Troubleshooting: See "Troubleshooting" section in `README.md`

---

**Happy humanizing! 🤖➡️👤**
