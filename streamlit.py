import streamlit as st
import time
import json
import requests
from requests.structures import CaseInsensitiveDict


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
    st.header('Чат-бот по внутренней документации', divider='blue')
    search_query = st.text_input("Введите ваш вопрос...", value="", key="вопрос")

    if search_query:
        with st.spinner(text=f"Ищу {search_query}"):
            url = 'http://20.68.151.129:5000/user_question'
            answer = posting(url, search_query)
            st.write("Ответ:", answer)