from aiogram import executor
from aiogram.types import CallbackQuery, Message
from config import dp
import datetime
from datetime import *
import requests
from keyboards import *
import logging
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: Message):
    txt = '<b>Assalom aleykum. Namoz vaqtlari botiga xush kelibsiz!</b>'
    await message.answer(txt, parse_mode='html', reply_markup=menu)

@dp.callback_query_handler(text='back')
async def back(call: CallbackQuery):
    await call.message.edit_text('<b>Assalom aleykum. Namoz vaqtlari botiga xush kelibsiz!</b>', parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=menu)

@dp.callback_query_handler(text='toshkent')
async def toshkent_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Toshkent shahri)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=toshkent_btn)

@dp.callback_query_handler(text='ttomorrow')
async def toshkent_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Toshkent shahri)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=toshkent1_btn)

@dp.callback_query_handler(text='andijon')
async def andijon_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'(<b>Andijon viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=andijon_btn)

@dp.callback_query_handler(text='atomorrow')
async def andijon_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Andijon viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=andijon1_btn)

@dp.callback_query_handler(text='buxoro')
async def buxoro_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Buxoro viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=buxoro_btn)

@dp.callback_query_handler(text='btomorrow')
async def buxoro_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Buxoro viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=buxoro1_btn)

@dp.callback_query_handler(text='fargona')
async def fargona_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Farg\'ona viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=fargona_btn)

@dp.callback_query_handler(text='ftomorrow')
async def fargona_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Farg\'ona viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=fargona1_btn)


@dp.callback_query_handler(text='jizzax')
async def jizzax_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Jizzax viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=jizzax_btn)

@dp.callback_query_handler(text='jtomorrow')
async def jizzax_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Jizzax viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=jizzax1_btn)


@dp.callback_query_handler(text='xorazm')
async def xorazm_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Xorazm viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=xorazm_btn)

@dp.callback_query_handler(text='xtomorrow')
async def xorazm_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today_time = datetime.today().now()
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Xorazm viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=xorazm1_btn)

@dp.callback_query_handler(text='namangan')
async def namangan_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Namangan viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=namangan_btn)

@dp.callback_query_handler(text='nmtomorrow')
async def namangan_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Namangan viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=namangan1_btn)

@dp.callback_query_handler(text='navoiy')
async def navoiy_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Navoiy viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=navoiy_btn)

@dp.callback_query_handler(text='nvtomorrow')
async def navoiy_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Navoiy viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=navoiy1_btn)

@dp.callback_query_handler(text='nukus')
async def qoraqalpoq_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>Qoraqalpog\'iston Respublikasi</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=nukus_btn)

@dp.callback_query_handler(text='nktomorrow')
async def qoraqalpoq_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Qoraqalpog\'iston Respublikasi)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=nukus1_btn)

@dp.callback_query_handler(text='samarqand')
async def samarqand_bugun(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await call.message.edit_text(f'<b>(Samarqand viloyati)</b> namoz vaqti {today}\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=samarqand_btn)

@dp.callback_query_handler(text='stomorrow')
async def samarqand_ertaga(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f'<b>(Samarqand viloyati)</b> namoz vaqti ertangi kun\n\n'
                                 f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                 f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                 f'-------------------------------------\n'
                                 f'🕢 Bomdod          {bomdod}\n'
                                 f'-------------------------------------\n'
                                 f'☀ Quyosh            {quyosh_ch}\n'
                                 f'-------------------------------------\n'
                                 f'🕑 Peshin              {peshin}\n'
                                 f'-------------------------------------\n'
                                 f'🕓 Asr                    {asr}\n'
                                 f'-------------------------------------\n'
                                 f'🕠 Shom                {shom}\n'
                                 f'-------------------------------------\n'
                                 f'🕖 Hufton             {xufton}\n'
                                 f'-------------------------------------\n'
                                 f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                 f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                 f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                 f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>',
                                 parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=samarqand1_btn)




if __name__ == '__main__':
    executor.start_polling(dp)