# Validation failure fixture

This project contains an intentional broken internal link. It is outside `variants/`, so normal variant discovery does not build it. From the repository root:

```sh
uv run --locked python scripts/check_fixtures.py
```

The runner expects `zensical build --strict -f invalid.toml` from this directory to fail with the missing-page validation diagnostic. A successful build, or a different failure, fails the check.
