"""
Application invoke tasks are defined in this file.

Tasks makes it easier to use the application.
"""
import shutil
from pathlib import Path
from invoke import task

# define projects directories
app_dir = Path('.')


@task
def dev(ctx):
    """Run the application (use when developing)."""
    ctx.run("python application.py")


@task
def uwsgi(ctx):
    """Run the application with uwsgi (production)."""
    ctx.run('uwsgi --http 0.0.0.0:8080 --wsgi-file application.py')


@task
def test(ctx):
    """Run the tests."""
    ctx.run('ENV=test python -m pytest')


@task
def check(ctx):
    """Run pycodestyle on the project."""
    ctx.run('pycodestyle application.py tasks.py ' + str(app_dir))


@task
def clean(ctx):
    """Clean any python generated files and folders."""
    for pattern in ['__pycache__', '.pytest_cache',
                    '*.pyc', '*.pyo', '*~', '._*']:
        for f in app_dir.rglob(pattern):
            if f.is_dir():
                print('Removing tree {}'.format(f.name))
                shutil.rmtree(f)
            else:
                print('Removing file {}'.format(f.name))
                f.unlink()
