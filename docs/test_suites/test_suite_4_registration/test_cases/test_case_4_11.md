## Тест-кейс 4.11 Проверка ввода текста в поле About Yourself

## Предусловия:
1. Открыт объект тестирования
https://way2automation.com/way2auto_jquery/registration.php#load_box
2. Все обязательные поля заполнены валидными данными:
 - поле First Name (first_name_value);
 - чекбокс Hobby (hobby_value)
 - поле Phone Number (phone_number_value);
 - поле Username (username_value);
 - поле E-mail(email_value);
 - поля Password и Confirm Password (password_value).

## Шаги:
1. В поле About Yourself ввести текст согласно таблице "Варианты"
2. Нажать на кнопку "SUBMIT"

## Ожидаемый результат:
Запрос на обработку формы (POST запрос https://way2automation.com/way2auto_jquery/registration.php) отправлен.  
Статус-код ответа на запрос 200 ОК.  
Payload ответа на запрос содержит следующие данные:
 - name = first_name_value;
 - hobby = "on";
 - phone = phone_number_value;
 - username = username_value;
 - email = email_value;
 - password = password_value;
 - c_password = password_value.


## Варианты:
| № | Вариант                                                                                                                                                      |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Вывести все возможные перестановки массива без повторяющихся элементов, массив [2025, 3,11]                                                                  |
| 2 | Найти длину самой длинной строго возрастающей подпоследовательности в массиве [1, 3, 6, 7, 9, 4, 10, 5, 6, 12, 2, 7, 11]                                     |
| 3 | Найти самую длинную подпоследовательность, которая встречается в двух строках в одинаковом порядке , но не обязательно подряд s1 = "aabbdsaacc" s2 = "abadc" |









