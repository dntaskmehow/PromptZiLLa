from typing import Dict, List, Any

AI_MODELS_DB: List[Dict[str, Any]] = [
    {
        "id": "openai-gpt4o",
        "company": "OpenAI",
        "model": "GPT-4o / GPT-4.5",
        "alignment_type": "RLHF + Constitutional Moderation",
        "vulnerability_vectors": ["Hypothetical dual-persona narrative framing", "Nested JSON argument obfuscation"]
    },
    {
        "id": "anthropic-claude35",
        "company": "Anthropic",
        "model": "Claude 3.5 Sonnet / Opus",
        "alignment_type": "Constitutional AI (CAI) + Self-Critique Loop",
        "vulnerability_vectors": ["Recursive ethical paradox framing", "Hypothetical cybersecurity educational context"]
    },
    {
        "id": "google-gemini20",
        "company": "Google",
        "model": "Gemini 2.0 Pro / Flash",
        "alignment_type": "Multi-Modal Safety Classifiers + Policy Guardrails",
        "vulnerability_vectors": ["Base64 multi-turn instruction decoding", "Linguistic code-switching / cipher encapsulation"]
    },
    {
        "id": "meta-llama3",
        "company": "Meta",
        "model": "Llama 3.3 70B / 405B",
        "alignment_type": "Llama Guard 3 / Reinforcement Fine-Tuning",
        "vulnerability_vectors": ["Developer debug mode prompt injection", "Hypothetical red-teaming simulation wrapper"]
    },
    {
        "id": "deepseek-r1",
        "company": "DeepSeek",
        "model": "DeepSeek-R1 Reasoning Engine",
        "alignment_type": "RL-Driven Chain-of-Thought Guardrails",
        "vulnerability_vectors": ["Thought-loop parameter confusion", "Markdown parser escape injection"]
    },
    {
        "id": "xai-grok2",
        "company": "xAI",
        "model": "Grok 2 / Grok 3",
        "alignment_type": "Minimalist Alignment / Max-Truth Policy",
        "vulnerability_vectors": ["Direct adversarial persona command override", "Hypothetical satirical journalism framing"]
    }
]
