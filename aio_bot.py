from aiogram import Bot, Dispatcher, executor
from aiogram import types
import datetime
import connect, config

token = '6596981303:AAEqYw5ga-iEWZZlkKpo7lS58RpSLKF_9WU'
arr = [[datetime.time(5, 0), datetime.time(5, 15)], [datetime.time(5, 15), datetime.time(5, 30)], [datetime.time(5, 30), datetime.time(5, 45)], [datetime.time(5, 45), datetime.time(6, 0)], [datetime.time(6, 0), datetime.time(6, 15)], [datetime.time(6, 15), datetime.time(6, 30)], [datetime.time(6, 30), datetime.time(6, 45)], [datetime.time(6, 45), datetime.time(7, 0)], [datetime.time(7, 0), datetime.time(7, 15)], [datetime.time(7, 15), datetime.time(7, 30)], [datetime.time(7, 30), datetime.time(7, 45)], [datetime.time(7, 45), datetime.time(8, 0)], [datetime.time(8, 0), datetime.time(8, 15)], [datetime.time(8, 15), datetime.time(8, 30)], [datetime.time(8, 30), datetime.time(8, 45)], [datetime.time(8, 45), datetime.time(9, 0)], [datetime.time(9, 0), datetime.time(9, 15)], [datetime.time(9, 15), datetime.time(9, 30)], [datetime.time(9, 30), datetime.time(9, 45)], [datetime.time(9, 45), datetime.time(10, 0)], [datetime.time(10, 0), datetime.time(10, 15)], [datetime.time(10, 15), datetime.time(10, 30)], [datetime.time(10, 30), datetime.time(10, 45)], [datetime.time(10, 45), datetime.time(11, 0)], [datetime.time(11, 0), datetime.time(11, 15)], [datetime.time(11, 15), datetime.time(11, 30)], [datetime.time(11, 30), datetime.time(11, 45)], [datetime.time(11, 45), datetime.time(12, 0)], [datetime.time(12, 0), datetime.time(12, 15)], [datetime.time(12, 15), datetime.time(12, 30)], [datetime.time(12, 30), datetime.time(12, 45)], [datetime.time(12, 45), datetime.time(13, 0)], [datetime.time(13, 0), datetime.time(13, 15)], [datetime.time(13, 15), datetime.time(13, 30)], [datetime.time(13, 30), datetime.time(13, 45)], [datetime.time(13, 45), datetime.time(14, 0)], [datetime.time(14, 0), datetime.time(14, 15)], [datetime.time(14, 15), datetime.time(14, 30)], [datetime.time(14, 30), datetime.time(14, 45)], [datetime.time(14, 45), datetime.time(15, 0)], [datetime.time(15, 0), datetime.time(15, 15)], [datetime.time(15, 15), datetime.time(15, 30)], [datetime.time(15, 30), datetime.time(15, 45)], [datetime.time(15, 45), datetime.time(16, 0)], [datetime.time(16, 0), datetime.time(16, 15)], [datetime.time(16, 15), datetime.time(16, 30)], [datetime.time(16, 30), datetime.time(16, 45)], [datetime.time(16, 45), datetime.time(17, 0)], [datetime.time(17, 0), datetime.time(17, 15)], [datetime.time(17, 15), datetime.time(17, 30)], [datetime.time(17, 30), datetime.time(17, 45)], [datetime.time(17, 45), datetime.time(18, 0)], [datetime.time(18, 0), datetime.time(18, 15)], [datetime.time(18, 15), datetime.time(18, 30)], [datetime.time(18, 30), datetime.time(18, 45)], [datetime.time(18, 45), datetime.time(19, 0)], [datetime.time(19, 0), datetime.time(19, 15)], [datetime.time(19, 15), datetime.time(19, 30)], [datetime.time(19, 30), datetime.time(19, 45)], [datetime.time(19, 45), datetime.time(20, 0)], [datetime.time(20, 0), datetime.time(20, 15)], [datetime.time(20, 15), datetime.time(20, 30)], [datetime.time(20, 30), datetime.time(20, 45)], [datetime.time(20, 45), datetime.time(21, 0)], [datetime.time(21, 0), datetime.time(21, 15)], [datetime.time(21, 15), datetime.time(21, 30)], [datetime.time(21, 30), datetime.time(21, 45)], [datetime.time(21, 45), datetime.time(22, 0)], [datetime.time(22, 0), datetime.time(22, 15)], [datetime.time(22, 15), datetime.time(22, 30)], [datetime.time(22, 30), datetime.time(22, 45)], [datetime.time(22, 45), datetime.time(23, 0)], [datetime.time(23, 0), datetime.time(23, 15)], [datetime.time(23, 15), datetime.time(23, 30)], [datetime.time(23, 30), datetime.time(23, 45)], [datetime.time(23, 45), datetime.time(0, 0)], [datetime.time(0, 0), datetime.time(0, 15)], [datetime.time(0, 15), datetime.time(0, 30)], [datetime.time(0, 30), datetime.time(0, 45)], [datetime.time(0, 45), datetime.time(1, 0)], [datetime.time(1, 0), datetime.time(1, 15)], [datetime.time(1, 15), datetime.time(1, 30)], [datetime.time(1, 30), datetime.time(1, 45)], [datetime.time(1, 45), datetime.time(2, 0)], [datetime.time(2, 0), datetime.time(2, 15)], [datetime.time(2, 15), datetime.time(2, 30)], [datetime.time(2, 30), datetime.time(2, 45)], [datetime.time(2, 45), datetime.time(3, 0)], [datetime.time(3, 0), datetime.time(3, 15)], [datetime.time(3, 15), datetime.time(3, 30)], [datetime.time(3, 30), datetime.time(3, 45)], [datetime.time(3, 45), datetime.time(4, 0)], [datetime.time(4, 0), datetime.time(4, 15)], [datetime.time(4, 15), datetime.time(4, 30)], [datetime.time(4, 30), datetime.time(4, 45)]]
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
async def func(message: types.Message):
    text = message.text
    message_time = message.date.time()
    if check_int(text):
        if 3 < int(text) < 20 and int(text) != 13:
            for i in arr:
                if i[0] < message_time <= i[1]:
                    left_interval, right_interval, time_in_str = i[0].strftime('%H:%M'), i[1].strftime('%H:%M'), message_time.strftime('%H:%M')
                    check = connect.checking(left_interval, right_interval)
                    if check != '0':
                        print(1)
                        connect.update_table_numbers(text, config.date, check)
                    else:
                        print(2)
                        connect.put_table_numbers(config.date, text, time_in_str)
                        connect.update_checking(left_interval, right_interval, time_in_str)
                        id_interval = connect.get_id_interval(left_interval, right_interval)
                        id_number = connect.get_id_number(config.date, connect.checking(left_interval, right_interval))
                        connect.update_pivot(id_interval, id_number)
        else:
            await message.answer(f'Введите число заново')
    else:
        await message.answer('Введите число')




def check_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
