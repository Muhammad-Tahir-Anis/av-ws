from typing import List


class EgoVehicleWheel:
    def __init__(self, wheel) -> object:
        self.tire_friction: float = wheel.tire_friction
        self.damping_rate: float = wheel.damping_rate
        self.max_steer_angle: float = wheel.max_steer_angle
        self.radius: float = wheel.radius
        self.max_brake_torque: float = wheel.max_brake_torque
        self.max_handbrake_torque: float = wheel.max_handbrake_torque
        self.position_x: float = wheel.position.x
        self.position_y: float = wheel.position.x
        self.position_z: float = wheel.position.x


class EgoVehicle:
    def __init__(self, data) -> object:
        self.wheels: List[EgoVehicleWheel] = []
        self.id: int = data.id
        self.type: str = data.type
        self.role_name: str = data.rolename
        for wheel in data.wheels:
            ego_wheel = EgoVehicleWheel(wheel)
            self.wheels.append(ego_wheel)
        self.max_rpm: float = data.max_rpm
        self.moi: float = data.moi
        self.damping_rate_full_throttle: float = data.damping_rate_full_throttle
        self.damping_rate_zero_throttle_clutch_engaged: float = data.damping_rate_zero_throttle_clutch_engaged
        self.damping_rate_zero_throttle_clutch_disengaged: float = data.damping_rate_zero_throttle_clutch_disengaged
        self.use_gear_autobox: float = data.use_gear_autobox
        self.gear_switch_time: float = data.gear_switch_time
        self.clutch_strength: float = data.clutch_strength
        self.mass: float = data.mass
        self.drag_coefficient = data.drag_coefficient
        self.center_of_mass_x: float = data.center_of_mass.x
        self.center_of_mass_y: float = data.center_of_mass.y
        self.center_of_mass_z: float = data.center_of_mass.z
