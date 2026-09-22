#include "ksr_test_sensor.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ksr_test_sensor {

static const char *TAG = "ksr_test_sensor";

void KsrTestSensor::update() {
  ESP_LOGI(TAG, "Wykonuję odczyt");

  this->publish_state(this->v);
}
void KsrTestSensor::setup() {
    this->v=24;
  ESP_LOGI(TAG, "Setup () wykonane");

}

}  // namespace ksr_test_sensor
}  // namespace esphome
