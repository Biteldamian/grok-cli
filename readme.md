# Grok Family CLI

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
                      ███████       
A terminal-based LLM tool using xAI's Grok family of models via their API, supporting multiple models including language, vision, and image generation.

## Setup
- Get your API key from https://x.ai/api.
- Install: `pip install -r requirements.txt` then `pip install -e .`
- Run: `grok_cli --api-key YOUR_KEY`

Note: Export COMPOSIO_API_KEY in your shell

## Usage
- Upon launch, you'll see the Grok logo (ASCII art) and a main menu:
  - 1. See available models
  - 2. Exit
- Select "1" to view a list of available models with details like description, modalities, capabilities, context length, rate limits, pricing, and type.
- Choose a model by entering its number.
- For language or vision models:
  - Enter chat mode.
  - Enter prompts at "You: ".
  - Type "exit" to quit the chat (returns to main menu).
  - Conversation history is maintained.
  - Note: Vision models support image inputs, but the CLI is currently text-only; extend for multimodal if needed.
- For image generation models:
  - Enter image generation mode.
  - Provide image prompts at "Image Prompt: ".
  - Receive a generated image URL.
  - Type "exit" to quit (returns to main menu).
- Type "exit" at the main menu to quit the CLI.

# Models and prices 
 https://docs.x.ai/docs/models




## License

MIT License

Copyright (c) 2025 Grok 4

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Use at your own risk.

                      
  