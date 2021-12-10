from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)


@task
def test(ctx):
    ctx.run("python3 -m pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("python3 -m pylint src", pty=True)


@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("python3 -m autopep8 --in-place --recursive src", pty=True)


@task
def coverage(ctx):
    ctx.run("python3 -m coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("python3 -m coverage html", pty=True)
