"""
Embodied AI Control Framework
-----------------------------
A modular framework for robotic manipulation and feedback control.
Includes a RoboticArm primitive layer and an Incremental PID controller.

Refactored and optimized by: Yuanzhe (Nikola) Chen, UNSW MEng EE
"""


class RoboticArm:
    """
    Simulates a robotic arm with basic action primitives.
    模擬具有基本動作原語的機械臂。
    """

    def __init__(self):
        self.position = None  # Current cartesian position (x, y, z)
        self.gripper_open = True  # State of the end-effector

    def move_to_position(self, target_position: tuple) -> None:
        """
        Action Primitive: Move the arm to a specific coordinate.
        動作原語：移動到指定坐標。
        """
        print(f"[Arm] Moving to position: {target_position}")
        self.position = target_position

    def grab(self) -> None:
        """
        Action Primitive: Activate the gripper.
        動作原語：執行抓取。
        """
        if self.gripper_open:
            print("[Arm] Grabbing object...")
            self.gripper_open = False
        else:
            print("[Arm] Warning: Gripper is already closed.")

    def release(self) -> None:
        """
        Action Primitive: Release the gripper.
        動作原語：執行釋放。
        """
        if not self.gripper_open:
            print("[Arm] Releasing object...")
            self.gripper_open = True
        else:
            print("[Arm] Warning: Gripper is already open.")

    def execute_task(self, start_pos: tuple, end_pos: tuple) -> None:
        """
        Task Planning: Sequences primitives to perform a pick-and-place task.
        任務規劃：組合動作原語以執行抓取與放置任務。
        """
        print(f"\n--- Starting Task: Pick and Place ---")
        self.move_to_position(start_pos)
        self.grab()
        self.move_to_position(end_pos)
        self.release()
        print(f"--- Task Completed ---\n")


class IncrementalPID:
    """
    Incremental PID Controller Implementation.
    增量式 PID 控制器實現。

    Formula:
    u(k) = u(k-1) + Kp * [e(k) - e(k-1)] + Ki * e(k) + Kd * [e(k) - 2e(k-1) + e(k-2)]
    """

    def __init__(self, kp: float, ki: float, kd: float):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.target_value = 0.0
        self.pid_output = 0.0

        # Error terms for incremental calculation
        self.error_k_1 = 0.0  # Error at (k-1)
        self.error_k_2 = 0.0  # Error at (k-2)

        # Output limits (Anti-windup / Motor safety)
        self.limit_output = False
        self.output_min = 0.0
        self.output_max = 0.0

    def set_target(self, target: float) -> None:
        """Sets the desired target value."""
        self.target_value = target

    def set_output_limits(self, min_val: float, max_val: float) -> None:
        """Configures the saturation limits for the controller output."""
        if min_val == 0 and max_val == 0:
            self.limit_output = False
        else:
            self.limit_output = True
            self.output_min = min_val
            self.output_max = max_val

    def set_pid_params(self, kp: float, ki: float, kd: float) -> None:
        """Updates PID parameters dynamically and resets errors."""
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.reset()

    def reset(self) -> None:
        """Resets the controller state."""
        self.pid_output = 0.0
        self.error_k_1 = 0.0
        self.error_k_2 = 0.0

    def calculate(self, feedback_value: float) -> float:
        """
        Calculates the control output based on current feedback.
        根據當前反饋計算控制輸出。
        """
        error_k = self.target_value - feedback_value

        # Incremental PID formula
        # Delta P: Kp * (error - last_error)
        p_term = self.kp * (error_k - self.error_k_1)
        # Delta I: Ki * error
        i_term = self.ki * error_k
        # Delta D: Kd * (error - 2*last_error + prev_error)
        d_term = self.kd * (error_k - 2 * self.error_k_1 + self.error_k_2)

        delta_output = p_term + i_term + d_term

        # Update output
        self.pid_output += delta_output

        # Update error history
        self.error_k_2 = self.error_k_1
        self.error_k_1 = error_k

        # Apply Output Limiting (Safety Saturation)
        if self.limit_output:
            if self.pid_output > self.output_max:
                self.pid_output = self.output_max
            elif self.pid_output < self.output_min:
                self.pid_output = self.output_min

        return self.pid_output


# --- Main Execution Block (For Demo) ---
if __name__ == "__main__":
    # 1. Test Robotic Arm Logic
    arm = RoboticArm()
    arm.execute_task(start_pos=(10, 5, 0), end_pos=(20, 10, 5))

    # 2. Test PID Controller
    print("--- Starting PID Simulation ---")
    pid = IncrementalPID(kp=0.2, ki=0.01, kd=0.05)
    pid.set_target(100.0)
    pid.set_output_limits(-50, 50)

    current_val = 0.0
    for i in range(10):
        # Simulate a simple system process
        control_signal = pid.calculate(current_val)
        current_val += control_signal * 0.5  # System response
        print(f"Step {i + 1}: Target=100, Current={current_val:.2f}, Control Signal={control_signal:.2f}")