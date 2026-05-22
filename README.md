# n8n Masterclass

This repository contains materials and example workflows for the n8n Masterclass. It is intended to help developers learn automation with n8n, including building, testing, and deploying workflows.

## Contents

- `workflows/` - example n8n workflow JSON files
- `docs/` - lesson notes and reference materials
- `scripts/` - helper scripts for running or validating workflows

## Prerequisites

- Node.js (LTS recommended)
- n8n (installed locally or available via Docker)

## Installation

1. Clone the repository:

	git clone <repo-url>

2. Install dependencies (if any):

	npm install

3. Start n8n (example using Docker):

	docker run -it --rm \
	  -p 5678:5678 \
	  -v ~/.n8n:/home/node/.n8n \
	  n8nio/n8n

## Usage

- Import workflow JSON files from the `workflows/` folder into the n8n editor.
- Review the `docs/` folder for step-by-step lessons and explanations.
- Use scripts in `scripts/` to validate or deploy workflows if provided.

## Contributing

Contributions are welcome. Please open issues for bugs or feature requests and submit pull requests for changes.

## License

Specify the project license here (e.g., MIT).

## Contact

For questions, open an issue in the repository.
