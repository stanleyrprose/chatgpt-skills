# Promotion Gate Scheduled Monitoring + Telegram Alerting

This is a small GitHub-hosted monitoring loop around the deterministic Promotion Gate.

## Runtime

`.github/workflows/monitor-promotion-gate.yml` runs:

- every 6 hours at minute 17;
- on manual `workflow_dispatch`.

The job:

1. evaluates the current Promotion Gate;
2. persists semantic state changes under `state/promotion-gate/`;
3. sends Telegram only when `CANDIDATE` or `PROMOTE` has a new alert fingerprint;
4. records a successful Telegram notification receipt so the same alert is not sent repeatedly.

No LLM is called.

## GitHub state

`state/promotion-gate/latest.json`

- current deterministic result;
- current alert fingerprint;
- last successfully sent Telegram fingerprint and timestamp.

`state/promotion-gate/history.jsonl`

- append-only semantic state transitions;
- does not add a new line when the Gate result is unchanged.

This intentionally avoids a new commit every six hours when nothing changed.

## Telegram

The sender is `scripts/send-promotion-alert.py`.

The bot token should belong to `@github_stan_bot`.

Telegram bots cannot use their own bot username as the private-message destination. The workflow therefore needs two GitHub repository secrets:

- `TELEGRAM_BOT_TOKEN` — BotFather token for `@github_stan_bot`;
- `TELEGRAM_CHAT_ID` — numeric chat id for the private chat between the user and the bot.

### One-time setup

First open `@github_stan_bot` in Telegram and send `/start`.

Then add the secrets to this repository:

```bash
gh secret set TELEGRAM_BOT_TOKEN --repo stanleyrprose/chatgpt-skills
gh secret set TELEGRAM_CHAT_ID --repo stanleyrprose/chatgpt-skills
```

If the numeric chat id is not known, after sending `/start`, use the bot token locally to inspect Telegram `getUpdates` and read `message.chat.id`. Do not commit or paste the token into repository files.

## Retry semantics

A Telegram notification is considered delivered only after the Bot API succeeds and `last_sent_fingerprint` is written back to GitHub.

Therefore:

- Gate reaches `CANDIDATE/PROMOTE`, but secrets are missing → result is still stored; alert remains pending.
- Telegram API temporarily fails → workflow fails after state persistence; next scheduled/manual run retries.
- Telegram succeeds → notification receipt is persisted.
- Same fingerprint appears again → no duplicate message.
- Gate falls back to `WATCH/GREEN` → notification fingerprint is reset.
- A later new `CANDIDATE/PROMOTE` episode can alert again.

## Security boundary

The scheduled workflow has `contents: write` only because it must persist state commits.

Checkout credentials are not persisted. The GitHub token is exposed only to the narrow push steps through an HTTP authorization header. Telegram secrets are exposed only to the Telegram-send step.

No token, chat id, or Telegram API response is stored in the repository.

## Manual test

After configuring secrets:

```bash
gh workflow run monitor-promotion-gate.yml --repo stanleyrprose/chatgpt-skills
```

A `GREEN` or `WATCH` state does not send Telegram. This is expected.

Do not fabricate production observations merely to force a Telegram message. Sender behavior is covered by deterministic tests.
