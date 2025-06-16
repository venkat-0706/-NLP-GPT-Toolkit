import openai

# OpenAI API key
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def generate_code(prompt, max_tokens=300):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def exploratory_data_analysis(dataset_description):
    prompt = (
        f"Generate Python code for exploratory data analysis using pandas on a dataset with the following description:\n"
        f"{dataset_description}\n"
        "Include summary statistics, data info, and any useful insights."
    )
    return generate_code(prompt)

def data_visualization(dataset_description):
    prompt = (
        f"Generate Python code for data visualization using matplotlib and seaborn on a dataset with the following description:\n"
        f"{dataset_description}\n"
        "Include a histogram, boxplot, and correlation heatmap where applicable."
    )
    return generate_code(prompt)

def generate_resume(experience_paragraph):
    prompt = (
        f"Generate a professional resume from the following paragraph about experience and skillset:\n"
        f"{experience_paragraph}"
    )
    return generate_code(prompt, max_tokens=500)

def generate_interview_questions(programming_language, num_questions=5):
    prompt = (
        f"Generate a set of {num_questions} interview questions in {programming_language} programming language "
        "covering basics, data structures, and algorithms."
    )
    return generate_code(prompt)

def generate_meeting_summary(meeting_notes):
    prompt = (
        f"Generate a concise summary from the following meeting notes:\n"
        f"{meeting_notes}"
    )
    return generate_code(prompt)

if __name__ == "__main__":
    # Example dynamic inputs
    dataset_desc = "columns: 'age', 'salary', 'department', 1000 rows of employee data"
    experience_text = (
        "Experienced software engineer with 5 years in full-stack development, skilled in Python, JavaScript, "
        "and cloud technologies. Proven track record in delivering scalable web applications and leading teams."
    )
    meeting_notes_text = (
        "Max: Profits up 50%\n"
        "Ruby: New servers are online\n"
        "Kyle: Need more time to fix software\n"
        "Walker: Happy to help\n"
        "Parkman: Beta testing almost done"
    )

    print("Exploratory Data Analysis Code:\n")
    print(exploratory_data_analysis(dataset_desc))
    print("\nData Visualization Code:\n")
    print(data_visualization(dataset_desc))
    print("\nGenerated Resume:\n")
    print(generate_resume(experience_text))
    print("\nInterview Questions:\n")
    print(generate_interview_questions("Python", 5))
    print("\nMeeting Summary:\n")
    print(generate_meeting_summary(meeting_notes_text))
