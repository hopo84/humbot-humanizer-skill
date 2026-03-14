# Changelog

## Version 2.0.0 (2026-03-14)

### 🚀 Major Updates

- **Production API endpoints:** Switched from test environment to production
  - Create: `https://humbot.ai/api/humbot/v1/create`
  - Retrieve: `https://humbot.ai/api/humbot/v1/retrieve`

- **Simplified authentication:** Removed Basic Authorization requirement
  - Now only requires `api-key` header
  - Users must get their own API key from https://humbot.ai/ai-humanizer-api

- **Environment-based configuration:**
  - API key now stored in `HUMBOT_API_KEY` environment variable
  - No hardcoded credentials in scripts
  - Better security and user privacy

### 📖 New Documentation

- Added comprehensive `README.md` with setup guide
- Added `INSTALL.md` for post-installation instructions
- Updated `SKILL.md` with API key configuration workflow
- Added this `CHANGELOG.md`

### ✨ Improvements

- Scripts now validate API key presence before making requests
- Clear error messages guide users to get their API key
- Better security: no credentials committed to code
- Easier multi-user setup: each user uses their own key

### 🔄 Migration Guide

If you were using the old version:

1. **Get your own API key** from https://humbot.ai/ai-humanizer-api
2. **Set the environment variable:**
   ```bash
   echo 'export HUMBOT_API_KEY="your_key_here"' >> ~/.bashrc
   source ~/.bashrc
   ```
3. **Test the new setup:**
   ```bash
   python scripts/create_task.py "test"
   ```

### ⚠️ Breaking Changes

- Hardcoded API credentials removed from scripts
- Users must configure their own `HUMBOT_API_KEY`
- API base URL changed from test to production environment

---

## Version 1.0.0 (Initial Release)

- Basic Humbot API integration
- Support for Quick/Standard/Advanced modes
- Task creation and result retrieval
- Test environment endpoints
