import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

my_sensor_ns = cg.esphome_ns.namespace("my_sensor")

MySensor = my_sensor_ns.class_(
    "MySensor",
    cg.PollingComponent,
)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MySensor),
}).extend(
    cv.polling_component_schema("10s")
).extend(
    sensor.sensor_schema()
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
