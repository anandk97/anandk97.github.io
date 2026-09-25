---
layout: default
title: "Research"
---

# Research

<p class="page-lede">Physics-informed machine learning and adaptive control for complex engineering systems, from nuclear reactors to aircraft manufacturing.</p>

## Idaho National Laboratory (October 2025 – Present)

### Surrogate Modeling for Prometheus (Collaboration with NVIDIA)

- **Objective:** Replace high-fidelity CFD and multiphysics reactor simulations with fast, accurate surrogates.
- **Approach:** Physics-informed surrogate models built with NVIDIA's PhysicsNeMo framework, plus an agentic interface for natural-language interaction with reactor simulation results.
- **Outcome:** 99% accuracy with 1–2 second inference, against 1–2 hours per high-fidelity sample. The work won 2nd place and the People's Choice award at the INL Research SLAM and was selected for a technical demonstration to the Chairman of the U.S. Nuclear Regulatory Commission.

### Robust Control for Nuclear Power Plants (LDRD 25P1094-008FP, Principal Investigator)

- **Objective:** Regulate reactor power under parameter uncertainty and limited state observability.
- **Outcome so far:** The algorithms track reference power trajectories across a range of operating conditions.

### IMPACT-AI Data Assimilation

- **Objective:** Enable real-time data assimilation from experimental data.
- **Approach:** A surrogate for a BISON fuel-performance model that runs 10,000× faster than the original.

### Autonomous Control for the Neutron Radiography (NRAD) TRIGA Reactor

- **Objective:** Autonomous load-following control using predictive modeling.

## Independent Projects

### Data-Driven Dynamics: Beating the Scientific ML Benchmark (2026)

- **Objective:** Beat the best published models in the Common Task Framework for scientific machine learning (NeurIPS 2025) on chaotic and physical systems.
- **Approach:** Identify the governing equation from data with a sparse fit through a differentiable solver. Then denoise with EKF/4D-Var data assimilation and forecast with the identified model.
- **Outcome:** Top of the leaderboard on Lorenz (78.85 vs 64.54), Kuramoto–Sivashinsky (83.41 vs 18.88) and, as an estimate, the molten salt reactor (79.33 vs 70.97).
- **[Interactive results →]({{ "/projects/" | relative_url }})** · [Code](https://github.com/anandk97/data-driven-dynamics)

### Which Neural Operator for Which Data? (2026)

- **Objective:** Compare five operator-learning families (DeepONet, Fourier neural operators, Kolmogorov–Arnold networks, transformers and physics-informed networks), each in its original form and a newer variant, and explain which properties of the data favour which architecture.
- **Approach:** Train all ten under one protocol on six standard PDE benchmarks (Burgers, advection, Darcy, Navier–Stokes, airfoil and elasticity). Then test data efficiency, input noise and resolution transfer, and set the results against published comparisons.
- **Outcome:** Fourier models win on regular grids and need far less data. DeepONet breaks on moving discontinuities, as theory predicts, but is the most robust to input noise. Transformers win on point clouds. The local-kernel FNO's failure at finer resolution was traced to its finite-difference branch amplifying grid-scale content, with a simple fix at inference time.
- **[Interactive results →]({{ "/projects/operators/" | relative_url }})** · [Code](https://github.com/anandk97/neural-operator-comparison)

## University of Washington (2019 – 2025)

### Adaptive Learning Framework for Digital Twins: Airplane Fuselage Shape Control (January 2024 – August 2025)

- **Objective:** Predict composite fuselage deflection under load to ensure precise alignment during assembly.
- **Approach:** Transfer learning, Gaussian process regression and Kalman filtering that combine high-fidelity measurements with finite element predictions to correct model–reality discrepancies from limited experimental data.
- **Outcome:** Uncertainty quantification and optimized sensor and actuator placement. Recognized with a Boeing Advanced Research Collaboration Research Excellence Award (2024); patent pending.

### Data-Driven Risk Assessment of Complex Hand-Intensive Manufacturing (June 2021 – August 2025)

- **Objective:** Detect ergonomic risk in real time for manufacturing technicians.
- **Approach:** A multimodal sensing testbed that captures synchronized upper-body and hand poses with hand forces (314 variables at 60 Hz), with computer-vision segmentation, gradient boosting classifiers and GRU time-series models.
- **Outcome:** Automated ergonomic scoring that generalizes well (> 95% accuracy) across 15+ technicians, and a new ergonomic score (BACH) for detailed injury risk assessment. Published in *Nature Communications Engineering*.

### Control of Vortex Dynamics using Invariants (June 2021 – September 2023)

- **Objective:** Use model predictive control to steer the evolution of vortices with "virtual cylinders".
- **Approach:** Visualizations and evaluations that compare controlled and uncontrolled flow dynamics.

### Control of Microswimmers in Turbulent Flow using Reinforcement Learning (from June 2020)

- **Objective:** Develop "smart" microswimmers that navigate turbulent flows efficiently toward designated targets.
- **Approach:** Deep reinforcement learning that minimizes energy use and travel time.
- **Outcome:** Up to 2× faster target acquisition and significant energy savings compared with naive strategies. Presented at the APS Division of Fluid Dynamics Annual Meeting (2021).
