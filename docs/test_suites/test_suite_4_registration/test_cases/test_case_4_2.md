## Тест-кейс 4.2 Проверка заполнения обязательных полей валидными данными

## Предусловия:
Открыт объект тестирования
https://way2automation.com/way2auto_jquery/registration.php#load_box

## Шаги:
1. В поле First Name ввести случайное имя (first_name_value)
2. Выбрать случайное значения из чекбокса Hobby
3. В поле Phone Number ввести случайный номер (phone_number_value)
4. В поле Username ввести случайный username (username_value)
5. В поле E-mail ввести случайную электронную почту (email_value)
6. В поля Password и Confirm Password ввести одинаковый случайный пароль (password_value)
7. Нажать на кнопку "SUBMIT"

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
