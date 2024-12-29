# Run test
- `ptw <file_path>`
 
# Submit
- `exercism submit <directory>/<file_name>.py`

# Compilation with mypy
- `mypy script.py`


# watch file with `python3` to execut
```
    watchmedo shell-command \
    --patterns="returns-practice/returns_practice.py" \
    --command='python3 returns-practice/returns_practice.py' \
    --recursive \
    --drop
```

# watch file with `mypy` to check typing error
```
    watchmedo shell-command \
    --patterns="returns-practice/returns_practice.py" \
    --command='mypy returns-practice/returns_practice.py' \
    --recursive \
    --drop
```