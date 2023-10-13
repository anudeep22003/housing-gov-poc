## Tasks

- [ ] Remove memory implementation and make sure it works
- [ ] COnvert docs to markdown
- [ ] use docs to create vector index
- [ ] set up query retriever mechanism
- [ ] set up cors for frontend

# First set up the environment

First set up the environment. You have two options:

- mamba. Install from [here](https://mamba.readthedocs.io/en/latest/installation.html) and run `mamba env create -f env.yml`
  - then run `mamba activate poc-pdf-demo`
- if using pip there is a `requirements.txt` file that you can use with `venv`

# To run the server

`uvicorn main:app --port 8000`

- the server will run on port 8000
- it isnt bound to a host so it will be localhost

# api documentation

- documentation is available at [http://localhost:8000/redoc](http://localhost:8000/redoc)
