# Copyright (c) 2025 The Militia Trading Company
# All rights reserved.
#
# This source code is made public for transparency and deployment purposes only.
# No part of this code may be reproduced, modified, or distributed without
# explicit written permission from The Militia Trading Company.
#
# For licensing inquiries, contact: legal@themilitiatradingcompany.com

import os
import threading
import http.server
import socketserver
from dotenv import load_dotenv

# ─── Load & Validate Token ─────────────────────────────────────────────────────
load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("Missing TOKEN")

print("✅ TOKEN loaded:", TOKEN[:10], "...")

# ─── Initialize Discord Client ─────────────────────────────────────────────────
bot = interactions.Client(token=TOKEN, sync_commands=True)

# ─── Permission Check Helper ────────────────────────────────────────────────────
def has_militia_role(ctx):
    allowed_roles = ["Militia"]
    user_roles = [r.name for r in ctx.author.roles]
    return any(r in allowed_roles for r in user_roles)

# ─── Phase 1 – Core TMTC Concepts ────────────────────────────────────────────────
@interactions.slash_command(
    name="scalpingfirst",
    description="Explain why scalping is the foundation of The Thesis Method.",
)
async def scalpingfirst(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "At TMTC, scalping is the foundation. Scalping teaches precision, discipline, "
        "and speed — all required skills before expanding to larger timeframes. "
        "Master scalping first to build long-term trading success."
    )

@interactions.slash_command(
    name="the8020rule",
    description="Explain why markets range 80% of the time.",
)
async def the8020rule(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "Markets range 80% of the time and trend only 20% of the time. TMTC trades "
        "differently by focusing on sniper entries at extremes, not chasing breakouts."
    )

@interactions.slash_command(
    name="valuearea",
    description="Explain what a Value Area is.",
)
async def valuearea(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "The Value Area (VA) is where 70–80% of volume transacted during a session. "
        "Key levels: VAH (high), VAL (low), POC (point of control). TMTC uses the VA to "
        "find sniper deviations, not random trades inside it."
    )

@interactions.slash_command(
    name="goldenpocket",
    description="Explain the Golden Pocket (Fibonacci zone).",
)
async def goldenpocket(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "The Golden Pocket is the 61.8%–65% Fibonacci retracement zone. In The Thesis Method, "
        "we target GP retests with liquidity sweeps for sniper entries — not blindly buying pullbacks."
    )

@interactions.slash_command(
    name="thesispull",
    description="Explain how to properly pull Fibonacci in TMTC.",
)
async def thesispull(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "A Thesis Pull uses Fibonacci retracement based on valid, structure-confirmed highs/lows — "
        "not random swings. We pull fibs only after structure confirms a bias shift."
    )

@interactions.slash_command(
    name="sfp",
    description="Explain what an SFP (Swing Failure Pattern) is.",
)
async def sfp(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "An SFP (Swing Failure Pattern) occurs when price sweeps a high/low to trigger liquidity, "
        "then sharply rejects. In TMTC, SFPs are critical entry confirmations after liquidity sweeps."
    )

@interactions.slash_command(
    name="chochbos",
    description="Explain CHOCH and BOS in The Thesis Method.",
)
async def chochbos(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "CHOCH (Change of Character) marks the first sign of a directional shift. BOS (Break of Structure) "
        "confirms continuation after a CHOCH. TMTC respects both when forming bias."
    )

# ─── Phase 2 – Advanced TMTC Playbook ────────────────────────────────────────────
@interactions.slash_command(
    name="steveshallway",
    description="Explain Steve’s Hallway scalping zone inside Value Area.",
)
async def steveshallway(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "Steve’s Hallway refers to limited scalping opportunities inside the Value Area. Hallway scalps "
        "must align with CHOCH, require liquidity sweeps, and fast confirmation. Strict stop control (<1%)."
    )

@interactions.slash_command(
    name="failedaauction",
    description="Explain Failed Auction setups inside TMTC framework.",
)
async def faileauction(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "A Failed Auction is when price breaches the VA edge but fails to hold, snapping back inside. "
        "TMTC trades these as high-probability reversals after liquidity sweeps."
    )

@interactions.slash_command(
    name="wd40",
    description="Explain the WD40 Method (Weekly, Daily, 4H Alignment).",
)
async def wd40(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "WD40 requires Weekly, Daily, and 4H timeframe alignments before considering sniper trades. "
        "TMTC uses it to confirm bias and avoid random counter-trend entries."
    )

@interactions.slash_command(
    name="model1",
    description="Explain TMTC Model 1 (Full Structure Swing).",
)
async def model1(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "Model 1 is a full-structure swing: CHOCH → retrace into VA for liquidity sweep + GP retest → continuation."
    )

@interactions.slash_command(
    name="model2",
    description="Explain TMTC Model 2 (Hallway Scalps inside VA).",
)
async def model2(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "Model 2 is the Hallway Scalping model: quick CHOCH + liquidity sweeps inside VA → fast sniper entries."
    )

@interactions.slash_command(
    name="adb",
    description="Explain TMTC Ascending Double Bottom (ADB) entry.",
)
async def adb(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "ADB (Ascending Double Bottom) is when price sweeps a low, prints a higher low, then breaks structure up. "
        "TMTC uses ADB for precision sniper entries."
    )

# ─── Company Policies & Membership Info ─────────────────────────────────────────
@interactions.slash_command(
    name="refundpolicy",
    description="Explain TMTC's refund policy.",
)
async def refundpolicy(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("TMTC maintains a strict no-refund policy for all digital products, memberships, and services.")

@interactions.slash_command(
    name="cancel",
    description="Explain how members can cancel their subscription.",
)
async def cancel(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "To cancel your membership, log into your payment provider (Patreon, Launchpass, or Stripe) "
        "and manage your subscription directly. TMTC cannot cancel on your behalf."
    )

@interactions.slash_command(
    name="riskpolicy",
    description="Remind members of TMTC risk management standards.",
)
async def riskpolicy(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Always risk 0.25–0.5% per trade max. Preserve capital and trade for longevity, not one-offs.")

@interactions.slash_command(
    name="coachinginfo",
    description="How to book coaching sessions with ThesisHimself.",
)
async def coachinginfo(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send(
        "Private coaching requires advance payment. Sessions expire in 90 days. Contact @TMTC Support to onboard."
    )

# ─── Health-Check HTTP Handler ───────────────────────────────────────────
class HealthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    with socketserver.TCPServer(("", port), HealthHandler) as server:
        print(f"🔌 HTTP server listening on port {port}")
        server.serve_forever()

# ─── Start Services ───────────────────────────────────────────────────────
if __name__ == "__main__":
    # 1) Launch the health-check server in the background
    threading.Thread(target=run_http_server, daemon=True).start()

    # 2) Connect your Discord bot (this blocks indefinitely)
    bot.start()