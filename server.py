''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_detector():
    """ emotion Detector  """
    # Recuperar el texto a detectar de los argumentos de la solicitud
    text_to_detector = request.args.get('textToAnalyze')
    # Pasar el texto a la función emotion_detector y almacenar la respuesta
    response = emotion_detector(text_to_detector)

    #Extraer la etiqueta y la puntuación de la respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Verifica si el label es None, indicando un error o entrada inválida
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo"
    #Devuelve una cadena formateada con la emociones y name_dominant_emotion
    return f"la respuesta del sistema es 'anger':{anger}, 'disgust':{disgust}," \
           f" 'fear':{fear}, 'joy': {joy}, 'sadness': {sadness}," \
           f" 'dominant_emotion': {dominant_emotion} " 

@app.route("/")
def render_index_page():
    ''' Render template index.html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
