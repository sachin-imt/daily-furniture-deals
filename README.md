# Daily Australian Furniture Deal Hunter

Automatically hunts for the best furniture and appliance deals across Australian retailers every morning, then emails a full HTML report to sachin.imt@gmail.com.

## How it works

1. GitHub Actions runs every day at 7am AEST
2. Claude Code searches 15+ Australian retailers for 16 furniture/appliance items
3. Finds direct product links, prices, discounts, and coupon codes
4. Generates a styled HTML email report
5. Sends it via Gmail to sachin.imt@gmail.com
6. Archives each daily report in the `/archive` folder

## Shopping list covered

Living Room (7 items) · Bedroom (5 items) · Kitchen/Appliances (1 item) · Home Office x2 (2 items) · Outdoor (1 item)

**Budget target:** $10,000–$12,000 AUD

## Setup — Required GitHub Secrets

Go to your repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from console.anthropic.com |
| `GMAIL_USERNAME` | Your Gmail address (e.g. sachin.imt@gmail.com) |
| `GMAIL_APP_PASSWORD` | Gmail App Password (see instructions below) |

## How to create a Gmail App Password

1. Go to your Google Account → **Security**
2. Enable **2-Step Verification** if not already on
3. Search for **"App passwords"** → click it
4. Select app: **Mail** · Select device: **Other** → type "Deal Hunter"
5. Click **Generate** → copy the 16-character password
6. Paste it as the `GMAIL_APP_PASSWORD` secret in GitHub

## Manual trigger

Go to **Actions tab** → **Daily Furniture Deal Hunt** → **Run workflow** to trigger immediately.

## Schedule

Runs daily at **9pm UTC = 7am AEST (Sydney)**. Edit the cron in `.github/workflows/daily-deals.yml` to change the time.
