from telegram.ext import Updater, CommandHandler
import settings

def start_bot(bot, update):
	txt = """Привет!
	Как ты?
	"""
	update.messenger.reply_text(txt)
	print("start")

def main():
	upd = Updater(settings.TELEGA_API)
	
	upd.dispatcher.add_handler(CommandHandler("start", start_bot))

	upd.start_polling()
	upd.idle()


if __name__ == '__main__':
	main()
