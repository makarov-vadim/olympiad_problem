## Тест-кейс 4.1 Проверка незаполнения обязательных полей

## Предусловия:
Открыт объект тестирования
https://way2automation.com/way2auto_jquery/registration.php#load_box

## Шаги:
1. Заполнить форму согласно таблице "Заполнение формы" (заполнять обязательные поля, пропуская один элемент)
2. Нажать на кнопку "SUBMIT"

## Ожидаемый результат:
Запрос на обработку формы (POST запрос https://way2automation.com/way2auto_jquery/registration.php) не был отправлен.  
Вокруг незаполненного/невыбранного элемента появляется рамка красного цвета и текст "This field is required.".  
Класс элемента в DevTools объявляется "error_p".

## Заполнение формы:
<table>
    <tr>
        <td><b>№</b></td>
        <td><b>First Name</b></td>
        <td><b>Hobby</b></td>
        <td><b>Phone Number</b></td>
        <td><b>Username</b></td>
        <td><b>E-mail</b></td>
        <td><b>Password</b></td>
        <td><b>Confirm Password</b></td>
    </tr>
    <tr>
        <td>1</td>
        <td>NONE</td>
        <td>hobby_value</td>
        <td>phone_number_value</td>
        <td>username_value</td>
        <td>email_value</td>
        <td>password_value</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>2</td>
        <td>first_name_value</td>
        <td>NONE</td>
        <td>phone_number_value</td>
        <td>username_value</td>
        <td>email_value</td>
        <td>password_value</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>3</td>
        <td>first_name_value</td>
        <td>hobby_value</td>
        <td>NONE</td>
        <td>username_value</td>
        <td>email_value</td>
        <td>password_value</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>4</td>
        <td>first_name_value</td>
        <td>hobby_value</td>
        <td>phone_number_value</td>
        <td>NONE</td>
        <td>email_value</td>
        <td>password_value</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>5</td>
        <td>first_name_value</td>
        <td>hobby_value</td>
        <td>phone_number_value</td>
        <td>username_value</td>
        <td>NONE</td>
        <td>password_value</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>6</td>
        <td>first_name_value</td>
        <td>hobby_value</td>
        <td>phone_number_value</td>
        <td>username_value</td>
        <td>email_value</td>
        <td>NONE</td>
        <td>password_value</td>
    </tr>
    <tr>
        <td>7</td>
        <td>first_name_value</td>
        <td>hobby_value</td>
        <td>phone_number_value</td>
        <td>username_value</td>
        <td>email_value</td>
        <td>password_value</td>
        <td>NONE</td>
    </tr>
</table>

где
 - first_name_value - случайное имя;
 - hobby_value - выбор случайного значения из чекбокса Hobby;
 - phone_number_value - случайный номер;
 - username_value - случайный username;
 - email_value - случайная электронная почта;
 - password_value - случайный пароль;
 - NONE - незаполнение/невыбор значения в элементе.
        