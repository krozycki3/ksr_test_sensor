#include "my_sensor.h"
#include "esphome/core/log.h"

namespace esphome {
namespace my_sensor {

static const char *TAG = "my_sensor";

void MySensor::update() {
  ESP_LOGI(TAG, "Odczytuję wartość...");

  this->publish_state(11);
}

}  // namespace my_sensor
}  // namespace esphome
