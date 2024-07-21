# # x=round(123,-2)
# # y=str(x)
# # z=y[-2]
# # print(z)
# import matplotlib.pyplot as plt

# # Given data
# x_values = [40, 50, 60, 70]
# y_values = [0.18, 0.24, 0.30, 0.35]

# # Create the plot
# plt.plot(x_values, y_values, marker='o')

# # Add titles and labels
# plt.title('Sample Graph')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Show the plot
# plt.show()

from typing import Final
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot token and username
TOKEN: Final  = '6936652267:AAHFC48u21ouCMT3II28LRmJ1R_jNPyTSec'
BOT_USERNAME: Final = '@qwegbfvx_bot'

# Define the function to generate and send the table
async def table(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
*TINGKATAN EMPAT*
| *BIL* | *NAMA* | *NO KP* | *NO TELEFON* | *EMEL* |
| --- | ---- | ----- | ---------- | ---- |
| 1   |      |       |            |      |
| 2   |      |       |            |      |
| 3   |      |       |            |      |
| 4   |      |       |            |      |
| 5   |      |       |            |      |
| 6   |      |       |            |      |
| 7   |      |       |            |      |
| 8   |      |       |            |      |
| 9   |      |       |            |      |
| 10  |      |       |            |      |
    """
    
    await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN) # type: ignore

def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Register the /table command
    application.add_handler(CommandHandler("table", table))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()

