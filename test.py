import subprocess

result = subprocess.run(
    ['echo', 'Witaj z procesu potomnego!'], capture_output=True,
    encoding='utf-8')
result.check_returncode()
print(result.stdout)
