# Role_Based_Chatbot
Role based Chatbot which has a dictionary which contain 5 pairs to answer user.<br>
Rule-Based AI Chatbot (DecodeLabs Industrial Training Kit, Batch 2026)<br>
Context: This is the foundation project for an AI Engineer internship track. Before working with "real" AI/ML, the goal is to master control flow and decision-making logic — the building blocks underlying more complex AI systems.<br>
Core Goal: Build a simple rule-based chatbot that responds to predefined user inputs using explicit if-else/lookup logic, running in a continuous loop.<br>
Key Concepts Covered:<br>

Two "minds" of AI: probabilistic (neural networks/LLMs) vs. deterministic (rule-based logic) — this project focuses on the deterministic side.<br>
Why rule-based logic still matters: traceability (clear input→logic→output), safety (zero hallucination risk), and compliance (important in finance/healthcare). It's framed as the same principle behind modern "AI guardrail" systems (e.g., NVIDIA NeMo, Llama Guard) that sit in front of LLMs.
IPO Model: Input (sanitize/normalize) → Process (match intent, maintain state) → Output (generate response, loop back).<br>
Anti-pattern warning: long if-elif ladders are called out as inefficient (O(n) linear lookup) and hard to maintain.<br>
Recommended approach: use a dictionary/hash map for O(1) constant-time lookups, with Python's .get(key, default) method to elegantly combine lookup + fallback in one line.
Forward-looking bridge: this exact-match dictionary approach is contrasted with Project 2's likely direction — semantic/vector-based matching (embeddings) instead of exact keys.<br>
<br>

Technical Requirements (Spec Checklist):<br>
<br>
Input Loop – continuous while True loop<br>
Sanitization – normalize case and whitespace (.lower().strip())<br>
Knowledge Base – a dictionary with 5+ intents/responses<br>
Fallback – default response for unrecognized input<br>
Exit Strategy – a clean "kill command" (e.g., typing "exit") to break the loop<br>

