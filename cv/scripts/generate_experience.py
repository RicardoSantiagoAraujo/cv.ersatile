from experience import Experience
from datetime import date

experienceDict = {
    "livingpackets": Experience(
        postTitle={"Title": "Data analyst"},
        employer={"Employer": "Living Packets"},
        startDate=date(2025, 2, 24),
        endDate=date.today(),
        location={"Location": "Nantes"},
        content="Content goes here",
    ),
    "soprasteria": Experience(
        postTitle={"Title": "Software Enginner"},
        employer={"Employer": "Sopra Steria"},
        startDate=date(2023, 1, 14),
        endDate=date(2025, 1, 14),
        location={"Location": "Toulouse"},
        content="Content goes here",
    ),
    "phd": Experience(
        postTitle={"Title": "PhD Student"},
        employer={"Funding": "CNRS"},
        startDate=date(2019, 10, 1),
        endDate=date(2023, 4, 1),
        location={"Location": "Toulouse"},
        content="Content goes here",
    ),
}



# Python script to generate a LaTeX file

# Define the LaTeX content as a string
latex_content = r"""

"""

for key, value in experienceDict.items():
    # Open a new .tex file and write the LaTeX content into it
    with open("experience_template.tex", "r") as tex_file:
        tex_content = tex_file.read()
        tex_content = tex_content.replace("postTitle", key)
        # print(tex_content)
    latex_content += tex_content


# Open a new .tex file and write the LaTeX content into it
with open("sample_document.tex", "w") as tex_file:
    tex_file.write(latex_content)

print("LaTeX file generated successfully!")
