# Embodied AI & Physical Control Sandbox
### 具身智能與物理控制實驗室

This repository serves as a personal research and implementation log for **Embodied AI** and **Physical AI**. It focuses on bridging the gap between high-level task planning and low-level motion control for robotic systems.

本倉庫是關於**具身智能 (Embodied AI)** 與**物理 AI (Physical AI)** 的個人研究與實作記錄，核心目標在於串聯機器人系統的高層級任務規劃與底層運動控制。

---

## 🚀 Current Implementation / 當前進度

The current project, implemented in `embodied_ai.ipynb`, establishes a foundational framework for robotic manipulation and feedback control.

目前在 `embodied_ai.ipynb` 中，我建立了一個機器人操縱與反饋控制的基礎框架。

### 1. Robotic Action Primitives / 機器人動作原語
- **Abstraction Layer**: Defined a `RoboticArm` class to encapsulate hardware-level movements into high-level primitives.
- **Operations**: Supports `move_to_position`, `grab`, and `release`.
- **Task Planning**: Implemented `execute_task` to sequence primitives for complex multi-step missions.

- **抽象層**: 定義了 `RoboticArm` 類別，將硬件級運動封裝為高層原語。
- **操作模塊**: 支援 `move_to_position`（移動）、`grab`（抓取）與 `release`（釋放）。
- **任務規劃**: 實現了 `execute_task` 邏輯，能將複雜的多步任務分解為有序的動作序列。

### 2. Control Theory - Incremental PID / 控制理論：增量式 PID
- **Feedback Loop**: Implemented an **Incremental PID Controller** to ensure precise execution and error correction in physical environments.
- **Safety Features**: Integrated output limiting (Anti-Saturation) to simulate real-world motor constraints.
- **Flexibility**: Supports dynamic parameter tuning for $K_p, K_i, K_d$.

- **反饋閉環**: 實現了**增量式 PID 控制器**，確保在物理環境中的精確執行與誤差修正。
- **安全特性**: 集成了輸出限幅（抗飽和）功能，模擬真實電機的物理限制。
- **靈活性**: 支援 $K_p, K_i, K_d$ 參數的動態調整與狀態重置。

---

## 🛠 Future Roadmap / 未來改進方向

To evolve this project into a robust Physical AI system, I have planned the following upgrades:

為了將此項目演進為完整的物理 AI 系統，我計劃進行以下升級：

* **Modern Control Algorithms / 現代控制算法**:
    * Transition from classic PID to **Model Predictive Control (MPC)** and **MPPI** for handling multi-constraint trajectory optimization.
    * 從傳統 PID 轉向**模型預測控制 (MPC)** 與 **MPPI**，以處理多約束下的軌跡優化。
* **System Integration / 系統集成**:
    * Migrate logic to **ROS 2 (Robot Operating System)** nodes for distributed real-time communication.
    * 將邏輯遷移至 **ROS 2** 節點，實現分佈式實時通訊。
* **Perception & Cognition / 感知與認知**:
    * Integrate vision-based feedback using Camera/LiDAR data for closed-loop visual servoing.
    * 集成基於相機/激光雷達的視覺反饋，實現閉環視覺伺服。
* **Embodied Intelligence / 具身化決策**:
    * Explore **LLM-based Task Planning** to convert natural language instructions into actionable robotic primitive sequences.
    * 探索基於**大語言模型 (LLM)** 的任務規劃，將自然語言指令轉化為可執行的動作序列。

---

## 📚 Disclaimer / 聲明
This project is for educational and research purposes. Code snippets derived from external literature have been manually re-implemented and optimized by me for learning.

本項目僅用於教育與研究目的。參考自外部文獻的代碼片段均經由本人手動實現並針對學習需求進行了優化。
