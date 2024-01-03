import os
import streamlit as st
import time
import json
import requests
from requests.structures import CaseInsensitiveDict

URL = os.getenv('QUESTION_URL')


def posting(url, data):
    data = json.dumps(data)

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data
    else:
        return 'Ошибка. Сервер не работает'


if __name__ == "__main__":
    st.header('Чат по внутренней документации', divider='blue')
    search_query = st.text_input("Введите ваш вопрос...", value="", key="вопрос")

    if search_query:
        with st.spinner(text=f"Ищу {search_query}"):
            answer = posting(URL, search_query)
            st.write("Ответ:", answer)

