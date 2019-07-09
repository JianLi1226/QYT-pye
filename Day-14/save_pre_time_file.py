from datetime import datetime, timedelta


now = datetime.now()
five_days_before = (now - timedelta(days= 5))
formatted_5d_before = five_days_before.strftime("%Y-%m-%d_%H-%M-%S")
filename = f'save_fivedaysago_time_{formatted_5d_before}'

if __name__ == '__main__':
    with open(f'{filename}.txt', 'w') as f:
        f.write(str(five_days_before))

