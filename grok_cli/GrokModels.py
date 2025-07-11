GROK_MODELS = {
    "grok-4-0709": {
        "description":
        "Advanced language model with large context window and strong reasoning capabilities.",
        "modalities": "Text to Text",
        "capabilities":
        "Function calling, structured outputs (e.g., JSON mode), advanced reasoning",
        "context_length": 256000,
        "rate_limits":
        "16K tokens per minute (tpm), 60 requests per minute (rpm)",
        "pricing":
        "$3.00 per million input tokens, $15.00 per million output tokens",
        "type": "language"
    },
    "grok-3": {
        "description":
        "High-performance language model suitable for a wide range of tasks.",
        "modalities": "Text to Text",
        "capabilities":
        "Function calling, structured outputs (e.g., JSON mode), advanced reasoning",
        "context_length": 131072,
        "rate_limits": "600 requests per minute (rpm)",
        "pricing":
        "$3.00 per million input tokens, $15.00 per million output tokens",
        "type": "language"
    },
    "grok-3-mini": {
        "description":
        "Compact and efficient language model for cost-sensitive applications.",
        "modalities": "Text to Text",
        "capabilities":
        "Function calling, structured outputs (e.g., JSON mode), advanced reasoning",
        "context_length": 131072,
        "rate_limits": "480 requests per minute (rpm)",
        "pricing":
        "$0.30 per million input tokens, $0.50 per million output tokens",
        "type": "language"
    },
    "grok-3-fast": {
        "description":
        "Optimized for speed while maintaining strong performance.",
        "modalities": "Text to Text",
        "capabilities":
        "Function calling, structured outputs (e.g., JSON mode), advanced reasoning",
        "context_length": 131072,
        "rate_limits": "600 requests per minute (rpm)",
        "pricing":
        "$5.00 per million input tokens, $25.00 per million output tokens",
        "type": "language"
    },
    "grok-3-mini-fast": {
        "description": "Fast and lightweight model for quick responses.",
        "modalities": "Text to Text",
        "capabilities":
        "Function calling, structured outputs (e.g., JSON mode), advanced reasoning",
        "context_length": 131072,
        "rate_limits": "180 requests per minute (rpm)",
        "pricing":
        "$0.60 per million input tokens, $4.00 per million output tokens",
        "type": "language"
    },
    "grok-2-image-1212": {
        "description":
        "Image generation model for creating images from text prompts.",
        "modalities": "Text to Image",
        "capabilities": "Image generation, flux-based diffusion model",
        "context_length": None,  # Not applicable for image generation
        "rate_limits": "300 requests per minute (rpm)",
        "pricing": "$0.07 per image output",
        "type": "image_generation"
    }
}
