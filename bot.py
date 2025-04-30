# Copyright (c) 2025 The Militia Trading Company
# All rights reserved.
#
# This source code is made public for transparency and deployment purposes only.
# No part of this code may be reproduced, modified, or distributed without
# explicit written permission from The Militia Trading Company.
#
# For licensing inquiries, contact: legal@themilitiatradingcompany.com

import os
from dotenv import load_dotenv
import interactions

load_dotenv()  # This does nothing on Render, but keeps local compatibility
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ TOKEN is missing.")
    exit(1)
else:
    print("✅ TOKEN loaded:", TOKEN[:10], "...")

bot = interactions.Client(token=TOKEN)

# ======= Helper Functions =======

def has_militia_role(ctx):
    allowed_roles = ["Militia"]
    user_roles = [role.name for role in ctx.author.roles]
    return any(role in allowed_roles for role in user_roles)

# ======= Phase 1 – Core TMTC Concepts =======

@interactions.slash_command(
    name="scalpingfirst",
    description="Explain why scalping is the foundation of The Thesis Method.",
)
async def scalpingfirst(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("At TMTC, scalping is the foundation. Scalping teaches precision, discipline, and speed — all required skills before expanding to larger timeframes. Master scalping first to build long-term trading success.")

@interactions.slash_command(
    name="the8020rule",
    description="Explain why markets range 80% of the time.",
)
async def the8020rule(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Markets range 80% of the time and trend only 20% of the time. TMTC trades differently by focusing on sniper entries at extremes, not chasing breakouts into inefficient expansions.")

@interactions.slash_command(
    name="valuearea",
    description="Explain what a Value Area is.",
)
async def valuearea(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("The Value Area (VA) is where 70–80% of volume transacted during a session. Key levels: VAH (high), VAL (low), POC (point of control). TMTC uses the Value Area to find sniper deviations, not random trades inside it.")

@interactions.slash_command(
    name="goldenpocket",
    description="Explain the Golden Pocket (Fibonacci zone).",
)
async def goldenpocket(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("The Golden Pocket is the 61.8%–65% Fibonacci retracement zone. In The Thesis Method, we target GP retests with liquidity sweeps for sniper entries — not blindly buying pullbacks.")

@interactions.slash_command(
    name="thesispull",
    description="Explain how to properly pull Fibonacci in TMTC.",
)
async def thesispull(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("A Thesis Pull uses Fibonacci retracement based on valid, structure-confirmed highs/lows — not random swings. We pull fibs only after structure confirms a bias shift.")

@interactions.slash_command(
    name="sfp",
    description="Explain what an SFP (Swing Failure Pattern) is.",
)
async def sfp(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("An SFP (Swing Failure Pattern) occurs when price sweeps above a high or below a low to trigger liquidity, then sharply rejects. In TMTC, SFPs are critical entry confirmations after liquidity sweeps.")

@interactions.slash_command(
    name="chochbos",
    description="Explain CHOCH and BOS in The Thesis Method.",
)
async def chochbos(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("CHOCH (Change of Character) marks the first sign of a directional shift — the first major break against previous trend. BOS (Break of Structure) confirms continuation after a CHOCH. TMTC respects both during bias formation.")

# ======= Phase 2 – Advanced TMTC Playbook =======

@interactions.slash_command(
    name="steveshallway",
    description="Explain Steve’s Hallway scalping zone inside Value Area.",
)
async def steveshallway(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Steve’s Hallway refers to limited scalping opportunities inside the Value Area. Hallway scalps must align with structure shifts (CHOCH) and require liquidity sweeps and fast confirmation. Only take hallway trades with strict stop control (<1%).")

@interactions.slash_command(
    name="faileauction",
    description="Explain Failed Auction setups inside TMTC framework.",
)
async def faileauction(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("A Failed Auction happens when price attempts to break outside a Value Area but fails to find acceptance, quickly snapping back inside. TMTC trades these failures as high-probability reversal setups after liquidity sweeps.")

@interactions.slash_command(
    name="wd40",
    description="Explain the WD40 Method (Weekly, Daily, 4H Alignment).",
)
async def wd40(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("WD40 Method requires Weekly, Daily, and 4H timeframe alignments before considering sniper trades. TMTC uses WD40 filtering to confirm directional bias and avoid random counter-trend entries.")

@interactions.slash_command(
    name="model1",
    description="Explain TMTC Model 1 (Full Structure Swing).",
)
async def model1(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Model 1 represents a full structure swing. After a CHOCH, price retraces back into the Value Area for a liquidity sweep and Golden Pocket retest before continuation. Full confirmation needed before entry.")

@interactions.slash_command(
    name="model2",
    description="Explain TMTC Model 2 (Hallway Scalps inside VA).",
)
async def model2(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Model 2 is the Hallway Scalping model. Quick structure shifts (CHOCH) and liquidity sweeps occur inside the Value Area, offering fast sniper entries. Must be low-risk, fast-confirmation, small-stop setups.")

@interactions.slash_command(
    name="adb",
    description="Explain TMTC Ascending Double Bottom (ADB) entry.",
)
async def adb(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("ADB (Ascending Double Bottom) happens when price sweeps a low, prints a higher low, and breaks structure upwards. TMTC uses ADB patterns for precision sniper entries after liquidity sweeps.")

# ======= Company Policies & Membership Info =======

@interactions.slash_command(
    name="refundpolicy",
    description="Explain TMTC's refund policy.",
)
async def refundpolicy(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("TMTC maintains a strict no-refund policy for all digital products, memberships, and services. (Policy §2)")

@interactions.slash_command(
    name="cancel",
    description="Explain how members can cancel their subscription.",
)
async def cancel(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("To cancel your membership, log into your payment provider (Patreon, Launchpass, or Stripe) and manage your subscription directly. TMTC cannot cancel memberships on your behalf.")

@interactions.slash_command(
    name="riskpolicy",
    description="Remind members of TMTC risk management standards.",
)
async def riskpolicy(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("TMTC Risk Management: Always risk 0.25–0.5% per trade maximum. Preserve your capital. Mastery comes through longevity, not oversized risk.")

@interactions.slash_command(
    name="coachinginfo",
    description="How to book coaching sessions with ThesisHimself.",
)
async def coachinginfo(ctx):
    if not has_militia_role(ctx):
        await ctx.send("❌ You do not have permission to use this command.", ephemeral=True)
        return
    await ctx.send("Private coaching requires advance payment. Sessions expire in 90 days. Contact @TMTC Support for onboarding.")

# ======= Start the Bot =======
import threading
import http.server
import socketserver
import asyncio

# Dummy HTTP server to trick Render
def dummy_server():
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🔌 Dummy server running on port {PORT}")
        httpd.serve_forever()

# Start dummy server in background
threading.Thread(target=dummy_server, daemon=True).start()

# Start Discord bot
async def start_bot():
    await bot.start()

asyncio.run(start_bot())