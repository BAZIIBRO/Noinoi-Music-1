import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"Noinoi/DREAMS/search/thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"Noinoi/DREAMS/search/thumb{userid}.png")
    image2 = Image.open("Noinoi/DREAMS/source/LightBlue.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"Noinoi/DREAMS/search/temp{userid}.png")
    img = Image.open(f"search/temp{userid}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Noinoi/DREAMS/source/regular.ttf", 52)
    font2 = ImageFont.truetype("Noinoi/DREAMS/source/medium.ttf", 76)
    draw.text(
        (25, 609),
        f"{title[:18]}...",
        fill="black",
        font=font2,
    )
    draw.text(
        (27, 534),
        f"Playing on {ctitle[:12]}",
        fill="black",
        font=font,
    )
    img.save(f"Noinoi/DREAMS/search/final{userid}.png")
    os.remove(f"Noinoi/DREAMS/search/temp{userid}.png")
    os.remove(f"Noinoi/DREAMS/search/thumb{userid}.png")
    final = f"Noinoi/DREAMS/search/final{userid}.png"
    return final
