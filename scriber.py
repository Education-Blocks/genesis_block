import json
import os
import time
import random
from datetime import datetime
from algosdk import account, mnemonic, encoding
from algosdk.v2client import algod
from algosdk import transaction, constants

from w1thermsensor import W1ThermSensor


sensor = W1ThermSensor()



def generate_new_account():
    private_key, address = account.generate_account()
    return {
        'address': address,
        'private_key': private_key,
        'mnemonic': mnemonic.from_private_key(private_key)
    }


def write_measurements(account, payload, algod_client):
    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE
    note = json.dumps(payload).encode()

    txn = transaction.PaymentTxn(
        sender=account['address'],
        sp=params,
        receiver=account['address'],  # Sending to self
        amt=0,
        note=note
    )

    signed_txn = txn.sign(account['private_key'])
    txid = algod_client.send_transaction(signed_txn)
    print("Transaction ID: {}".format(txid))
    transaction.wait_for_confirmation(algod_client, txid)
    print("Transaction confirmed.")


def get_payload():
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    return {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "location": {
            "school_name": "Joane Elementary",
            "room": "Classroom A2",
            "coordinates": {"latitude": 41.437761, "longitude": -8.414574}
        },
        "status": {
            "power_mode": "Plugged",   # Battery | Plugged
            "battery_level": 100,      # Battery level in %
            "last_calibration": "2023-10-01",
            "sensor_health": "good"
        },
        "sensors": {
            "environment": {
                "temperature" : temperature,   # temperature in ºC
                "humidity": 60,        # humidity in %
                "pressure":  1015      # atmospheric pressure in milibars
            },
            "particles": {
                "pm1": 12,             # Particulate Matter between 0.3-1 in µg/m³
                "pm2_5": 12,           # Particulate Matter between 1-2.5 in µg/m³
                "pm10": 20,            # Particulate Matter between 2.5-10 in µg/m³
            },
            "co2": {
                "co2": 400,            # Carbon Dioxide in ppm
            },
            "noise": {
                "mean_level": 35,      # Average noise level in dB
                "peak_level": 88       # Peak noise level in dB
            }
        }
    }


def main():
    # Connect to the Algorand node
    algod_token = os.getenv("ALGOD_TOKEN")
    algod_address = os.getenv("ALGOD_ADDR")
    headers = {"X-API-Key": algod_token}
    algod_client = algod.AlgodClient(algod_token, algod_address, headers)

    scriber_account = {
        'address': os.getenv("SCRIBER_ADDRESS"),
        'private_key': os.getenv("SCRIBER_PRIVATE_KEY"),
        'mnemonic': os.getenv("SCRIBER_MNEMONIC")
    }


    # Schedule to write measurements every 10 minutes
    while True:
        sensor_data = get_payload()
        write_measurements(scriber_account, sensor_data, algod_client)
        time.sleep(600)  # Wait for 10 minutes

if __name__ == "__main__":
    main()


