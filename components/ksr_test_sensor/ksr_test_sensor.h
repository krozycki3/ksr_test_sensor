#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace ksr_test_sensor {

class KsrTestSensor : public Component, public sensor::Sensor {
 public:
  void setup() override;
    // Ta funkcja wywoła się automatycznie zgodnie z update_interval z YAML
  void update() override {
        this->publish_state(11);
    };

}  // namespace ksr_test_sensor
}  // namespace esphome
