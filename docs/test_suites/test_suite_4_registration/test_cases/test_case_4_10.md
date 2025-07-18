## Тест-кейс 4.10 Проверка прикрепления файла в поле загрузки файла Your Profile Picture

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
1. В поле загрузки файла Your Profile Picture нажать "Выберите файл" и выбрать файл "src/attachments/profile_picture.png"
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











