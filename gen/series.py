from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class StopDefinition:
    stop: datetime
    value: float
    noise: float = 0


@dataclass
class SeriesDefinition:
    id: str
    start: datetime
    value: float
    stops: list[StopDefinition]
    seed: int
    interval: timedelta = timedelta(hours=1)


series = [
    SeriesDefinition(
        id="stock",
        start=datetime.fromisoformat("2020-01-01"),
        value=100,
        seed=42,
        stops=[
            StopDefinition(
                stop=datetime.fromisoformat("2021-01-30"),
                value=100,
                noise=10
            ),
            StopDefinition(
                stop=datetime.fromisoformat("2021-02-07"),
                value=10,
                noise=10
            ),
            StopDefinition(
                stop=datetime.fromisoformat("2021-02-26"),
                value=3,
                noise=3
            ),
            StopDefinition(
                stop=datetime.fromisoformat("2021-03-16"),
                value=60,
                noise=2
            ),
            StopDefinition(
                stop=datetime.fromisoformat("2021-12-31"),
                value=100,
                noise=10
            )
        ]
    )
]
