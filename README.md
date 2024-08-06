[![jarvis-timeseries](https://img.shields.io/static/v1?label=&message=iflb&color=blue&logo=github)](https://github.com/daiyabarus/iflb "Go to GitHub repo")
[![Made with Python](https://img.shields.io/badge/Python->=3.12-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/ "Go to Microsoft homepage")
![maintained - yes](https://img.shields.io/badge/maintained-yes-blue)

# Mobile Network Carrier Configurations

This repository contains a Streamlit application for visualizing and understanding different mobile network carrier configurations using Plotly. The application provides detailed summaries and visualizations for three primary configurations: Equal Priority Carrier Configuration, Sticky Carrier Configuration, and Priority Carrier Configuration.

## Table of Contents

- [Overview](#overview)
- [Configurations](#configurations)
  - [Equal Priority Carrier Configuration](#equal-priority-carrier-configuration)
  - [Sticky Carrier Configuration](#sticky-carrier-configuration)
  - [Priority Carrier Configuration](#priority-carrier-configuration)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to provide a comprehensive understanding of different strategies for managing User Equipment (UE) behavior in mobile networks with multiple frequency carriers. The configurations discussed here are:

1. **Equal Priority Carrier Configuration**
2. **Sticky Carrier Configuration**
3. **Priority Carrier Configuration**

## Configurations

### Equal Priority Carrier Configuration

#### Key Takeaways:

1. In idle mode, UEs reselect between carriers based on relative signal strengths, applying hysteresis and offsets.
2. The configuration divides the signal strength plane into three regions (blue, green, and grey), determining UE camping behavior.
3. The `sNonIntraSearch` parameter controls the "stickiness" of UEs to the serving frequency, which can be useful when combined with load balancing.
4. This configuration works well for non-co-located cells but may not be ideal for pushing UEs towards a particular frequency in co-located cells.
5. Connected mode actions are governed by coverage-triggered events and Inter-Frequency Load Balancing (IFLB).
6. The alignment of various thresholds (e.g., `sNonIntraSearch`, `a5Threshold2Rsrp`) is crucial for ensuring that idle mode behavior and IFLB work harmoniously.

#### Conclusion:

The Equal Priority Configuration offers a flexible approach to managing UE distribution across multiple frequency carriers. It is most effective for non-co-located cells, allowing UEs to select the strongest frequency. Careful parameter tuning is essential to balance signal strength-based selection and load-based distribution.

### Sticky Carrier Configuration

#### Key Takeaways:

1. In this configuration, the serving frequency is given a higher priority than the neighboring frequency, regardless of which frequency the UE is currently on.
2. It's most useful when two carriers have similar coverage properties, allowing Inter-Frequency Load Balancing (IFLB) to distribute UEs in connected mode and maintain this distribution in idle mode.
3. The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `threshServingLow` and `threshXLow`.
4. Stickiness in the grey region is guaranteed by standards, as reselection only occurs when both thresholds are met.
5. This configuration is not suited for pushing UEs strongly towards a particular frequency or for use between two primary LTE coverage layers. It's best used between capacity layers with similar coverage and performance.
6. The configuration allows fine-tuning of both idle mode behavior and connected mode actions, including coverage-triggered handovers and IFLB.

#### Conclusion:

The Sticky Carrier Configuration balances UE distribution across multiple frequency carriers with similar coverage characteristics. It leverages IFLB for efficient load distribution in connected mode, leading to stable and predictable network behavior. This configuration is ideal when active pushing of UEs to a specific carrier is not required but maintaining a balanced load across carriers is desirable.

### Priority Carrier Configuration

#### Key Takeaways:

1. This configuration is typically used when carriers have vastly different coverage areas, such as low band vs. high band or macro cells vs. small cells.
2. One carrier is assigned a higher idle mode priority via the `cellReselectionPriority` parameter.
3. The configuration divides the signal strength plane into three regions (blue, green, and grey) based on key parameters: `threshXHigh`, `threshServingLow`, and `threshXLow`.
4. It provides better control over UE distribution compared to Equal Priority or Sticky Carrier Configurations, balancing between actively pushing UEs to the high-priority carrier and leaving room for Inter-Frequency Load Balancing (IFLB).
5. The configuration allows for fine-tuning of both idle mode behavior and connected mode actions, including coverage-triggered handovers and IFLB.
6. Careful parameter setting is crucial to ensure that idle mode behavior, coverage fallback, and IFLB work harmoniously.

#### Conclusion:

The Priority Carrier Configuration is effective in scenarios where one carrier needs prioritization to maximize its utilization while maintaining overall network efficiency and coverage. This configuration balances pushing UEs to a preferred carrier in idle mode and distributing traffic in connected mode. Careful planning and ongoing optimization are required to determine the optimal settings based on network characteristics.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/daiyabarus/iflb.git
    ```
2. Navigate to the project directory:
    ```bash
    cd iflb
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application, execute the following command in the project directory:
```bash
streamlit run main.py
