"""
LinguaBridge — Context-Aware Language Learning Assistant
Author: Popuri Sai Vedagna

Description:
LinguaBridge is an AI-powered language learning tool that helps users
understand words and phrases from a target language by explaining them
using examples from the user's native language.

The system generates:
- Meaning of the word or phrase
- Example sentences
- Contextual explanation in the user's native language
"""

import requests

API_KEY = "YOUR_OPENAI_API_KEY"

API_URL = "https://api.openai.com/v1/chat/completions"


def generate_learning_content(native_language, target_language, phrase):

    prompt = f"""
You are a language tutor.

Explain the word or phrase '{phrase}' from {target_language}
to someone whose native language is {native_language}.

Provide the following:

1. Meaning
2. Two example sentences
3. Explanation in {native_language}
4. A learning tip
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code != 200:
        return "Error communicating with the language model."

    result = response.json()

    return result["choices"][0]["message"]["content"]


def main():

    print("\nLinguaBridge Language Learning Assistant\n")

    native_language = input("Enter your native language: ").strip()
    target_language = input("Language you want to learn: ").strip()
    phrase = input("Enter a word or phrase: ").strip()

    explanation = generate_learning_content(
        native_language,
        target_language,
        phrase
    )

    print("\nLearning Output\n")
    print(explanation)


if __name__ == "__main__":
    main()
