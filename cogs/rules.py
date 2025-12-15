import discord
from discord.ext import commands
from discord import app_commands

class RulesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rules = {
            "r1": "**R1❯ Follow Discord Terms & Guidelines**\n\nAll server rules are based on Discord’s Terms of Service and Community Guidelines.\nModded clients like Vencord or BetterDiscord are allowed.",
            "r2": "**R2❯ No Raids, Doxxing, or Swatting**\n\nDo not participate in, joke about, or threaten raids, doxxing, or swatting.\nAny such threat will result in a permanent ban.\nSharing information related to these actions is also prohibited, even “for awareness”.\nYou may discuss incidents for awareness only, without encouraging the behavior.",
            "r3": "**R3❯ No Scams, Malware, or Malicious Links**\n\nUsing Discord for scams, malware, viruses, IP grabbers, or harmful links is strictly prohibited.\nThis applies both inside the server and in DMs.\nCybersecurity discussions are allowed only in appropriate channels.\nDo not share malware, source code, tutorials, tools, or stream such content.",
            "r4": "**R4❯ No Sharing Personal Information**\n\nLeaking or sharing personal information is not allowed.\nThis includes IP addresses, phone numbers, addresses, legal names, IDs, or similar data.",
            "r5": "**R5❯ Voice Channel Conduct**\n\nProhibited behavior in voice channels includes:\nRacism, sexism, hate speech, ToS violations, earrape, or disruptive behavior.\nRecording or archiving conversations without owner permission is not allowed.",
            "r6": "**R6❯ No NSFW, Gore, or Shock Content**\n\nNSFW content, gore, shock content, or explicit behavior is strictly prohibited.\nThis includes jokes or indirect references to such content.\nRacism and sexism are also not allowed.",
            "r7": "**R7❯ No Politics or Religious Debates**\n\nPolitics and religion are not topics for this server.\nAny offensive content toward countries, institutions, or beliefs is prohibited.\nAny reference to Nazis/Hitler or equivalents will result in a permanent ban.",
            "r8": "**R8❯ Profiles Must Follow Rules**\n\nYour Discord profile must comply with server rules and Discord ToS.\nNames, bios, avatars, pronouns, and statuses can be moderated.\nNSFW content, hate speech, impersonation, or malicious content will be punished.",
            "r9": "**R9❯ No Advertising**\n\nAdvertising is not allowed on this server.\nDM advertising without a valid reason is prohibited and can result in a ban.\nIf someone asks for a link, share it via DM only.\nProjects may be shared only in the appropriate channels.",
            "r10": "**R10❯ No Rule Loopholes / Use Common Sense**\n\nThese rules are not exhaustive.\nTrying to bypass rules is not allowed.\nIf unsure, ask staff via tickets or do not proceed.",
            "r11": "**R11❯ Respect Moderation Decisions**\n\nDo not disrupt the server if you disagree with a punishment.\nAppeal respectfully through proper channels.\nIf bias is suspected after appeal, contact staff in this order via tickets only:\nHead Mod → Admin → Owner\nDo not DM staff or add them without consent.",
            "tldr": "**TL;DR**\nUse common sense, respect others, and act maturely."
        }

    async def send_rule(self, ctx, rule_key):
        rule_content = self.rules.get(rule_key)
        if rule_content:
            embed = discord.Embed(description=rule_content, color=discord.Color.blue())
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Rule `{rule_key}` not found.")

    @commands.command(name="r1")
    async def rule1(self, ctx):
        await self.send_rule(ctx, "r1")

    @commands.command(name="r2")
    async def rule2(self, ctx):
        await self.send_rule(ctx, "r2")

    @commands.command(name="r3")
    async def rule3(self, ctx):
        await self.send_rule(ctx, "r3")

    @commands.command(name="r4")
    async def rule4(self, ctx):
        await self.send_rule(ctx, "r4")

    @commands.command(name="r5")
    async def rule5(self, ctx):
        await self.send_rule(ctx, "r5")

    @commands.command(name="r6")
    async def rule6(self, ctx):
        await self.send_rule(ctx, "r6")

    @commands.command(name="r7")
    async def rule7(self, ctx):
        await self.send_rule(ctx, "r7")

    @commands.command(name="r8")
    async def rule8(self, ctx):
        await self.send_rule(ctx, "r8")

    @commands.command(name="r9")
    async def rule9(self, ctx):
        await self.send_rule(ctx, "r9")

    @commands.command(name="r10")
    async def rule10(self, ctx):
        await self.send_rule(ctx, "r10")

    @commands.command(name="r11")
    async def rule11(self, ctx):
        await self.send_rule(ctx, "r11")

    @commands.command(name="tldr")
    async def tldr_rule(self, ctx):
        await self.send_rule(ctx, "tldr")

    @app_commands.command(name="rules", description="Display a specific rule")
    @app_commands.choices(rule=[
        app_commands.Choice(name="R1: Discord Terms", value="r1"),
        app_commands.Choice(name="R2: No Raids/Doxxing", value="r2"),
        app_commands.Choice(name="R3: No Scams/Malware", value="r3"),
        app_commands.Choice(name="R4: No Personal Info", value="r4"),
        app_commands.Choice(name="R5: Voice Conduct", value="r5"),
        app_commands.Choice(name="R6: No NSFW/Gore", value="r6"),
        app_commands.Choice(name="R7: No Politics/Religion", value="r7"),
        app_commands.Choice(name="R8: Profile Rules", value="r8"),
        app_commands.Choice(name="R9: No Advertising", value="r9"),
        app_commands.Choice(name="R10: Common Sense", value="r10"),
        app_commands.Choice(name="R11: Respect Staff", value="r11"),
        app_commands.Choice(name="TL;DR", value="tldr")
    ])
    async def slash_rules(self, interaction: discord.Interaction, rule: app_commands.Choice[str]):
        rule_content = self.rules.get(rule.value)
        if rule_content:
            embed = discord.Embed(description=rule_content, color=discord.Color.blue())
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Rule not found.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(RulesCog(bot))
