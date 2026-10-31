# AI-Powered Email Reply Assistant (with UI)

## Start the visual interface
1. Install Python 3.10+.
2.  open the `email-reply-assistant` folder in VS Code or a terminal.
3. Install packages: `pip install -r requirements.txt`
4. Copy `.env.example` to a new file named `.env`.
5. Put your own API key after `OPENAI_API_KEY=` in `.env`. Keep this file private.
6. Run: `streamlit run app.py`
7. A browser page should open. If not, open the local address printed in the terminal (usually `http://localhost:8501`).

## Using the UI
Paste the original email, select a purpose and tone, adjust creativity, then click **Generate email reply**. Review and copy the result or download it as a TXT file.

## Troubleshooting
- Missing/rejected API key: check `.env` exists beside `app.py` and contains a valid key.
- `streamlit` command not found: run `python -m pip install -r requirements.txt`.
- API quota error: check your API account usage.
- To capture the empty-input error screenshot, leave the email box blank and click Generate.
