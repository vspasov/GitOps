import subprocess


def test_script_output():
    result = subprocess.run(
        ['python', 'script.py'],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == 'Hello from Mac M1!'
