# Education Blocks: Air Quality Monitoring Script

## Introduction
This script is specifically designed for monitoring and recording air quality in educational environments, leveraging the Algorand blockchain for secure and transparent data management. The core functionality involves encoding sensor data within transaction notes, ensuring immutable and transparent record-keeping.

Explore a demo of the monitoring data [on algorand testnet here](https://testnet.algoexplorer.io/address/EOM6ICZ6MC7N26SHCELKAJPJPCDP3OC6L2L7JWCH5DTLCASXXVZJT47UKI) the JSON payload is encoded on the notes fields of each transaction.

## Installation and Configuration

### Prerequisites
- Python 3.6 or higher
- Python package manager (pip)

### Environment Setup
1. **Algorand Python SDK**:
   - Install the SDK using: `pip install py-algorand-sdk`.

2. **Environment Variables**:
   - The script depends on these environment variables:
     - `ALGOD_TOKEN`: Your Algorand node API token.
     - `ALGOD_ADDR`: Your Algorand node address.
     - `SCRIBER_ADDRESS`: Algorand account address for transactions.
     - `SCRIBER_PRIVATE_KEY`: Private key of the SCRIBER_ADDRESS.
     - `SCRIBER_MNEMONIC`: Mnemonic phrase for the SCRIBER_ADDRESS.
   - Set these variables in your environment or use a `.env` file with a package like `python-dotenv` for loading them.

### Using Algorand TestNet
For development and testing:
1. Obtain `ALGOD_TOKEN` and `ALGOD_ADDR` from the Algorand TestNet website or your TestNet node.
2. Update the environment variables to point to the TestNet node.
3. Fund your `SCRIBER_ADDRESS` with TestNet Algos for transaction fees using a TestNet faucet.
4. Switch back to MainNet configuration for production deployment.

## Payload Description
The script generates a payload with the following structure:
- `timestamp`: UTC timestamp of the data recording.
- `location`: Information about the school's location including name, specific room, and coordinates.
- `status`: Details on the device's power mode, battery level, last calibration date, and sensor health.
- `sensors`: Data from various environmental sensors (currently, only temperature is actively tracked). Other attributes like humidity, pressure, particulate matter (PM1, PM2.5, PM10), CO2 levels, and noise levels are placeholders for future sensor integrations.

### Current Sensor Data
- **Temperature**: Measured in Celsius (ºC).

### Sample Data (To be integrated)
- **Environment**: Humidity (%), Pressure (milibars).
- **Particles**: PM1, PM2.5, PM10 measurements in µg/m³.
- **CO2**: Carbon Dioxide levels in ppm.
- **Noise**: Mean and peak noise levels in dB.

## Usage
Run the script to start monitoring and recording air quality data. The script is set to record data every 10 minutes.

