from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS: list = env.list("ADMINS")  # Тут у нас будет список из админов
IP: str = env.str("ip")  # Тоже str, но для айпи адреса хоста

