from fastapi import Request
import time
import psutil
import os

process = psutil.Process(os.getpid())

METRICS = {
    "request_count": 0,
    "total_response_time": 0.0,
    "average_response_time_ms": 0.0
}

async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000  # ms

    METRICS["request_count"] += 1
    METRICS["total_response_time"] += duration
    METRICS["average_response_time_ms"] = (
        METRICS["total_response_time"] / METRICS["request_count"]
    )

    return response

def get_system_metrics():

    memory_mb = round(process.memory_info().rss / 1024 / 1024, 2)
    return {
        "memory": memory_mb,
        "threads": process.num_threads(),
        "time":METRICS["average_response_time_ms"]
    }