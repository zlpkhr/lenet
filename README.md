# LeNet-5 Fault Injection Testing

This project implements fault injection testing on a quantized LeNet-5 convolutional neural network using PyTorch. The network is trained on the MNIST dataset, quantized to 8-bit integers, and systematically tested by flipping individual bits in its parameters.

## Overview

The testing framework allows both random bit flips across all layers and targeted testing of specific layers and bit positions, measuring how these faults impact the model's classification accuracy. PyTorch was chosen for its ability to modify neural network parameters during runtime testing, as it directly exposes quantized weights through its API.

## Requirements

- Python 3.11
- Dependencies listed in `requirements.txt`

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `lenet.ipynb`: Main Jupyter notebook containing the implementation
- `requirements.txt`: Python package dependencies
- Generated files during execution:
  - `lenet.pt`: Saved trained LeNet model parameters
  - `qlenet.pt`: Saved quantized LeNet model parameters
  - `results.csv`: Random fault injection results
  - `results_c1_5.csv`: Targeted fault injection results for layer c1, bit position 5
  - Various analysis CSV files: `table_4.csv`, `bit_position_impact.csv`, `layer_impact.csv`, `flip_direction_table.csv`

## Usage

1. Open and run the Jupyter notebook:
```bash
jupyter notebook lenet.ipynb
```

2. The notebook will:
   - Train the LeNet-5 model on MNIST
   - Quantize the model to 8-bit integers
   - Perform fault injection experiments
   - Generate analysis results and visualizations

## Key Features

- Training and quantization of LeNet-5
- Random fault injection across all layers
- Targeted fault injection for specific layers/bits
- Comprehensive result analysis and visualization
- Support for both 0-to-1 and 1-to-0 bit flips

## Results

The framework generates several CSV files containing detailed analysis:
- Layer-wise sensitivity analysis
- Bit position vulnerability analysis
- Flip direction impact analysis
- Targeted testing results
