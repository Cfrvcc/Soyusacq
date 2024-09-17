from pyrogram import Client, filters

# API məlumatlarınızı burada daxil edin
api_id = '21'
api_hash = 'df5d791a9d5ffc4b0'
bot_token = '712645AAF47fz6fWflyfAA'

app = Client("anti_swear_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start mesajı funksiyası
@app.on_message(filters.command("start"))
async def start(client, message):
    sender_name = message.from_user.first_name
    start_message = f"**Salam** {sender_name}, Mən Qrupdakı söyüşləri avtomatik silən botam .\n📢 Məni Qrupa əlavə edib mesaj silmə hüququ verin."
    await message.reply_text(start_message)

# Söyüşlərin siyahısını fayldan oxumaq funksiyası
def load_bad_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        bad_words = file.read().splitlines()
    return bad_words

# Söyüşləri fayldan oxuyuruq
bad_words = load_bad_words("bad_words.txt")

# Söyüşləri yoxlayan, mesajı silən və istifadəçiyə xəbərdarlıq edən filter
@app.on_message(filters.text & ~filters.private)
async def check_bad_words(client, message):
    words_in_message = message.text.lower().split()
    for word in words_in_message:
        if word in bad_words:  # Yalnız tam uyğun gələn sözləri yoxlayır
            await message.delete()  # Mesajı silir
            
            # İstifadəçinin adını tag edib xəbərdarlıq mesajı göndərir
            user_mention = message.from_user.mention
            await message.reply_text(f"{user_mention}, lütfən qrupda söyüşdən istifadə etməyin!")
            break

app.run()
