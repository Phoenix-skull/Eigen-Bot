"""
Daily Quests System - Inspired by OWO bot
Complete daily challenges to earn streak freezes and bonus hints!
"""

import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
from utils.codebuddy_database import (
    get_daily_quest_progress, 
    get_quest_rewards,
    use_streak_freeze
)


class DailyQuestsCog(commands.Cog):
    """Daily quests and rewards system for CodeBuddy."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="dailyquest", aliases=["dq", "quests", "quest", "daily", "checklist"])
    async def daily_quest(self, ctx: commands.Context):
        """
        View your daily quest progress and rewards.
        Complete 5 quizzes and vote for the bot to earn rewards!
        """
        user_id = ctx.author.id
        
        try:
            # Get quest progress
            quest_date, quizzes, voted, completed, freezes, _ = await get_daily_quest_progress(user_id)
            
            # Create embed
            embed = discord.Embed(
                title="Daily Quest Checklist",
                description="Complete all tasks to earn rewards! Resets every 24 hours.",
                color=0x000000
            )
            
            # Quest tasks
            quiz_status = "Done" if quizzes >= 5 else f"{quizzes}/5"
            
            tasks = f"""
            **Solve 5 Basic Quizzes** {quiz_status}
            Answer <#1398986762352857129> quiz questions correctly to complete the quest!
            
            *Note: Top.gg voting will be added soon for bonus rewards!*
            """
            
            embed.add_field(name="Quest Tasks", value=tasks, inline=False)
            
            # Rewards section
            if completed == 1:
                reward_text = "**Quest Completed!** You earned:\n• 1 Streak Freeze"
            else:
                reward_text = "Complete all tasks to earn:\n• 1 Streak Freeze (protects your streak)"
            
            embed.add_field(name="Rewards", value=reward_text, inline=False)
            
            # Current inventory
            inventory = f"Streak Freezes: **{freezes}**"
            embed.add_field(name="Your Inventory", value=inventory, inline=False)
            
            # Footer
            embed.set_footer(text=f"Quest Date: {quest_date.strftime('%Y-%m-%d')} • Keep grinding!")
            embed.set_thumbnail(url=ctx.author.display_avatar.url)
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            print(f"[Error in daily_quest command]: {e}")
            await ctx.send("An error occurred while fetching your quest progress.", ephemeral=True)
    
    @commands.command(name="inventory", aliases=["inv", "rewards"])
    async def inventory(self, ctx: commands.Context):
        """View your quest rewards inventory."""
        user_id = ctx.author.id
        
        try:
            freezes, _ = await get_quest_rewards(user_id)
            
            embed = discord.Embed(
                title="Your Inventory",
                description="Items earned from completing daily quests",
                color=0x000000
            )
            
            # Streak Freezes
            freeze_desc = "Protect your quiz streak when you answer incorrectly.\nAutomatically used when needed."
            embed.add_field(
                name=f"Streak Freezes: {freezes}",
                value=freeze_desc,
                inline=False
            )
            
            # How to earn more
            embed.add_field(
                name="How to Earn More",
                value="Complete your daily quest! Use `?dailyquest` to check progress.",
                inline=False
            )
            
            embed.set_thumbnail(url=ctx.author.display_avatar.url)
            embed.set_footer(text="Keep completing quests to build your inventory!")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            print(f"[Error in inventory command]: {e}")
            await ctx.send("An error occurred while fetching your inventory.", ephemeral=True)
    
    @app_commands.command(name="dailyquest", description="View your daily quest progress and rewards")
    async def daily_quest_slash(self, interaction: discord.Interaction):
        """Slash command version of dailyquest."""
        user_id = interaction.user.id
        
        try:
            # Get quest progress
            quest_date, quizzes, voted, completed, freezes, _ = await get_daily_quest_progress(user_id)
            
            # Create embed
            embed = discord.Embed(
                title="Daily Quest Checklist",
                description="Complete all tasks to earn rewards! Resets every 24 hours.",
                color=0x000000
            )
            
            # Quest tasks
            quiz_status = "Done" if quizzes >= 5 else f"{quizzes}/5"
            
            tasks = f"""
            **Solve 5 Basic Quizzes** {quiz_status}
            *Answer CodeBuddy quiz questions correctly to complete the quest!*
            
            *Note: Top.gg voting will be added soon for bonus rewards!*
            """
            
            embed.add_field(name="Quest Tasks", value=tasks, inline=False)
            
            # Rewards section
            if completed == 1:
                reward_text = "**Quest Completed!** You earned:\n• 1 Streak Freeze"
            else:
                reward_text = "Complete all tasks to earn:\n• 1 Streak Freeze (protects your streak)"
            
            embed.add_field(name="Rewards", value=reward_text, inline=False)
            
            # Current inventory
            inventory = f"Streak Freezes: **{freezes}**"
            embed.add_field(name="Your Inventory", value=inventory, inline=False)
            
            # Footer
            embed.set_footer(text=f"Quest Date: {quest_date.strftime('%Y-%m-%d')} • Keep grinding!")
            embed.set_thumbnail(url=interaction.user.display_avatar.url)
            
            await interaction.response.send_message(embed=embed)
            
        except Exception as e:
            print(f"[Error in daily_quest_slash command]: {e}")
            await interaction.response.send_message("An error occurred while fetching your quest progress.", ephemeral=True)


async def setup(bot: commands.Bot):
    """Setup function to load the cog."""
    await bot.add_cog(DailyQuestsCog(bot))
