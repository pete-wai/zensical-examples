# Features that connect to another service

These examples explain where external services fit. No analytics account, comment service, or feedback collection is connected to this showcase.

## Comments: a discussion attached to a page

A comment integration puts a discussion below the article. Readers can ask about an example or suggest a correction without editing the documentation. A release announcement is a second useful setting: discussion stays beside the release instead of being scattered across unrelated channels.

A GitHub-backed integration such as Giscus requires an actual repository discussion setup and its identifiers. There is no live comment box here because that setup would create a real communication channel.

[Official comments guide](https://zensical.org/docs/setup/comment-system/)

## Analytics: learn what people read

Analytics can answer questions such as “Which migration guide gets used?” and “Are readers searching for a topic we have not documented?” A service receives events; the site itself is not the reporting dashboard.

For a product manual, page views can help prioritize maintenance. For a tutorial collection, search terms can reveal missing explanations. No measurement ID or tracking script is configured here.

[Official analytics guide](https://zensical.org/docs/setup/analytics/)

## Feedback: a quick signal about a page

A helpful/not-helpful control can collect a small signal at the end of an article. It is useful after a troubleshooting recipe or a conceptual explanation. The response still needs somewhere to go and a process for acting on it; showing a decorative button would not demonstrate that workflow.

The `hide: [feedback]` page setting removes the widget where it is inappropriate. This site leaves the integration disabled rather than implying that responses are being recorded.
