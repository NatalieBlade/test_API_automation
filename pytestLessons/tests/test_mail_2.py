import pytest

def test_sending_message_3(set_up):
    print('Письмо отправлено')

def test_sending_message_4(set_up):
    print('Письмо отправлено')

# Запуск тестов
# pytest - просто список тестов с точками и процент выполнения
# pytest -v - файл, название теста, PASSED/FAILED и процент выполнения
# pytest -s - надписи и принты
# pytest -s -v - файл, название теста, надписи и принты, PASSED/FAILED
# pytest -s -v test_mail.py - запуск определенного теста
