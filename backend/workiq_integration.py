"""
Work IQ Integration - English Version for Hackathon MVP
This is a faithful mock implementation of Microsoft Work IQ
Extracts mood from workplace communication (emails, meetings)
"""

def analyze_sentiment(emails, meeting_transcripts):
    """
    Simulates Work IQ sentiment analysis
    Analyzes text and returns mood keywords
    """
    
    all_text = " ".join(emails) + " " + " ".join(meeting_transcripts)
    all_text_lower = all_text.lower()
    
    mood_keywords = []
    
    # Keyword lists for different moods
    urgency_words = ["urgent", "asap", "deadline", "quick", "immediately", "fast", "now"]
    stress_words = ["stress", "tired", "overwhelmed", "busy", "hard", "difficult", "pressure"]
    confidence_words = ["confident", "great", "excellent", "proud", "win", "success", "achievement"]
    calm_words = ["calm", "relaxed", "take time", "easy", "slow", "steady", "peaceful"]
    
    if any(word in all_text_lower for word in urgency_words):
        mood_keywords.append("urgent")
    if any(word in all_text_lower for word in stress_words):
        mood_keywords.append("stressed")
    if any(word in all_text_lower for word in confidence_words):
        mood_keywords.append("confident")
    if any(word in all_text_lower for word in calm_words):
        mood_keywords.append("calm")
    
    if not mood_keywords:
        mood_keywords.append("neutral")
    
    # Determine primary sentiment
    if "urgent" in mood_keywords or "stressed" in mood_keywords:
        primary_sentiment = "high_energy"
    elif "calm" in mood_keywords:
        primary_sentiment = "low_energy"
    elif "confident" in mood_keywords:
        primary_sentiment = "confident"
    else:
        primary_sentiment = "balanced"
    
    return {
        "keywords": mood_keywords,
        "primary_sentiment": primary_sentiment,
        "confidence": 0.85
    }


def generate_color_palette(mood_keywords, primary_sentiment):
    """
    Generates color palette based on mood keywords
    Returns list of 5 hex codes
    """
    
    if "urgent" in mood_keywords:
        # Red/orange theme - urgency
        return ["#FF4444", "#FF6666", "#CC0000", "#FF8888", "#990000"]
    elif "stressed" in mood_keywords:
        # Orange/brown theme - tension
        return ["#FF8844", "#FFAA66", "#CC5500", "#FFCC88", "#884400"]
    elif "confident" in mood_keywords:
        # Blue theme - trust, professionalism
        return ["#0044CC", "#3366FF", "#002299", "#6688FF", "#001166"]
    elif "calm" in mood_keywords:
        # Green theme - peace, nature
        return ["#44AA44", "#66CC66", "#228822", "#88DD88", "#115511"]
    else:
        # Neutral gray theme
        return ["#888888", "#AAAAAA", "#666666", "#CCCCCC", "#444444"]


def generate_style_directions(mood_keywords):
    """
    Generates visual style directions based on mood
    Returns dict with imagery, lighting, texture, example visuals
    """
    
    if "urgent" in mood_keywords or "stressed" in mood_keywords:
        return {
            "imagery": "Dynamic, sharp contrast, high energy photography",
            "lighting": "Dramatic, high contrast, directional lighting",
            "texture": "Bold, gritty, concrete or metal textures",
            "example_visuals": "Motion blur, close-up, urban, fast-paced"
        }
    elif "confident" in mood_keywords:
        return {
            "imagery": "Clean, professional, studio photography",
            "lighting": "Bright, even, soft box lighting",
            "texture": "Smooth, glossy, premium feel",
            "example_visuals": "Corporate, minimalist, geometric, polished"
        }
    elif "calm" in mood_keywords:
        return {
            "imagery": "Soft, natural, landscape photography or illustration",
            "lighting": "Warm, golden hour, diffused light",
            "texture": "Organic, paper texture, matte finish",
            "example_visuals": "Nature, abstract organic shapes, peaceful scenes"
        }
    else:
        return {
            "imagery": "Balanced, versatile, lifestyle photography",
            "lighting": "Natural, soft, ambient",
            "texture": "Clean, subtle grain, approachable",
            "example_visuals": "Everyday moments, authentic, relatable"
        }