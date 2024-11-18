import requests
import json

def emotion_detector(text_to_analyze):
     # URL del servicio detector de emociones
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Construyendo la carga útil de la solicitud en el formato esperado
    myobj = { "raw_document": { "text": text_to_analyze } }  # Crear un diccionario con el texto a analizar
    
    # Encabezado personalizado que especifica el ID del modelo para el servicio de detector de emociones
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Establecer los encabezados requeridos para la solicitud API
    
    # Enviando una solicitud POST a la API de detención de emociones
    response = requests.post(url, json = myobj, headers=header)  # Enviar una solicitud POST a la API con el texto y los encabezados
    
    # Analizando la respuesta JSON de la API
    formatted_response = json.loads(response.text)

    # Si el código de estado de la respuesta es 200, extrae el label y el score de la respuesta
    if response.status_code == 200:

        # Extrayendo la etiqueta de sentimiento y la puntuación de la respuesta
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness'] 
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        name_dominant_emotion = max(emotions, key=emotions.get)
    
    # Si el código de estado de la respuesta es 500, establece label y score como None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        name_dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': name_dominant_emotion
    }  # Devolver el texto de respuesta de la API
