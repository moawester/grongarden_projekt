import pandas as pd
from math import ceil
from tqdm.auto import tqdm
from transformers import pipeline

sentiment_pipe = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=-1)

def predict_sentiment_hf(texts, model=None, batch_size=16, sleep_time=0):
    """
    texts: list eller pandas Series med str
    return: pandas.DataFrame med columns ['text','sentiment','score']
    """
    s = pd.Series(texts).fillna("").astype(str).str.strip()
    results = []
    n = len(s)
    n_batches = ceil(n / batch_size)
    
    for i in tqdm(range(n_batches), desc="Local sentiment"):
        batch = s[i*batch_size:(i+1)*batch_size].tolist()
        res = sentiment_pipe(batch)
        for r in res:
            lab = r.get("label", "").lower()
            score = float(r.get("score", 0.0))
            norm = "positive" if "positive" in lab else ("negative" if "negative" in lab else "neutral")
            results.append({"sentiment": norm, "score": score})
    
    out = pd.DataFrame(results)
    out.insert(0, "text", s.tolist())
    return out

def get_embeddings_hf(texts, model=None, batch_size=16, sleep_time=0):
    """Mock - returnerar tom lista för nu"""
    return [None] * len(texts)