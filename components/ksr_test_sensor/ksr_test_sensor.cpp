#include "ksr_test_sensor.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ksr_test_sensor {

static const char *TAG = "ksr_test_sensor";

void KsrTestSensor::setup() {
  ESP_LOGI(TAG, "Uruchamiam KSR Test Sensor");
}

void KsrTestSensor::loop() {
  this->publish_state(11);
}

}  // namespace ksr_test_sensor
}  // namespace esphome
