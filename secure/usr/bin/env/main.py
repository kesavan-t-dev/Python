#!/usr/bin/env python3


import cgi
import cgitb
import html
import os
import sys

cgitb.enable() 

try:
    from cryptography.fernet import Fernet
except Exception as e:
    print("Content-Type: text/plain; charset=utf-8\n")
    print("ERROR: 'cryptography' package not installed or not importable.\n")
    print("Install: pip install cryptography\n")
    print("Details:", e)
    sys.exit(0)


def page(title, body_html):
    print("Content-Type: text/html; charset=utf-8\n")
    print(f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    .box {{ max-width: 900px; }}
    textarea, input[type=text] {{ width: 100%; padding: 10px; margin: 6px 0 12px; }}
    textarea {{ height: 120px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    .row {{ display: flex; gap: 12px; }}
    .row > div {{ flex: 1; }}
    button {{ padding: 10px 14px; cursor: pointer; }}
    .ok {{ background: #e9f7ef; padding: 10px; border: 1px solid #b6e2c7; }}
    .err {{ background: #fdecea; padding: 10px; border: 1px solid #f5c2c7; }}
    .hint {{ color: #444; font-size: 0.95rem; }}
  </style>
</head>
<body>
  <div class="box">
    <h1>{html.escape(title)}</h1>
    {body_html}
    <hr>
    <p class="hint">
      Tip: Use <b>Fernet</b> for a simple “it works” validation (includes integrity check).
      Turn off <code>cgitb.enable()</code> in production.
    </p>
  </div>
</body>
</html>""")


def safe(s):
    return html.escape(s or "")


form = cgi.FieldStorage()
action = (form.getfirst("action") or "").strip().lower()
key_in = (form.getfirst("key") or "").strip()
plain_in = form.getfirst("plaintext") or ""
cipher_in = (form.getfirst("ciphertext") or "").strip()

if action == "genkey":
    new_key = Fernet.generate_key().decode("utf-8")
    body = f"""
    <div class="ok"><b>Generated Fernet Key:</b><br><code>{safe(new_key)}</code></div>
    <p>Copy this key into the Key field below and try Encrypt/Decrypt.</p>
    """
    action = ""  
else:
    body = ""


result_html = ""

if action in ("encrypt", "decrypt"):
    try:
        if not key_in:
            raise ValueError("Key is required. Click 'Generate Key' or paste your Fernet key.")

        f = Fernet(key_in.encode("utf-8"))

        if action == "encrypt":
            token = f.encrypt(plain_in.encode("utf-8")).decode("utf-8")
            result_html = f"""
            <div class="ok">
              <b>Encrypted Token (ciphertext):</b>
              <textarea readonly>{safe(token)}</textarea>
            </div>
            """
            cipher_in = token  
        elif action == "decrypt":
            recovered = f.decrypt(cipher_in.encode("utf-8")).decode("utf-8")
            result_html = f"""
            <div class="ok">
              <b>Decrypted Plaintext:</b>
              <textarea readonly>{safe(recovered)}</textarea>
            </div>
            """
            plain_in = recovered  
    except Exception as e:
        result_html = f"""
        <div class="err">
          <b>Error:</b> {safe(str(e))}
        </div>
        """


form_html = f"""
{body}
<form method="post">
  <label><b>Fernet Key</b> (paste or generate)</label>
  <input type="text" name="key" value="{safe(key_in)}" placeholder="e.g. vqv... (base64 key)">
  <div class="row">
    <div>
      <label><b>Plaintext</b></label>
      <textarea name="plaintext" placeholder="Type message to encrypt...">{safe(plain_in)}</textarea>
      <button type="submit" name="action" value="encrypt">Encrypt</button>
    </div>
    <div>
      <label><b>Ciphertext Token</b></label>
      <textarea name="ciphertext" placeholder="Paste token to decrypt...">{safe(cipher_in)}</textarea>
      <button type="submit" name="action" value="decrypt">Decrypt</button>
    </div>
  </div>
  <p>
    <button type="submit" name="action" value="genkey">Generate Key</button>
  </p>
</form>

{result_html}
"""

page("Python CGI Crypto Test (Fernet)", form_html)