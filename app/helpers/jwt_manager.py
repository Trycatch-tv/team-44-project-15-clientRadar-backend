import datetime
from jwt import encode, decode
from decouple import config

jwt_seed = config("JWT_SEED")


def create_token(data: dict):
    exp = datetime.datetime.now(
        tz=datetime.timezone.utc) + datetime.timedelta(hours=24)
    token: str = encode(payload={**data, "exp": exp},
                        key=jwt_seed, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, "my_secret_key", algorithms=["HS256"])
    return data
