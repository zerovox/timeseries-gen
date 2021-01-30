from gen.series import series
from random import random, seed
from datetime import datetime


def apply_noise(target: float, previousValue: float, previousTarget: float, noise: float):
    if noise == 0:
        return target

    # previous effective noise applied
    previousOffset = min(abs(previousValue - previousTarget), noise)
    # between 0 and 1, how much should we weight the target, i.e regress to the target
    regressionCoefficient = (previousOffset / noise)

    # add some noise, -noise to noise
    nextNoise = noise * ((random() * 2) - 1)
    targetPlusNoise = target + nextNoise

    return (regressionCoefficient * target) + ((1 - regressionCoefficient) * targetPlusNoise)


def linear_interpolate(a: float, b: float, start: int, end: int, now: int):
    d = (now - start) / (end - start)
    return (a * (1 - d)) + (b * d)


for serie in series:
    seed(serie.seed)

    prevTime = serie.start.timestamp()
    prevValue = serie.value
    prevTarget = serie.value

    stopStartValue = serie.value
    stopStartTime = serie.start.timestamp()

    for stop in serie.stops:
        stopEndTime = stop.stop.timestamp()

        while prevTime < stopEndTime:
            print(serie.id, datetime.fromtimestamp(prevTime), prevValue)

            prevTime = prevTime + serie.interval.total_seconds()
            target = linear_interpolate(stopStartValue, stop.value, stopStartTime, stopEndTime, prevTime)
            prevValue = apply_noise(target, prevValue, prevTarget, stop.noise)
            prevTarget = target

        stopStartValue = stop.value
        stopStartTime = stop.stop.timestamp()

    print(serie.id, datetime.fromtimestamp(prevTime), prevValue)
