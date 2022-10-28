import os
import subprocess

zals = ['Красный',
        'Зелёный',
        'Бордовый',
        'Голубой',
        'Жёлтый',
        'Бежевый',
        'Лимонный',
        'Оранжевый',
        'Розовый',
        'Салатовый',
        'Серебряный',
        'Фиолетовый']


def rename_videos():
    for dir in os.listdir(f"video"):
        if dir == '.DS_Store':
            continue
        for file in os.listdir(f"video/{dir}/"):
            if file == '.DS_Store':
                continue

            os.rename(f"video/{dir}/{file}", f"video/{dir}/{file.replace(' ', '_')}")


def convert_videos():
    # for zal in zals:
    #     os.mkdir(f'converted/{zal}')

    for dir in os.listdir(f"video"):
        if dir == '.DS_Store':
            continue
        for file in os.listdir(f"video/{dir}/"):
            if file == '.DS_Store':
                continue

            input_file = file
            output_file = file + ".mp4"

            if output_file in os.listdir(f"converted/{dir}/"):
                continue
            ffmpeg_command = "ffmpeg -i video/%s/%s -c:v libx264 -b:v 4000k converted/%s/%s" % (
                dir, input_file, dir, output_file)
            print(subprocess.call(ffmpeg_command, shell=True))


# rename_videos()
convert_videos()
