import os
import PIL
import json
import google.generativeai as genai

# do not reveal your api key when submitting the assignment
GOOGLE_API_KEY = "API key"  
genai.configure(api_key=GOOGLE_API_KEY)
def list_genai_models():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
def read_file_as_string(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content
def prompt_response(recipe,prompt_text): 
    #Generate content based on input files: input_lunch_menu, kitchen, and prompt.  
    model = genai.GenerativeModel('gemini-pro')

    #menu_recipes = read_file_as_string("input.json")

    #kitchen_ingredients = read_file_as_string("kitchen.txt")
    prompt = prompt_text.format(recipe=recipe['dish'])
    #prompt_text = read_file_as_string("prompt.txt")

    response = model.generate_content(prompt)

    with open(f"{recipe['dish']}_Task_tree.json", "w") as f:        
        f.write(response.text)

if __name__ == "__main__":
    list_genai_models()
    prompt_text= read_file_as_string("prompt.txt")
    with open("input.json", "r") as json_file:
        categories = json.load(json_file)
    
    # Generate task tree for each recipe
    for category in categories:
        for recipe in category['menu']:
            prompt_response(recipe, prompt_text)

