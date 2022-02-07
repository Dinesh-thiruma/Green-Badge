from PIL import Image, ImageFont, ImageDraw
import datetime

# Enter your name here
USER_NAME = input("Enter your name: ")

# Getting image and gif files
img = Image.open("green_badge.png")
gif = Image.open("green_badge_gif.gif")

# Getting font files
name_font = ImageFont.truetype("fonts/Freight Micro Bold.otf", 60)
time_font = ImageFont.truetype("fonts/SFPRODISPLAYMEDIUM.OTF", 30)
date_font = ImageFont.truetype("fonts/PMNCaeciliaSansTextRg.TTF", 60)

# Getting current datetime object
cur_time = datetime.datetime.now()

# Getting string of current time
minute = cur_time.minute
hour = cur_time.hour
if minute < 10:
    time_str = str(hour%12) + ":" + str(0) + str(minute)
else:
    time_str = str(hour%12) + ":" + str(minute)

# Getting string of current date
MONTH_ARR = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month, day, year = cur_time.month, cur_time.day, cur_time.year
date_str = MONTH_ARR[month-1] + " " + str(day) + ", " + str(year)

# Adding text to image
draw_obj = ImageDraw.Draw(img)
draw_obj.text((70, 61), time_str, font=time_font, fill=(255, 255, 255, 255), anchor="ms", align="center")
draw_obj.text((410, 280), USER_NAME, font=name_font, fill=(0, 0, 0, 0), anchor="ms", align="center")
draw_obj.text((410, 630), date_str, font=date_font, fill=(51, 51, 51, 0), anchor="ms", align="center")

# Saves a static version of the green badge w/o the moving checkmark
img.save('green_badge_static.png', quality=95)

# Form an array with final frames for the gif
new_arr = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    gif.save("IGNORE/gif.png")
    frame_gif = Image.open("IGNORE/gif.png")
    
    # resizes the checkmark gif
    width, height = frame_gif.size
    ratio = 1.37
    frame_gif = frame_gif.resize((round(width * ratio), round(height * ratio)), resample=0)
    img.paste(frame_gif, (2,650))
    img.save("IGNORE/final_frame" + str(frame) + ".png")
    new_arr.append(Image.open("IGNORE/final_frame" + str(frame) + ".png"))
    
#Saves the gif locally
new_arr[0].save(USER_NAME + '_green_badge.gif', save_all = True, append_images = new_arr[1:], optimize = False, duration = 30, loop = 0)