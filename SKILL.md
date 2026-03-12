---
name: humbot-humanizer
description: Transform AI-generated text into more natural, human-like writing using the Humbot API. Use this skill whenever the user wants to humanize AI text, make text sound more natural, bypass AI detection, rewrite text to sound less robotic, or convert AI-written content into human-style writing. Also trigger when the user mentions "humanize", "make it sound human", "rewrite to avoid AI detection", or similar requests to transform text style.
---

# Humbot Humanizer

Transform AI-generated or robotic text into natural, human-like writing using the Humbot API.

## What This Skill Does

This skill takes text that sounds artificial, robotic, or AI-generated and rewrites it to sound more natural and human. It uses the Humbot API which specializes in:

- Removing AI-typical patterns and phrases
- Adding natural variation and flow
- Making text sound conversational and authentic
- Helping content pass AI detection tools

The process involves two API calls:
1. **Create** - Submit the text and get a task ID
2. **Retrieve** - Poll for results using the task ID

## When to Use This Skill

Use this skill when the user:
- Explicitly asks to "humanize" text
- Wants to make AI-generated content sound more natural
- Needs to rewrite text to avoid AI detection
- Mentions the text sounds "too robotic" or "too AI-like"
- Asks to make writing more conversational or authentic
- References "Humbot" or similar humanizing services

## How to Use

### Step 1: Get the Text

The user will provide text in one of these ways:
- Direct paste in the conversation
- Reference to a file (read it first)
- Request to humanize something you just generated

If the text is very long (>2000 words), confirm with the user before proceeding, as the API may have limits or take longer to process.

### Step 2: Call the Create API

Use the helper script to submit the text:

```bash
python scripts/create_task.py <input_text> [--model-type Quick|Standard|Advanced]
```

**Model types:**
- `Quick` (default) - Fast, good for most content
- `Standard` - Balanced quality and speed
- `Advanced` - Highest quality, slower

The script will return a task ID.

### Step 3: Retrieve Results

Poll for results using:

```bash
python scripts/retrieve_result.py <task_id>
```

The script automatically polls every 2 seconds until the task completes. When done, it displays:
- The humanized output text
- Word count (original vs humanized)
- Detection result (whether it passes as human)
- Detection score (0-100, higher = more human-like)

### Step 4: Present Results

Show the user:

**Original Text:** (show first ~150 words if long)

**Humanized Text:** (full output)

**Stats:**
- Original: X words → Humanized: Y words
- Detection Score: Z/100 (human-like)
- Mode: Quick/Standard/Advanced

If the detection score is low (<70) or the user isn't satisfied, offer to:
- Try a different model type (upgrade to Standard or Advanced)
- Make manual adjustments
- Resubmit with tweaks

## Error Handling

**Common issues:**

1. **Task takes too long** - Some tasks may take 30+ seconds for long text. Be patient and let the polling continue.

2. **API errors** - If you get authentication errors, the API key may have expired. Inform the user they need to update credentials in the scripts.

3. **Text too long** - If the API rejects text as too long, offer to:
   - Split into chunks and humanize separately
   - Summarize first, then humanize
   - Ask the user which section to prioritize

4. **Low quality output** - If the result isn't satisfactory:
   - Try a higher model tier
   - Suggest manual refinement
   - Ask if specific aspects need improvement

## Tips for Best Results

- **Context matters**: Longer text (100+ words) tends to produce better results than very short snippets
- **Clean input**: Remove formatting artifacts or code blocks before submitting
- **Model selection**: Start with Quick for testing, use Advanced for important content
- **Review output**: Always review the humanized text - it may need minor adjustments
- **Multiple attempts**: If the first result isn't great, trying again with a different model type often helps

## Credential Management

**⚠️ Important: API credentials must be configured before using this skill.**

### Setup Instructions

1. **Get credentials** from [Humbot.ai](https://humbot.ai):
   - API Key (format: `api_key_xxxxx`)
   - Authorization Header (format: `Basic xxxxx`)

2. **Set environment variables**:
   ```bash
   export HUMBOT_API_KEY="your_api_key_here"
   export HUMBOT_AUTH_HEADER="your_auth_header_here"
   ```

3. **Make them permanent** (add to ~/.bashrc or ~/.zshrc):
   ```bash
   echo 'export HUMBOT_API_KEY="your_api_key_here"' >> ~/.bashrc
   echo 'export HUMBOT_AUTH_HEADER="your_auth_header_here"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Verification

Test your credentials:
```bash
cd ~/.openclaw/workspace/skills/humbot-humanizer
python scripts/create_task.py "Test text" --model-type Quick
```

If you see "Error: HUMBOT_API_KEY environment variable not set", credentials are not configured.

## Examples

**Example 1: Humanizing AI-generated content**

User: "This sounds too AI-ish, can you humanize it? 'Artificial intelligence has revolutionized numerous industries by providing innovative solutions...'"

→ Run create_task.py → Get task_id → Run retrieve_result.py → Show humanized version

**Example 2: Making text pass AI detection**

User: "I wrote this with ChatGPT and need it to pass Turnitin. Can you help?"

→ (Read their text) → Explain we'll use Humbot → Process → Show detection score → Confirm it's improved

**Example 3: Improving writing style**

User: "Make this essay sound more natural and less robotic"

→ Process the essay → Show before/after → Highlight the detection score improvement

## Limitations

- **Not a magic fix**: Output still needs human review
- **Context preservation**: The API tries to keep meaning intact, but verify important details
- **Language support**: Primarily optimized for English
- **Speed**: Advanced mode can take 30-60 seconds for long texts
- **Cost**: Each API call consumes quota (if applicable to the user's account)

## When NOT to Use This Skill

Don't use this skill when:
- The user just wants grammar correction (use editing tools instead)
- They want translation (different task)
- They want to generate new content (not rewriting)
- The text is already clearly human-written and they just want edits

---

Remember: The goal is to help users create authentic-sounding content, not to deceive. Always encourage users to review and refine the output.
