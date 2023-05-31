## Usage

install dependencies

```pip install -r requirements.txt```

run script

```python main.py -email <email> -app_password <app_password> -csv <csv_path>```

## Required parameters

`email` - e-mail address from which to send messages
`app_password` - [gmail app password](https://support.google.com/accounts/answer/185833?hl=en)
`csv` - path to the csv file.

## CSV data example

You need to fill in 3 columns: email, subject, and text.
See the example below

```
email,subject,text
python_hater428@gmail.com,Test Subject1,Test text1
cpp_enjoyer_1975@gmail.com,Test Subject2,Test text2
python_fan_2005@gmail.com,Test Subject3,Test text3
```

