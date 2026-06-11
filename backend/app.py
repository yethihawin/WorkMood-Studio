from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from backend.workiq_integration import analyze_sentiment, generate_color_palette, generate_style_directions

app = FastAPI(title="WorkMood Studio API", description="AI Mood Board Generator with Microsoft Work IQ")

# Request model
class MoodRequest(BaseModel):
    emails: List[str]
    meeting_transcripts: List[str]

# Response model
class MoodResponse(BaseModel):
    mood_keywords: List[str]
    color_palette: List[str]
    style_directions: dict
    primary_sentiment: str

@app.get("/")
def root():
    return {"message": "WorkMood Studio API is running with Work IQ integration"}

@app.post("/generate-mood-board")
def generate_mood_board(request: MoodRequest):
    """
    Generates mood board from emails and meeting transcripts
    Uses Work IQ mock implementation
    """
    try:
        # Step 1: Analyze sentiment with Work IQ
        sentiment_result = analyze_sentiment(request.emails, request.meeting_transcripts)
        
        mood_keywords = sentiment_result["keywords"]
        primary_sentiment = sentiment_result["primary_sentiment"]
        
        # Step 2: Generate color palette based on mood
        color_palette = generate_color_palette(mood_keywords, primary_sentiment)
        
        # Step 3: Generate style directions
        style_directions = generate_style_directions(mood_keywords)
        
        return MoodResponse(
            mood_keywords=mood_keywords,
            color_palette=color_palette,
            style_directions=style_directions,
            primary_sentiment=primary_sentiment
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/refine-tone")
def refine_tone(mood_keywords: List[str], adjustment: str):
    """
    Refines tone based on user adjustment
    adjustment: "more_urgent", "more_calm", "more_confident"
    """
    if adjustment == "more_urgent":
        mood_keywords.append("urgent")
    elif adjustment == "more_calm":
        mood_keywords.append("calm")
    elif adjustment == "more_confident":
        mood_keywords.append("confident")
    
    color_palette = generate_color_palette(mood_keywords, "balanced")
    style_directions = generate_style_directions(mood_keywords)
    
    return {
        "mood_keywords": mood_keywords,
        "color_palette": color_palette,
        "style_directions": style_directions
    }