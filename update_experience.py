from datetime import date

start_date = date(2021, 11, 1)
today = date.today()

years = int((today - start_date).days // 365.25)

experience = f"+{years}"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

import re

new_content = re.sub(
    r"<!-- EXPERIENCE_START -->(.*?)<!-- EXPERIENCE_END -->",
    f"<!-- EXPERIENCE_START -->{experience}<!-- EXPERIENCE_END -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated README:", experience, "years experience")
