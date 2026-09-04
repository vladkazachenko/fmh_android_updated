# Дипломный проект «Мобильный хоспис»

## Описание проекта

В рамках дипломного проекта выполнено тестирование Android-приложения «Мобильный хоспис».

Приложение содержит:

* авторизацию пользователя;
* главный экран со списком новостей;
* раздел News;
* сортировку и фильтрацию новостей;
* Control Panel для создания, редактирования и удаления новостей;
* раздел Our Mission / Love is all с тематическими цитатами;
* сохранение пользовательской сессии и выход из учётной записи.

Автоматизация выполнена на Python с использованием Appium, pytest, Page Object Model и Allure.

## Тестовое окружение

Автотесты разработаны и проверены в следующем окружении:

* Windows 10;
* Android API 36;
* Android Emulator;
* Python 3.14;
* pytest 9.1.1;
* Appium 3.3.0;
* Appium-Python-Client 6.0.0;
* UiAutomator2 Driver 7.1.2;
* allure-pytest 2.16.0;
* Allure Commandline 2.43.0.

Тестируемое приложение:

* package: `ru.edu.qamid`
* activity: `ru.edu.qamid.ui.AppActivity`

Данные для авторизации:

* Login: `login2`
* Password: `password2`

## Структура автотестов

Автотесты расположены в директории:

```text
tests/
```

Page Object-классы расположены в:

```text
tests/pages/
```

Основные тестовые файлы:

```text
tests/test_login.py
tests/test_main.py
tests/test_news.py
tests/test_news_delete.py
tests/test_news_filter.py
tests/test_news_navigation.py
tests/test_news_validation.py
tests/test_our_mission.py
tests/test_session.py
```

Всего автоматизировано 26 тест-кейсов.

## Предварительные требования

Перед запуском необходимо установить:

* Python;
* Node.js и npm;
* Java;
* Android Studio;
* Android SDK;
* Appium;
* UiAutomator2 Driver;
* Allure Commandline.

Также должен быть запущен Android Emulator с Android API 36.

Проверить подключённый эмулятор можно командой:

```bash
adb devices
```

В списке устройств должен отображаться эмулятор, используемый для запуска тестов.

Например:

```text
emulator-5554    device
```

## Установка зависимостей Python

В корне проекта создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его в Git Bash:

```bash
source .venv/Scripts/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

В проекте используются:

```text
Appium-Python-Client==6.0.0
pytest==9.1.1
allure-pytest==2.16.0
```

## Установка Appium

Установить Appium:

```bash
npm install -g appium
```

Проверить версию:

```bash
appium --version
```

Установить драйвер UiAutomator2:

```bash
appium driver install uiautomator2
```

Проверить установленные драйверы:

```bash
appium driver list --installed
```

## Установка Allure Commandline

Установить Allure CLI:

```bash
npm install -g allure-commandline
```

Проверить установку:

```bash
allure --version
```

## Подготовка приложения

Приложение должно быть установлено на Android Emulator.

Package приложения:

```text
ru.edu.qamid
```

Основная Activity:

```text
ru.edu.qamid.ui.AppActivity
```

В `gradle.properties` добавлена настройка:

```text
android.injected.androidTest.leaveApksInstalledAfterRun=true
```

Она предотвращает удаление APK после запуска инструментальных Android-тестов.

## Запуск Appium

Перед запуском pytest необходимо запустить Appium Server в отдельном терминале:

```bash
appium
```

По умолчанию автотесты подключаются к Appium по адресу:

```text
http://127.0.0.1:4723
```

Терминал с Appium необходимо оставить запущенным на время выполнения тестов.

## Проверка количества тестов

Перед запуском можно проверить список собираемых pytest тестов:

```bash
pytest --collect-only -q
```

Ожидаемый результат:

```text
26 tests collected
```

## Запуск всех автотестов

Перед финальным запуском рекомендуется удалить результаты предыдущих прогонов Allure:

```bash
rm -rf allure-results
mkdir allure-results
```

Запустить все тесты:

```bash
pytest -v -s --alluredir=allure-results
```

## Запуск отдельного тестового файла

Например, тесты авторизации:

```bash
pytest tests/test_login.py -v -s --alluredir=allure-results
```

Тесты работы с новостями:

```bash
pytest tests/test_news.py -v -s --alluredir=allure-results
```

## Запуск отдельного теста

Пример:

```bash
pytest tests/test_news.py::test_create_news -v -s --alluredir=allure-results
```

## Формирование Allure-отчёта

После выполнения тестов сгенерировать HTML-отчёт:

```bash
allure generate allure-results -o allure-report --clean
```

Открыть отчёт:

```bash
allure open allure-report
```

Для остановки локального сервера Allure необходимо нажать:

```text
Ctrl + C
```

## Скриншоты при падении тестов

При падении автотеста автоматически создаётся снимок текущего экрана приложения.

Скриншот прикрепляется к соответствующему тесту в Allure в секции `Tear down`.

## Результат финального прогона

В финальном прогоне было выполнено 26 автотестов.

Результат:

```text
24 passed
2 failed
```

Неуспешными являются:

* `TC-002 Авторизация с неверным логином`;
* `TC-003 Авторизация с неверным паролем`.

В обоих случаях ожидается сообщение:

```text
Wrong login or password
```

Фактически приложение отображает:

```text
Something went wrong. Try again later.
```

Падения данных тестов связаны с обнаруженным дефектом приложения и не являются ошибками автотестов.

Дефект оформлен в разделе Issues репозитория.

## Архив результатов Allure

Для сдачи проекта результаты финального прогона упаковываются в:

```text
allure-results.zip
```

Архив содержит исходные данные Allure, включая результаты тестов и прикреплённые скриншоты неуспешных тестов.

## Документация проекта

В корне репозитория находятся:

* `Plan.md` — план тестирования и автоматизации;
* `Check.csv` — чек-лист;
* `Cases.csv` — тест-кейсы с отметками об автоматизации;
* `README.md` — инструкция по запуску автотестов;
* `Result.md` — результаты тестирования и сравнение времени ручной и автоматизированной проверки;
* `allure-results.zip` — результаты финального прогона для Allure.

Баг-репорты оформлены в GitHub Issues.
