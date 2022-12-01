from aocd import get_data
from dotenv import load_dotenv
load_dotenv()


def data_loader(day=1, year=2022):
    return get_data(day=day, year=year)
