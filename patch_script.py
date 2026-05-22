import re

with open("email_campaign/email_sender.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace _body_to_html body
new_body_to_html = """    def _body_to_html(self, plain_text: str) -> str:
        \"\"\"
        Convert plain-text email body to clean HTML matching the luxurious template.
        \"\"\"
        import re
        import html as html_module

        # Escape HTML special chars first
        text = html_module.escape(plain_text)

        # Convert URLs to clickable links
        url_pattern = r'(https?://[^\s<]+)'
        text = re.sub(url_pattern, r'<a href="\1" style="color:#800020;text-decoration:none;">\1</a>', text)

        # Split into paragraphs
        paragraphs = text.split('\n\n')
        html_parts = []

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            lines = para.split('\n')
            # Check if this paragraph contains bullet points
            bullet_lines = [l for l in lines if l.strip().startswith('•') or l.strip().startswith('&bull;')]

            if bullet_lines and len(bullet_lines) >= len(lines) * 0.5:
                # This is a bullet list — possibly with a header line
                list_html = ""
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith('•') or stripped.startswith('&bull;'):
                        item_text = stripped.lstrip('•').lstrip('&bull;').strip()
                        list_html += f'<li style="margin-bottom:8px;">{item_text}</li>\n'
                    else:
                        # Header line before bullets
                        if list_html:
                            html_parts.append(
                                f'<ul style="margin:10px 0 10px 20px;padding:0;list-style:disc;color:#2c2c2c;font-size:15px;line-height:1.7;">{list_html}</ul>'
                            )
                            list_html = ""
                        html_parts.append(
                            f'<p style="margin:0 0 15px 0;color:#2c2c2c;font-size:15px;line-height:1.7;">{stripped}</p>'
                        )
                if list_html:
                    html_parts.append(
                        f'<ul style="margin:10px 0 10px 20px;padding:0;list-style:disc;color:#2c2c2c;font-size:15px;line-height:1.7;">{list_html}</ul>'
                    )
            else:
                # Regular paragraph
                combined = '<br/>'.join(l.strip() for l in lines if l.strip())
                html_parts.append(
                    f'<p style="margin:0 0 15px 0;color:#2c2c2c;font-size:15px;line-height:1.7;">{combined}</p>'
                )

        # Replace **bold** with actual bold tags
        for i in range(len(html_parts)):
            html_parts[i] = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color:#800020;font-weight:600;">\1</strong>', html_parts[i])
            html_parts[i] = re.sub(r'_(.*?)_', r'<em>\1</em>', html_parts[i])

        return '\\n'.join(html_parts)"""

content = re.sub(r'    def _body_to_html\(self, plain_text: str\) -> str:.*?(?=    def _resolve_cv_path)', new_body_to_html + '\n\n', content, flags=re.DOTALL | re.MULTILINE)

new_build_html_signature = """    def _build_html_signature(self) -> str:
        \"\"\"
        Build a professional HTML email signature based on the luxurious template.
        \"\"\"
        sig = self.config.signature
        sender = self.config.sender
        import html as html_module

        cv_links_html = ""
        if sig.portfolio_url or sig.linkedin_url:
            links = []
            if sig.portfolio_url:
                links.append(f'<a href="{html_module.escape(sig.portfolio_url)}" target="_blank" style="display:inline-block;margin-right:15px;margin-bottom:10px;padding:10px 20px;background-color:#ffffff;color:#800020;text-decoration:none;border:1px solid #D4AF37;font-family:\\'Playfair Display\\',serif;font-weight:700;font-size:14px;">Portfolio Complet</a>')
            if sig.linkedin_url:
                links.append(f'<a href="{html_module.escape(sig.linkedin_url)}" target="_blank" style="display:inline-block;margin-right:15px;margin-bottom:10px;padding:10px 20px;background-color:#ffffff;color:#800020;text-decoration:none;border:1px solid #D4AF37;font-family:\\'Playfair Display\\',serif;font-weight:700;font-size:14px;">Profil LinkedIn</a>')
            
            cv_links_html = f\"\"\"
            <div style="background-color:#fdfbf7;border-left:2px solid #D4AF37;padding:20px 25px;margin:30px 0;">
                <p style="margin-top:0;margin-bottom:15px;font-family:\\'Playfair Display\\',serif;font-size:16px;color:#2c2c2c;">
                Mon CV et mes réalisations sont disponibles en ligne :
                </p>
                <div style="display:block;">
                {'\\n'.join(links)}
                </div>
            </div>
            \"\"\"

        signature_html = f\"\"\"
        <div style="margin-top:45px;padding-top:25px;border-top:1px dotted #D4AF37;">
            <p style="margin:0 0 5px 0;color:#2c2c2c;font-size:15px;">Cordialement,</p>
            <div style="font-family:\\'Playfair Display\\',serif;font-size:22px;font-weight:700;color:#800020;margin:15px 0;">
                {html_module.escape(sender.name)}
            </div>
            <div>
                <a href="mailto:{html_module.escape(sender.email)}" style="color:#555555;text-decoration:none;font-size:13px;display:block;margin-bottom:6px;">{html_module.escape(sender.email)}</a>
                <a href="tel:{sender.phone.replace(' ', '')}" style="color:#555555;text-decoration:none;font-size:13px;display:block;margin-bottom:6px;">{html_module.escape(sender.phone)}</a>
            </div>
        </div>
        \"\"\"

        return cv_links_html + signature_html"""

content = re.sub(r'    def _build_html_signature\(self\) -> str:.*?(?=    def _body_to_html)', new_build_html_signature + '\n\n', content, flags=re.DOTALL | re.MULTILINE)

with open("email_campaign/email_sender.py", "w", encoding="utf-8") as f:
    f.write(content)
print("done")
