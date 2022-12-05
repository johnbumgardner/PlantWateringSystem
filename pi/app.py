from hardware.water_sensor import WaterSensor
from flask import Flask, jsonify, make_response

app = Flask(__name__)
left_sensor = WaterSensor(7)
right_sensor = WaterSensor(0)

water_sensors = [left_sensor, right_sensor]

@app.route("/sample")
def sample():
    sampled_values = []
    for sensor in water_sensors: 
        sampled_values.append(sensor.sample())
    
    response = make_response(
                jsonify(
                    {"sensors": sampled_values}
                ),
                200,
            )
    response.headers["Content-Type"] = "application/json"
    return response

app.run(debug=False, host="0.0.0.0")

