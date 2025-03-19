
# LLM Quiz Proctor

## Overview
This is very simple self-study or educational tool which proctors multiple choice tests from the command line. 

## Purpose
The script consumes test questions provided in JSON format. The purpsose of this is that LLMs will easily generate multiple choice questions in JSON format on any topic given the context. 

## Usage
```bash
python proctor.py <path_to_test.json>
```
## Creating Tests 
Provide you own version of the following prompt template to your LLM of choice to generate a test. Ensure the format of the generated JSON matches exactly the provided template. You're ready to begin testing!
```json
You are helping me a subject matter by providing me with questions and answers, but I can only read JSON. 
Given the following example of JSON, 

{
    "questions":[
        {
            "id": 1,
            "category": "Geography",
            "question": "What is the capital of France?",
            "a": "Berlin", 
            "b": "Madrid",
            "c": "Paris",
            "d": "Rome",
            "answer": "c"
        },
        {
            "id": 2,
            "category": "Trivia",
            "question": "What is the chemical symbol for water?",
            "a": "CH4", 
            "b": "H2O",
            "c": "NaCL",
            "d": "Au",
            "answer": "b"
        }
    ]
}

generate 20 multiple choice questions using this JSON format on only topic of <your_topic_here>. 
```

## License
This project is licensed under the MIT License.
