"""
team_hub.py — GTM Ops Team Hub
Links to internal tools + how-to docs for each.
Deploy as a standalone Streamlit app on Community Cloud.
Edit the TOOLS list to add/remove/update entries.
"""

import streamlit as st

st.set_page_config(
    page_title="GTM Ops — Team Hub",
    page_icon="⚙️",
    layout="wide",
)

st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .tool-header { color: #003F70; font-size: 1rem; font-weight: 700; margin-bottom: 0.2rem; }
    .tool-desc   { color: #444; font-size: 0.88rem; margin-bottom: 0.5rem; line-height: 1.45; }
    .badge {
        display: inline-block;
        border-radius: 4px;
        font-size: 0.72rem;
        padding: 1px 8px;
        font-weight: 600;
        margin-right: 4px;
    }
    .badge-sf  { background:#E8F0FE; color:#003F70; }
    .badge-xl  { background:#E6F4EA; color:#1B6B3A; }
    .badge-mo  { background:#FFF3CD; color:#856404; }
    .badge-wk  { background:#F3E8FD; color:#5B2D8E; }
    .divider   { border-top: 1px solid #eee; margin: 1.2rem 0; }
    h1 { color: #003F70; }
</style>
""", unsafe_allow_html=True)

# ── Tool registry ──────────────────────────────────────────────────────────
# badges: "sf" = Salesforce, "xl" = needs Excel upload, "mo" = run monthly, "wk" = run weekly
TOOLS = [
    {
        "name": "Territory Redistribution Tool",
        "description": (
            "Redistributes accounts owned by a rep who is departing or going on extended leave. "
            "Divides the territory equally across the remaining team, with the option to also "
            "distribute any open opportunities. Automatically updates the FY18 Sales Planning "
            "field on all affected accounts. Once complete, download the output file, review it, "
            "and submit a case to Field Services directly from the app."
        ),
        "url": "https://account-reassignment-app-xbtckvpir.streamlit.app/",
        "badges": ["sf", "xl"],
        "upload_note": None,
        "download_note": "Always review the downloaded file before submitting to FS — confirm account counts match the departing rep's territory and that no accounts are missing.",
        "how_to": [
            "Select the departing rep from the dropdown. The app pulls their current account and opportunity list live from Salesforce.",
            "Choose which team members will absorb the territory. The app will calculate an equal split automatically.",
            "Toggle **Include Open Opportunities** on or off depending on whether opps should also be redistributed.",
            "Review the proposed assignment table. Adjust any individual assignments manually if needed before confirming.",
            "Click **Generate Output** — this updates the FY18 Sales Planning field on all affected accounts.",
            "Download the output file and review it. Check that the total account count matches the rep's original territory.",
            "Click **Submit Case to FS** to send the reassignment request. Attach the downloaded file to the case when prompted.",
        ],
    },
    {
        "name": "Account Transitions — New Biz to Client Sales",
        "description": (
            "Runs the monthly new account transition process for accounts moving from New Business "
            "into Client Sales. Pulls current rep volumes across Client Sales, factors in CSM "
            "partnerships, and assigns incoming accounts to balance territory load. "
            "Run once at the start of each month for that month's transitions — for example, "
            "run on November 1st for all November transitions."
        ),
        "url": "https://acct-transition-app-bw44z4vo94mqw2mgsubkqc.streamlit.app/",
        "badges": ["sf", "mo"],
        "upload_note": None,
        "download_note": None,
        "how_to": [
            "Run this tool on the **first of the month** for that month's transitions. Do not run it mid-month.",
            "The app automatically pulls the list of accounts scheduled to transition from the New Business report in Salesforce.",
            "It then pulls current rep volumes for all Client Sales reps to calculate available capacity.",
            "Review the proposed assignments — the app factors in CSM partnerships so accounts stay with familiar success teams where possible.",
            "Adjust any assignments manually if you spot an issue (e.g. rep on leave, territory mismatch).",
            "Click **Confirm & Push** to apply the assignments. The app updates the account owner and team fields in Salesforce.",
            "Download the summary and file it in the shared drive under the relevant month folder.",
        ],
    },
    {
        "name": "Former Customers — Return to New Biz",
        "description": (
            "Identifies former customer accounts that have hit the 6-month mark since their "
            "former customer date stamp and need to move back to the New Business teams. "
            "Pulls the report automatically, assigns accounts based on preloaded territory files, "
            "updates the account owner and marketing fields, and generates a ready-to-send email "
            "to Field Services. You just need to attach the downloaded file to the email before sending. "
            "If the New Biz roster has changed, updated territory files can be loaded directly in the app."
        ),
        "url": "https://former-customers-pbmqfhyxzucvgnltgrawxy.streamlit.app/",
        "badges": ["sf", "xl"],
        "upload_note": "If the New Business roster has changed since the last run, upload the latest territory file before processing. The app will flag if the preloaded file looks stale.",
        "download_note": "Attach the downloaded file to the FS email before sending — the email is generated automatically but the attachment must be added manually.",
        "how_to": [
            "Open the app — it pulls all former customer accounts that crossed the 6-month threshold automatically.",
            "Check whether the preloaded territory file is current. If the New Biz roster has changed, upload the latest version using the file uploader.",
            "Review the proposed assignments. The app maps accounts to New Biz reps based on territory zip codes.",
            "Confirm the assignments. The app updates the account owner and marketing fields in Salesforce.",
            "Click **Generate FS Email** — this drafts the Field Services notification with all affected accounts listed.",
            "Download the output file, then copy the generated email, attach the file, and send to FS.",
        ],
    },
    {
        "name": "New Accounts Vetting App",
        "description": (
            "Runs every week against newly created accounts and checks each one against the Rules "
            "of Engagement for correct assignment. Flags accounts that are incorrectly assigned or "
            "need review — specifically anything with a D&B employee count under 5 or missing entirely. "
            "Lets you validate flagged accounts against LinkedIn in real time before making a decision. "
            "For accounts that need reassigning, select the appropriate team and the app populates the "
            "right rep based on preloaded territory maps. Pushes updates to Field Services in a couple "
            "of clicks. Territory maps may need refreshing if the roster changes."
        ),
        "url": "https://account-assignment-validator.streamlit.app/",
        "badges": ["sf", "wk", "xl"],
        "upload_note": "Territory maps are preloaded but may be out of date if there has been a roster change. Upload a fresh territory file if assignments are populating incorrectly.",
        "download_note": None,
        "how_to": [
            "Run this tool **once per week** — ideally Monday morning before the team starts working the new account queue.",
            "The app pulls all accounts created in the current week from Salesforce automatically.",
            "It checks each account against the ROE: D&B employee count thresholds, team assignment rules, and territory boundaries.",
            "Flagged accounts fall into two buckets: **Incorrect Assignment** (clear rule violation) and **Needs Review** (D&B count under 5 or missing).",
            "For 'Needs Review' accounts, use the **Validate on LinkedIn** button to pull the company page in real time and verify employee count manually.",
            "Select all accounts that need reassigning. Choose the correct team from the dropdown — the app will auto-populate the rep based on the account's zip code and the preloaded territory map.",
            "If the rep populated looks wrong, check whether the territory map is current. Upload a new one if needed.",
            "Click **Send to FS** to submit the reassignment requests. A second confirmation button pushes the updates.",
        ],
    },
]

BADGE_HTML = {
    "sf": '<span class="badge badge-sf">Salesforce</span>',
    "xl": '<span class="badge badge-xl">File upload/download</span>',
    "mo": '<span class="badge badge-mo">Run monthly</span>',
    "wk": '<span class="badge badge-wk">Run weekly</span>',
}

# ── Header ─────────────────────────────────────────────────────────────────
st.markdown("# ⚙️ GTM Ops — Team Hub")
st.markdown(
    "Internal tools for the GTM Ops team. Each entry includes a link to the tool and a "
    "step-by-step guide so anyone on the team can run it independently."
)
st.info("📁 **File upload tools:** always keep the latest territory and hierarchy files in the shared drive so there's a single source of truth.", icon=None)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Quick reference index ──────────────────────────────────────────────────
with st.expander("📋 Quick Reference — which tool does what?", expanded=False):
    task_map = {
        "A rep is leaving or going on extended leave":         "Territory Redistribution Tool",
        "New accounts need to move from New Biz to Client Sales (1st of month)": "Account Transitions — New Biz to Client Sales",
        "Former customer accounts have hit 6 months and need to go back to New Biz": "Former Customers — Return to New Biz",
        "Weekly new account check against ROE and D&B thresholds": "New Accounts Vetting App",
    }
    for task, tool in task_map.items():
        st.markdown(f"- **{task}** → *{tool}*")

st.markdown("")

# ── Tool cards ─────────────────────────────────────────────────────────────
for tool in TOOLS:
    with st.container(border=True):
        left, right = st.columns([6, 1])
        with left:
            badges = "".join(BADGE_HTML.get(b, "") for b in tool["badges"])
            st.markdown(
                f'<p class="tool-header">{tool["name"]}</p>'
                f'<p class="tool-desc">{tool["description"]}</p>'
                f'{badges}',
                unsafe_allow_html=True,
            )
        with right:
            st.link_button("Open →", tool["url"], use_container_width=True)

        if tool.get("upload_note"):
            st.warning(f"**File upload:** {tool['upload_note']}", icon="📎")

        if tool.get("download_note"):
            st.info(f"**Before submitting to FS:** {tool['download_note']}", icon="📋")

        with st.expander("How-to guide"):
            for i, step in enumerate(tool["how_to"], 1):
                st.markdown(f"{i}. {step}")

    st.markdown("")

# ── Footer ─────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    "<p style='color:#aaa;font-size:0.8rem;text-align:center'>"
    "GTM Ops internal use only — update tool entries in team_hub.py</p>",
    unsafe_allow_html=True,
)
