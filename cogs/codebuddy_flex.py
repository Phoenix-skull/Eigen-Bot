import discord
from discord.ext import commands
from discord import app_commands
from PIL import Image, ImageDraw, ImageFont
import aiohttp
import io
import os
import math

from utils.codebuddy_database import get_user_stats

class CodeBuddyFlex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.flex_bg_path = "assets/codebuddy/flex_bg.png"
        self.font_path = "assets/codebuddy/fonts/DejaVuSans-Bold.ttf"
        self.gradient_colors = ["#00F6F6", "#583BFB", "#8410FE"]

    async def get_user_balance(self, user_id: int):
        stats = await get_user_stats(user_id)  # (correct_answers, streak, best_streak)
        return stats[0]

    async def get_user_streak(self, user_id: int):
        stats = await get_user_stats(user_id)
        return stats[1]

    def create_hexagon_mask(self, size):
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        w, h = size
        cx, cy = w / 2, h / 2
        r = min(w, h) / 2
        points = []
        for i in range(6):
            angle = math.radians(30 + i * 60)
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            points.append((x, y))
        draw.polygon(points, fill=255)
        return mask

    def draw_gradient_text(self, base_img, text, font, position, gradient_colors):
        text_mask = Image.new("L", base_img.size, 0)
        mask_draw = ImageDraw.Draw(text_mask)
        mask_draw.text(position, text, font=font, fill=255)
        
        gradient = Image.new("RGBA", base_img.size)
        draw = ImageDraw.Draw(gradient)
        w, h = base_img.size
        top_color = tuple(int(gradient_colors[0][i:i+2], 16) for i in (1,3,5)) + (255,)
        mid_color = tuple(int(gradient_colors[1][i:i+2], 16) for i in (1,3,5)) + (255,)
        bottom_color = tuple(int(gradient_colors[2][i:i+2], 16) for i in (1,3,5)) + (255,)

        for y in range(h):
            if y < h//2:
                r = (y/(h//2))
                color = tuple(int(top_color[i]*(1-r) + mid_color[i]*r) for i in range(4))
            else:
                r = ((y-h//2)/(h//2))
                color = tuple(int(mid_color[i]*(1-r) + bottom_color[i]*r) for i in range(4))
            draw.line([(0, y), (w, y)], fill=color)

        base_img.paste(gradient, (0,0), mask=text_mask)

    def draw_gradient_border(self, base_img, thickness=10):
        w, h = base_img.size
        gradient = Image.new("RGBA", (w, h))
        draw = ImageDraw.Draw(gradient)

        top_color = tuple(int(self.gradient_colors[0][i:i+2], 16) for i in (1,3,5)) + (255,)
        mid_color = tuple(int(self.gradient_colors[1][i:i+2], 16) for i in (1,3,5)) + (255,)
        bottom_color = tuple(int(self.gradient_colors[2][i:i+2], 16) for i in (1,3,5)) + (255,)

        for y in range(h):
            if y < h//2:
                r = y/(h//2)
                color = tuple(int(top_color[i]*(1-r) + mid_color[i]*r) for i in range(4))
            else:
                r = (y - h//2)/(h//2)
                color = tuple(int(mid_color[i]*(1-r) + bottom_color[i]*r) for i in range(4))
            draw.line([(0, y), (w, y)], fill=color)

        mask = Image.new("L", (w, h), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rectangle([0, 0, w, h], fill=255)
        mask_draw.rectangle([thickness, thickness, w-thickness, h-thickness], fill=0)

        base_img.paste(gradient, (0,0), mask=mask)

    @app_commands.command(name="codeflex", description="Show your flex with points and streak")
    async def codeflex(self, interaction: discord.Interaction):
        await interaction.response.defer()
        user = interaction.user

        if not os.path.isfile(self.flex_bg_path):
            await interaction.followup.send("Background not found.", ephemeral=True)
            return
        base_img = Image.open(self.flex_bg_path).convert("RGBA")

        # Avatar
        async with aiohttp.ClientSession() as session:
            async with session.get(user.display_avatar.url) as resp:
                avatar_bytes = await resp.read()
        avatar_img = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA").resize((128, 128))

        mask = self.create_hexagon_mask(avatar_img.size)
        avatar_img.putalpha(mask)

        avatar_center_x = 220
        avatar_center_y = 256
        avatar_x = avatar_center_x - avatar_img.width // 2
        avatar_y = avatar_center_y - avatar_img.height // 2
        base_img.paste(avatar_img, (avatar_x, avatar_y), avatar_img)

        # Punkte, Streak, Name
        points = await self.get_user_balance(user.id)
        streak = await self.get_user_streak(user.id)
        name = user.display_name[:13]  # maximal 13 Zeichen

        font_size = 60
        try:
            font = ImageFont.truetype(self.font_path, font_size)
        except IOError:
            font = ImageFont.load_default()

        text_x = int(base_img.width * 0.45)
        text_y = int(base_img.height * 0.25)

        self.draw_gradient_text(base_img, name, font, (text_x, text_y), self.gradient_colors)
        self.draw_gradient_text(base_img, f"Points: {points}", font, (text_x, text_y + font_size + 10), self.gradient_colors)
        self.draw_gradient_text(base_img, f"Streak: {streak}", font, (text_x, text_y + 2*(font_size + 10)), self.gradient_colors)

        # Rahmen hinzufügen
        self.draw_gradient_border(base_img, thickness=10)

        output = io.BytesIO()
        base_img.save(output, format="PNG")
        output.seek(0)
        file = discord.File(fp=output, filename="flex.png")
        await interaction.followup.send(file=file)

async def setup(bot: commands.Bot):
    await bot.add_cog(CodeBuddyFlex(bot))
