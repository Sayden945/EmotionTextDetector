import requests, json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(URL, json = myobj, headers = header)
    formatted_resp = json.loads(resp.text)
    
    #If receives OK, format output
    if resp.status_code == 200:
        emotions = formatted_resp['emotionPredictions'][0]['emotion']         
        dom_emotion = max(emotions.items(), key=lambda x: x[1])
        emotions['dominant_emotion'] = dom_emotion[0]
    #Else if error status code, set scores to none
    elif resp.status_code == 400:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None,
            "dominant_emotion": None 
            }
        
    return emotions