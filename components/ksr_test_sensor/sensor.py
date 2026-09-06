import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

ksr_test_sensor_ns = cg.esphome_ns.namespace("ksr_test_sensor")

KsrTestSensor = ksr_test_sensor_ns.class_(
    "KsrTestSensor",
    cg.PollingComponent,
    sensor.Sensor,
)

CONFIG_SCHEMA = (
    sensor.sensor_schema()
    .extend(
        {
            cv.GenerateID(): cv.declare_id(KsrTestSensor),
        }
    )
    .extend(
        cv.polling_component_schema("10s")
    )
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

