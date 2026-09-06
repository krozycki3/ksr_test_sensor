#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace my_sensor {

class MySensor : public PollingComponent, public sensor::Sensor {
 public:
  void update() override;
};

}  // namespace my_sensor
}  // namespace esphome
