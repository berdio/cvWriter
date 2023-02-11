import os
import openai
import json
from dotenv import load_dotenv


class Copilot:

    cover_letter_instruction = """
    \n[INSTRUCTION]
    \nWrite me Outstanding Cover Letter for [JOB] based on my [RESUME]\n
    """

    resume_instruction = """
    \n[INSTRUCTION]
    \nWrite me Outstanding Resume for [JOB] based on my [RESUME]\n
    """

    const_resume_text = """
    \n[RESUME]\n
    Here is my resume: \n\n
    """

    const_job_text = """
    \n[JOB]\n
    Here is Job: \n\n
    """

    def clear_text(self, text):
        a = text.replace("\n", " ")
        b = a.split()
        c = " ".join(b)

        return c

    def get_cover_letter(self, resume, job):
        load_dotenv()

        prompt = self.cover_letter_instruction + self.const_resume_text + resume + self.const_job_text + job
        print('\n-----------Cover Letter-----------\n')
        print(prompt)

        openai.api_key = os.getenv("CHAT_GPT3_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.cover_letter_instruction + self.const_resume_text + resume + self.const_job_text + job,
            max_tokens=512,
            temperature=0.7,
        )

        json_object = response

        # Convert the JSON object to a JSON string
        json_string = json.dumps(json_object)

        # Parse the JSON string using json.loads()
        parsed_json = json.loads(json_string)

        text = parsed_json['choices'][0]['text']
        cleared_text = self.clear_text(text)
        
        return cleared_text

    def get_resume(self, resume, job):
        load_dotenv()

        prompt = self.resume_instruction + self.const_resume_text + resume + self.const_job_text + job
        print('\n-----------Resume-----------\n')
        print(prompt)

        openai.api_key = os.getenv("CHAT_GPT3_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=512,
            temperature=0.7,
        )

        json_object = response

        # Convert the JSON object to a JSON string
        json_string = json.dumps(json_object)

        # Parse the JSON string using json.loads()
        parsed_json = json.loads(json_string)

        text = parsed_json['choices'][0]['text']
        cleared_text = self.clear_text(text)
        
        return cleared_text

