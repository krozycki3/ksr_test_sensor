import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

DEPENDENCIES = []

ksr_test_sensor_ns = cg.esphome_ns.namespace("ksr_test_sensor")

KsrTestSensor = ksr_test_sensor_ns.class_(
    "KsrTestSensor",
    cg.Component,
    sensor.Sensor,
)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(KsrTestSensor),
}).extend(sensor.sensor_schema())

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
