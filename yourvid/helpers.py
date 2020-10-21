import random


def generate_random_string(num_elements):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_="
    selected_characters = random.choices(alphabet, k=num_elements)
    return "".join(selected_characters)


def random_video_id():
    return generate_random_string(14)


def video_upload_path(instance, filename):
    suffix = filename.split(".")[-1]
    return f"videos/{instance.video_id}.{suffix}"


def thumbnail_upload_path(instance, filename):
    suffix = filename.split(".")[-1]
    return f"img/thumbs/{instance.video_id}.{suffix}"

