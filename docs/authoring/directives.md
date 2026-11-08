---
title: Directives
---

# Directives

The current [directives guide](https://zensical.org/docs/authoring/directives/) describes a separately distributed Zensical Spark extension. It requires installation and a catalog; this 0.1.0 showcase does not enable it. These examples are source illustrations, not live demos.

## Select content

```text
@if deployment = cloud

    Open the cloud console.

@else

    Configure the local service.
```

## Insert and reuse content

```text
This guide covers @var{deployment}.

@use shared/security-notice.md
```

A catalog declares allowed values and named variants. See the official guide for installation, catalog configuration, and the distinction between directives and textual snippets.
