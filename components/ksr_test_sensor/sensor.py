import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

DEPENDENCIES = []

ksr_test_sensor_ns = cg.esphome_ns.namespace("ksr_test_sensor")

KsrTestSensor = ksr_test_sensor_ns.class_(
    "KsrTestSensor",
    cg.Component,
)

CONFIG_SCHEMA = sensor.sensor_schema(
    unit_of_measurement="",
    accuracy_decimals=0,
).extend(
    cv.Schema({
        cv.GenerateID(): cv.declare_id(KsrTestSensor),
    })
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
