# mandarin-english-nn

This repository contains code for a neural network designed to translate between Mandarin and English. The project utilizes various tools and libraries to achieve effective translation and language processing.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Project Structure

```plaintext
mandarin-english-nn/
├── src/                    # Source code directory
│   ├── nn.py               # Main script to run the neural network
│   ├── cd.py               # Data generation script
├── .gitignore              # Git ignore file
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation (this file)
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/reubenrenshaw/mandarin-english-nn.git
   cd mandarin-english-nn
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have all dependencies installed as per the `requirements.txt` file.

2. Customize the parameters and settings in `nn.py` as needed for your specific use case.
   
3. Run the main script to start the translation process:

   ```bash
   python src/nn.py
   ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## Acknowledgments

- Thanks to Shai for being epic

---
