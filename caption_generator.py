
#install required libraries
!pip install google-generativeai --quiet
!pip install ipywidgets --quiet

#import libraries
import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown

#set up Gemini API
API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.5-flash")

# define the input fields
theme_input = widgets.Text(
    placeholder='Enter a theme',
    description='Theme:',
    layout=widgets.Layout(width='400px')
)

tone_input = widgets.Dropdown(
    description='Tone',
    options=['Witty', 'Romantic', 'Inspirational', 'Funny', 'Professional'],
    layout=widgets.Layout(width='400px')
)

audience_input = widgets.Text(
    description='Audience',
    placeholder='e.g., Instagram followers, brand clients',
    layout=widgets.Layout(width='400px')
)

hashtag_input = widgets.Text(
    description='Hashtags',
    placeholder='#travel #vibes',
    layout=widgets.Layout(width='400px')
)

submit_button = widgets.Button(
    description='Generate Caption',
    button_style='info',
    tooltip='Click to generate caption',
    layout=widgets.Layout(width='400px')
)

output = widgets.Output()

# Define the caption generation function
def generate_caption(b):
    output.clear_output()
    prompt = f"""
    You are a professional content writer.
    Generate an engaging caption for a post themed around "{theme_input.value}".
    The tone should be {tone_input.value}.
    Target it to the audience: {audience_input.value}.
    Include these hashtags: {hashtag_input.value}.
    Keep it under 250 characters.
    """
    with output:
        try:
            response = model.generate_content(prompt)
            caption = response.text.strip()
            display(Markdown(f"### Generated Caption: \n\n {caption}"))
        except Exception as e:
            print("Error:", e)

# Attach the function to button
submit_button.on_click(generate_caption)

# Display the form
form = widgets.VBox([
    widgets.HTML(value="<h3>📸 Caption Generator Agent</h3>"),
    theme_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])
display(form)
