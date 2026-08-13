def ai_writer(topic):
    responses = {
        "salom": "Assalomu alaykum! Sizga qanday yordam bera olaman?",
        "bugun havo": "Bugun havo ochiq, harorat 25 daraja.",
        "inglizcha salom": "Hello! How can I help you?",
        "macbook": "MacBook Apple kompaniyasining noutbukidir. O'zbekistonda iSpace va Alifshop'da sotiladi.",
    }
    for key in responses:
        if key in topic.lower():
            return responses[key]
    return "Kechirasiz, bu mavzu bo'yicha ma'lumotim yo'q."

while True:
    savol = input("Savolingizni yozing (chiqish uchun 'exit'): ")
    if savol.lower() == "exit":
        break
    javob = ai_writer(savol)
    print("AI:", javob)