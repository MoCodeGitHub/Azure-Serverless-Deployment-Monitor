import azure.functions as func
import datetime
import json
import logging
import requests

app = func.FunctionApp()

@app.timer_trigger(
    schedule="0 */5 * * * *",
    arg_name="myTimer",
    run_on_startup=False
)

def url_monitor(myTimer: func.TimerRequest) -> None:

    utc_timestamp = datetime.datetime.utcnow().isoformat()

    logging.info("URL Monitor started at %s", utc_timestamp)

    try:
        with open("urls.json", "r") as file:
            urls = json.load(file)

        for url in urls:

            try:
                response = requests.get(url, timeout=10)

                status = (
                    "UP"
                    if response.status_code < 400
                    else "DOWN"
                )

                logging.info(
                    "URL: %s | Status: %s | Code: %s | Time: %s",
                    url,
                    status,
                    response.status_code,
                    utc_timestamp
                )

            except requests.RequestException as error:

                logging.error(
                    "URL: %s | Status: DOWN | Error: %s | Time: %s",
                    url,
                    str(error),
                    utc_timestamp
                )

    except Exception as error:

        logging.error(
            "Monitor failed: %s",
            str(error)
        )