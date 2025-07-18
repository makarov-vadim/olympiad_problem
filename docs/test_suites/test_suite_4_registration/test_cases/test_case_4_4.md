## Тест-кейс 4.4 Проверка ввода невалидного адреса электронной почты в поле E-mail

## Предусловия:
1. Открыт объект тестирования
https://way2automation.com/way2auto_jquery/registration.php#load_box
2. Все обязательные поля кроме поля E-mail заполнены валидными данными:
 - поле First Name (first_name_value);
 - чекбокс Hobby (hobby_value)
 - поле Phone Number (phone_number_value);
 - поле Username (username_value);
 - поля Password и Confirm Password (password_value).

## Шаги:
1. В поле E-mail ввести случайный адрес электронной почты, исключив символа "@" и доменную часть.
2. Нажать на кнопку "SUBMIT"

## Ожидаемый результат:
Запрос на обработку формы (POST запрос https://way2automation.com/way2auto_jquery/registration.php) не был отправлен.  
Вокруг некорректно заполненного поля E-mail появляется рамка красного цвета и текст "Please enter a valid email address.".  
Класс поля E-mail в DevTools объявляется "error_p".
