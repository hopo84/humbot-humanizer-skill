# 🎉 Humbot Humanizer Skill Installed!

Thank you for installing the Humbot Humanizer skill. Before you can use it, you need to configure your API key.

## ⚠️ Required: Get Your API Key

1. **Visit the Humbot API Portal:**
   👉 **https://humbot.ai/ai-humanizer-api**

2. **Register or log in** to your account

3. **Get your API key** from the dashboard

4. **Configure the API key** by running:
   ```bash
   echo 'export HUMBOT_API_KEY="your_api_key_here"' >> ~/.bashrc
   source ~/.bashrc
   ```
   
   Replace `your_api_key_here` with your actual API key.

5. **Test it works:**
   ```bash
   cd ~/.openclaw/workspace/skills/humbot-humanizer
   python scripts/create_task.py "Test humanization"
   ```

## 📖 What's Next?

Once configured, you can:

- Ask the AI: **"Humanize this text: [your text]"**
- Use the command line directly (see README.md)
- Process files, choose quality modes, and more

For detailed usage instructions, see **README.md** in this skill directory.

## 🆘 Need Help?

If you encounter any issues:
1. Check that `HUMBOT_API_KEY` is set: `echo $HUMBOT_API_KEY`
2. Verify your API key is active at https://humbot.ai
3. Read the troubleshooting section in README.md

---

**Important:** Never share your API key publicly or commit it to version control!
