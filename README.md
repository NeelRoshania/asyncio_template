# asyncio-multiprocessing-template
A template to handle asynchronous applications.

This template covers boiler plate for;
- `asyncio`
- `multiprocessing` 

### References

### Installation guide

**Module setup**
1. `python -m venv .env` and `pip3 install --upgrade pip` 
2. `cd .env/scripts ` then `activate`
3. Modify `setup.cfg` and `src`
4. `pip3 install -e .`

**Jupyter kernel setup**
1. `jupyter kernelspec uninstall .example_env` - remove existing kernels called .example_env
2. `python -m ipykernel install --user --name=.example_env`- install new kernel

**Testing**
1. `pytest -v`

**Environment & application setup**
1. `pytest -v`
2. `pytest tests/scripts/test_requestservices.py > tests/test_outcomes/010123` to dump results to file. Use `grep` to search through dump

### Repository setup
1. Authenticate with github 
    - SSH Agent
        - `eval "$(ssh-agent -s)"` to start agent 
        - `ssh-add -l` to check for existing keys
        - `ssh-add ~/.ssh/id_ed25519` to add SSH private key to ssh-agen
    - Test connection & authenticate, 
        - `ssh -T git@github.com`. See [Github SSH Authentication](https://docs.github.com/en/authentication).
2. Authentication troubleshooting
    - [Permission denied (publickey)](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### References
Implementation
- [asycnio](https://docs.python.org/3/library/asyncio.html)
- [Croutines and Tasks](https://docs.python.org/3/library/asyncio-task.html#coroutines)
- [snakeviz](https://jiffyclub.github.io/snakeviz/)
    - generate profile, `python -m cProfile -o program.prof my_program.py`
    - interpret results `snakeviz program.prof`

Others
- [Diagnosing slow python code](https://www.youtube.com/watch?v=m_a0fN48Alw)
- [multiprocessing](https://wiki.python.org/moin/GlobalInterpreterLock)
- [GIL](https://wiki.python.org/moin/GlobalInterpreterLock)
- [Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor)
