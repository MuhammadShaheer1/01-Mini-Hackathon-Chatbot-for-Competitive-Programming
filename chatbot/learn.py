from django.http import JsonResponse

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')

        # Assuming you have logic to determine the chatbot's response
        chatbot_response = {
            "1. Factual Statements": {
                "definition": "Statements that describe facts that are verifiable and objective.",
                "examples": [
                    "Water boils at 100°C (212°F) at sea level.",
                    "The Great Wall of China is over 13,000 miles long."
                ]
            },
            "2. Philosophical Statements": {
                "definition": "Statements that explore fundamental questions about existence, knowledge, and values.",
                "examples": [
                    "The only constant in life is change.",
                    "Knowledge is power."
                ]
            },
            # Add more categories as needed...
        }

        # Format the response into a structured HTML string
        formatted_response = ""
        for category, content in chatbot_response.items():
            formatted_response += f"<strong>{category}</strong><br>"
            formatted_response += f"<strong>Definition:</strong> {content['definition']}<br>"
            formatted_response += "<ul>"
            for example in content["examples"]:
                formatted_response += f"<li>{example}</li>"
            formatted_response += "</ul><br>"

        return JsonResponse({'response': formatted_response})
