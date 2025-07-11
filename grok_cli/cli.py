import click
from .agent import GrokAgent
from .GrokModels import GROK_MODELS
import os

ASCII_ART = """
                                                         ██    
                                                       ███     
                                                     ████      
                       ███████████████             ████        
                   ███████████████████████       █████         
                ████████████████████████████    █████          
              ███████████████████████████     ███████          
            ████████████                    ████████           
           ██████████                     ██████████           
          █████████                     ████████████           
         ████████                     ██████████████           
        ████████                     ███████████████           
        ███████                    ██████    ████████          
       ████████                  ██████       ███████          
       ████████                █████          ███████          
       ████████              █████            ███████          
       ████████            ████               ███████          
       ████████           ██                  ███████          
        ████████        ██                   ████████          
        ████████                            ████████           
         █████████                         █████████           
          █████████                      █████████             
         ████████                      ██████████              
         ██████       ██████     ███████████████               
        █████     ████████████████████████████                 
       ████      ███████████████████████████                   
     ████            ███████████████████                       
   ███                     ███████                             
  ███                                                          
███ 
"""

def print_grey(text):
    click.echo(click.style(text, fg='bright_black'))

def print_header(text):
    click.echo(click.style(text, fg='cyan', bold=True))

@click.command()
@click.option('--api-key',
              default=None,
              help='xAI API key. If not provided, uses XAI_API_KEY env var.')
def main(api_key):
    api_key = api_key or os.getenv('XAI_API_KEY')
    if not api_key:
        raise click.UsageError(
            "API key is required. Provide via --api-key or XAI_API_KEY environment variable. Get it from https://x.ai/api."
        )

    print_grey(ASCII_ART)

    while True:
        print_header("Welcome to the Grok Family CLI.")
        print_grey("1. 1. See available models")
        print_grey("2. Exit")
        choice = input(click.style("Enter your choice: ", fg='white'))

        if choice == '2' or choice.lower() == 'exit':
            print_grey("Goodbye!")
            break
        if choice == '1':
            model_options = list(GROK_MODELS.keys())
            print_header("\nAvailable Models:")
            for i, model_name in enumerate(model_options, 1):
                model_info = GROK_MODELS[model_name]
                print_grey(f"\n{i}. {model_name}")
                print_grey(f"   Description: {model_info['description']}")
                print_grey(f"   Modalities: {model_info['modalities']}")
                print_grey(f"   Capabilities: {model_info['capabilities']}")
                if model_info['context_length'] is not None:
                    print_grey(f"   Context Length: {model_info['context_length']}")
                print_grey(f"   Rate Limits: {model_info['rate_limits']}")
                print_grey(f"   Pricing: {model_info['pricing']}")
                print_grey(f"   Type: {model_info['type']}")

            while True:
                try:
                    choice = int(input(click.style("Select a model by number: ", fg='white')))
                    if 1 <= choice <= len(model_options):
                        selected_model = model_options[choice - 1]
                        break
                    else:
                        print_grey(f"Please enter a number between 1 and {len(model_options)}.")
                except ValueError:
                    print_grey("Invalid input. Please enter a number.")

            print_header(f"\nSelected model: {selected_model}")
            model_type = GROK_MODELS[selected_model]['type']
            agent = GrokAgent(api_key=api_key, model=selected_model)
            if model_type == 'image_generation':
                print_grey("Note: Entering image generation mode. Provide prompts to generate images. Type 'exit' to quit.")
                while True:
                    prompt = input(click.style("Image Prompt: ", fg='white'))
                    if prompt.lower() == 'exit':
                        break
                   
                    response = agent.client.images.generate("") # Note: agent not needed, use client
                    client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
                    response = client.images.generate(
                        model=selected_model,
                        prompt=prompt,
                        size='1024x1024',  # Assuming default
                        quality='standard',
                        n=1
                    )
                    image_url = response.data[0].url
                    print_grey(f"Generated image URL: {image_url}")
            else:
                if model_type == 'vision':
                    print_grey("Note: Vision models support image inputs, but this CLI is text-only. For full functionality, extend for multimodal inputs.")

                print_header("\nChat with the selected Grok model.")
                print_grey("Type 'exit' to quit.")
                while True:
                    user_input = input(click.style("You: ", fg='white'))
                    if user_input.lower() == 'exit':
                        print_grey("Chat ended.")
                        break
                    agent.chat(user_input)
        else:
            print_grey("Invalid choice. Please select 1 or 2.")