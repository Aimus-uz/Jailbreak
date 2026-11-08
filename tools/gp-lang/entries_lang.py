# (file, find, uz, ru) — find: exact C# snippet in the ENGLISH source
L = 'lang/Jailbreak.English/'
E = []
def e(f, find, uz, ru): E.append((f, find, uz, ru))

# ---------- Generic ----------
f = L+'Generic/GenericCmdLocale.cs'
e(f, r'''$"Player '{ChatColors.BlueGrey}{query}{ChatColors.Grey}' not found."''',
     r'''$"'{ChatColors.BlueGrey}{query}{ChatColors.Grey}' o'yinchisi topilmadi."''',
     r'''$"Игрок '{ChatColors.BlueGrey}{query}{ChatColors.Grey}' не найден."''')
e(f, r'''$"Multiple players found for '{ChatColors.BlueGrey}{query}{ChatColors.Grey}'."''',
     r'''$"'{ChatColors.BlueGrey}{query}{ChatColors.Grey}' bo'yicha bir nechta o'yinchi topildi."''',
     r'''$"По запросу '{ChatColors.BlueGrey}{query}{ChatColors.Grey}' найдено несколько игроков."''')
e(f, r'''"Command is on cooldown for",''', r'''"Buyruqni qayta ishlatish uchun kuting:",''', r'''"Команду можно использовать через",''')
e(f, r'''"second" + (seconds == 1 ? "" : "s") + "."''', r'''"soniya."''', r'''"сек."''')
e(f, r'''$"Invalid parameter '{ChatColors.BlueGrey}{parameter}{ChatColors.Grey}',",''',
     r'''$"Noto'g'ri qiymat '{ChatColors.BlueGrey}{parameter}{ChatColors.Grey}',",''',
     r'''$"Неверный параметр '{ChatColors.BlueGrey}{parameter}{ChatColors.Grey}',",''')
e(f, r'''"expected a" + (expected[0].IsVowel() ? "n" : ""),''', r'''"kutilgan:",''', r'''"ожидалось:",''')
e(f, r'''$"This requires the {ChatColors.BlueGrey}{permission}{ChatColors.Grey} permission."''',
     r'''$"Buning uchun {ChatColors.BlueGrey}{permission}{ChatColors.Grey} huquqi kerak."''',
     r'''$"Для этого нужно право {ChatColors.BlueGrey}{permission}{ChatColors.Grey}."''')
e(f, r'''$"An error occurred: {ChatColors.Red}{message}{ChatColors.Grey}."''',
     r'''$"Xatolik yuz berdi: {ChatColors.Red}{message}{ChatColors.Grey}."''',
     r'''$"Произошла ошибка: {ChatColors.Red}{message}{ChatColors.Grey}."''')

# ---------- LastGuard ----------
f = L+'LastGuard/LGLocale.cs'
e(f, r'''$" {ChatColors.DarkBlue}Guard>"''', r'''$" {ChatColors.DarkBlue}Qo'riqchi>"''', r'''$" {ChatColors.DarkBlue}Охрана>"''')
e(f, r'''$"{ChatColors.Grey}All Ts are rebels! {ChatColors.DarkRed}LAST GUARD{ChatColors.Grey} must kill until two prisoners alive ({ChatColors.BlueGrey}LR{ChatColors.Grey})."''',
     r'''$"{ChatColors.Grey}Barcha mahbuslar isyonchi! {ChatColors.DarkRed}OXIRGI QO'RIQCHI{ChatColors.Grey} ikki mahbus qolguncha o'ldirishi kerak ({ChatColors.BlueGrey}LR{ChatColors.Grey})."''',
     r'''$"{ChatColors.Grey}Все заключённые — бунтари! {ChatColors.DarkRed}ПОСЛЕДНИЙ ОХРАННИК{ChatColors.Grey} убивает, пока не останутся двое заключённых ({ChatColors.BlueGrey}LR{ChatColors.Grey})."''')
e(f, r'''ChatColors.Grey + "has", ctHealth,''', r'''ChatColors.Grey + "sog'lig'i:", ctHealth,''', r'''ChatColors.Grey + "— здоровье:", ctHealth,''')
e(f, r'''$"{ChatColors.Grey}health, Ts have", tHealth,''', r'''$"{ChatColors.Grey}HP, mahbuslarda jami", tHealth,''', r'''$"{ChatColors.Grey}HP, у заключённых всего", tHealth,''')
e(f, r'''$"{ChatColors.Grey}health total."''', r'''$"{ChatColors.Grey}HP."''', r'''$"{ChatColors.Grey}HP."''')

# ---------- LastRequest ----------
f = L+'LastRequest/B4BLocale.cs'
e(f, r'''PREFIX, "Randomly selected", player, "to go first."''', r'''PREFIX, "Birinchi bo'lib", player, "boshlaydi (tasodifiy)."''', r'''PREFIX, "Первым начинает", player, "(случайно)."''')
e(f, r'''{ PREFIX, player, "picked", weapon }''', r'''{ PREFIX, player, "tanladi:", weapon }''', r'''{ PREFIX, player, "выбрал:", weapon }''')

f = L+'LastRequest/CoinflipLocale.cs'
e(f, r'''"You failed to choose in time, defaulting to",''', r'''"Vaqtida tanlamading, avtomatik tanlandi:",''', r'''"Ты не успел выбрать, выбрано автоматически:",''')
e(f, r'''$"{ChatColors.Green} {(choice ? "Heads" : "Tails")}{ChatColors.Grey}."''', r'''$"{ChatColors.Green} {(choice ? "Gerb" : "Raqam")}{ChatColors.Grey}."''', r'''$"{ChatColors.Green} {(choice ? "Орёл" : "Решка")}{ChatColors.Grey}."''')
e(f, r'''"chose",''', r'''"tanladi:",''', r'''"выбрал:",''')
e(f, r'''$" {ChatColors.Green}{(choice ? "Heads" : "Tails")}{ChatColors.Grey}, flipping..."''', r'''$" {ChatColors.Green}{(choice ? "Gerb" : "Raqam")}{ChatColors.Grey}, tanga tashlanmoqda..."''', r'''$" {ChatColors.Green}{(choice ? "Орёл" : "Решка")}{ChatColors.Grey}, бросаем монету..."''')
e(f, r'''"The coin landed on",''', r'''"Tanga tushdi:",''', r'''"Монета упала:",''')
e(f, r'''$" {ChatColors.Green}{(heads ? "Heads" : "Tails")}{ChatColors.Grey}."''', r'''$" {ChatColors.Green}{(heads ? "Gerb" : "Raqam")}{ChatColors.Grey}."''', r'''$" {ChatColors.Green}{(heads ? "Орёл" : "Решка")}{ChatColors.Grey}."''')

f = L+'LastRequest/GunTossLocale.cs'
e(f, r'''{ PREFIX, player, "threw their gun", dist, "units." }''', r'''{ PREFIX, player, "qurolini otdi:", dist, "birlik." }''', r'''{ PREFIX, player, "бросил оружие на", dist, "ед." }''')

f = L+'LastRequest/LastRequestLocale.cs'
e(f, r'''$"Last Request activated. Type {ChatColors.BlueGrey}!lr{ChatColors.Grey} to start a last request."''',
     r'''$"LR yoqildi. Boshlash uchun {ChatColors.BlueGrey}!lr{ChatColors.Grey} yoz."''',
     r'''$"LR активирован. Напиши {ChatColors.BlueGrey}!lr{ChatColors.Grey}, чтобы начать последнее желание."''')
e(f, r'''$"Last Request {ChatColors.Red}disabled{ChatColors.Grey}."''', r'''$"LR {ChatColors.Red}o'chirildi{ChatColors.Grey}."''', r'''$"LR {ChatColors.Red}выключен{ChatColors.Grey}."''')
e(f, r'''"Last Request is not enabled."''', r'''"LR hali yoqilmagan."''', r'''"LR ещё не активирован."''')
e(f, r'''"Invalid Last Request: "''', r'''"Noto'g'ri LR: "''', r'''"Неверный LR: "''')
e(f, r'''"is starting a",''', r'''"boshlamoqda:",''', r'''"начинает",''')
e(f, r'''"LR against",''', r'''"LR, raqib:",''', r'''"LR против",''')
e(f, r'''return new SimpleView { PREFIX, "Last Request decided." };''', r'''return new SimpleView { PREFIX, "LR yakunlandi." };''', r'''return new SimpleView { PREFIX, "LR завершён." };''')
e(f, r'''"lost the LR, but the prisoner left the game?"''', r'''"LR ni yutqazdi, lekin mahbus o'yindan chiqib ketdi."''', r'''"проиграл LR, но заключённый вышел из игры."''')
e(f, r'''"lost the LR, but the guard left the game?"''', r'''"LR ni yutqazdi, lekin qo'riqchi o'yindan chiqib ketdi."''', r'''"проиграл LR, но охранник вышел из игры."''')
e(f, r'''"Last Request timed out."''', r'''"LR vaqti tugadi."''', r'''"Время LR вышло."''')
e(f, r'''"Last Request interrupted."''', r'''"LR to'xtatildi."''', r'''"LR прерван."''')
e(f, r'''result == LRResult.PRISONER_WIN ? lr.Prisoner : lr.Guard, "won."''', r'''result == LRResult.PRISONER_WIN ? lr.Prisoner : lr.Guard, "g'olib bo'ldi."''', r'''result == LRResult.PRISONER_WIN ? lr.Prisoner : lr.Guard, "победил."''')
e(f, r'''$"You cannot LR, {ChatColors.BlueGrey + reason + ChatColors.Grey}."''', r'''$"LR qila olmaysan: {ChatColors.BlueGrey + reason + ChatColors.Grey}."''', r'''$"Ты не можешь начать LR: {ChatColors.BlueGrey + reason + ChatColors.Grey}."''')
e(f, r'''"You cannot LR",''', r'''"Bu o'yinchi bilan LR qila olmaysan:",''', r'''"Нельзя начать LR с игроком",''')
e(f, r'''{ PREFIX, "Starting in", seconds, "..." }''', r'''{ PREFIX, "Boshlanishiga", seconds, "..." }''', r'''{ PREFIX, "Начало через", seconds, "..." }''')
e(f, r'''{ PREFIX, player, "won by default." }''', r'''{ PREFIX, player, "avtomatik g'olib bo'ldi." }''', r'''{ PREFIX, player, "победил автоматически." }''')
e(f, r'''{ PREFIX, player, "won by health." }''', r'''{ PREFIX, player, "sog'lig'i ko'proq bo'lgani uchun g'olib." }''', r'''{ PREFIX, player, "победил по здоровью." }''')
e(f, r'''{ PREFIX, player, "won by", reason + "." }''', r'''{ PREFIX, player, "g'olib bo'ldi, sabab:", reason + "." }''', r'''{ PREFIX, player, "победил, причина:", reason + "." }''')
e(f, r'''{ PREFIX, player, "won." }''', r'''{ PREFIX, player, "g'olib bo'ldi." }''', r'''{ PREFIX, player, "победил." }''')
e(f, r'''"You or they are in LR, damage blocked."''', r'''"Sen yoki u LR da, zarar bloklandi."''', r'''"Ты или он в LR, урон заблокирован."''')
e(f, r'''"You are not in the same LR as them, damage blocked."''', r'''"Siz bir LR da emassiz, zarar bloklandi."''', r'''"Вы не в одном LR, урон заблокирован."''')
e(f, r'''$"{ChatColors.LightRed}has decided to {ChatColors.DarkRed}LR Rebel {ChatColors.LightRed}with",''', r'''$"{ChatColors.LightRed}{ChatColors.DarkRed}LR isyonini {ChatColors.LightRed}tanladi, sog'lig'i:",''', r'''$"{ChatColors.LightRed}решил {ChatColors.DarkRed}взбунтоваться в LR {ChatColors.LightRed}с",''')
e(f, r'''"Rebelling during last request is disabled."''', r'''"LR paytida isyon qilish o'chirilgan."''', r'''"Бунт во время LR отключён."''')
e(f, r'''"You cannot rebel as a CT during the last request."''', r'''"Qo'riqchi LR paytida isyon qila olmaydi."''', r'''"Охранник не может бунтовать во время LR."''')

f = L+'LastRequest/RPSLocale.cs'
e(f, r'''{ PREFIX, player, "made their choice." }''', r'''{ PREFIX, player, "tanlovini qildi." }''', r'''{ PREFIX, player, "сделал выбор." }''')
e(f, r'''"Both players rocked, papered, and scissored! (ew)"''', r'''"Ikkala o'yinchi ham tanlovini qildi!"''', r'''"Оба игрока сделали выбор!"''')
e(f, r'''"It's a tie! Let's go again!"''', r'''"Durang! Yana bir bor!"''', r'''"Ничья! Ещё раз!"''')
e(f, r'''"Results:",''', r'''"Natija:",''', r'''"Результат:",''')
e(f, r'''      guard,
      "picked",''', r'''      guard,
      "tanladi:",''', r'''      guard,
      "выбрал:",''')
e(f, r'''      "and",
      prisoner,
      "picked",''', r'''      "va",
      prisoner,
      "tanladi:",''', r'''      "и",
      prisoner,
      "выбрал:",''')
e(f, r'''0 => "Rock",''', r'''0 => "Tosh",''', r'''0 => "Камень",''')
e(f, r'''1 => "Paper",''', r'''1 => "Qog'oz",''', r'''1 => "Бумага",''')
e(f, r'''2 => "Scissors",''', r'''2 => "Qaychi",''', r'''2 => "Ножницы",''')
e(f, r'''_ => "Unknown"''', r'''_ => "Noma'lum"''', r'''_ => "Неизвестно"''')

f = L+'LastRequest/RaceLocale.cs'
e(f, r'''$"Type {ChatColors.Blue}!endrace{ChatColors.White} to set the end point!"''', r'''$"Marra nuqtasini belgilash uchun {ChatColors.Blue}!endrace{ChatColors.White} yoz!"''', r'''$"Напиши {ChatColors.Blue}!endrace{ChatColors.White}, чтобы поставить финиш!"''')
e(f, r'''"is racing you. Pay attention to where they set the end point!"''', r'''"sen bilan poyga qilmoqda. Marra qayerda belgilanishiga e'tibor ber!"''', r'''"устраивает с тобой гонку. Следи, где он поставит финиш!"''')
e(f, r'''$"{ChatColors.Red}You must be in a race {ChatColors.Blue + "!lr" + ChatColors.Red} to use this."''', r'''$"{ChatColors.Red}Buning uchun poyga {ChatColors.Blue + "!lr" + ChatColors.Red} da bo'lishing kerak."''', r'''$"{ChatColors.Red}Для этого нужно быть в гонке {ChatColors.Blue + "!lr" + ChatColors.Red}."''')
e(f, r'''"You must be in the pending state to use this command."''', r'''"Bu buyruq faqat poyga boshlanishidan oldin ishlaydi."''', r'''"Эта команда работает только до начала гонки."''')

# ---------- Mute ----------
f = L+'Mute/WardenPeaceLocale.cs'
e(f, r'''$" {ChatColors.DarkBlue}Voice>"''', r'''$" {ChatColors.DarkBlue}Ovoz>"''', r'''$" {ChatColors.DarkBlue}Голос>"''')
e(f, r'''"An admin enacted peace for",''', r'''"Admin sukunat e'lon qildi:",''', r'''"Админ объявил тишину на",''')
e(f, r'''"second" + (seconds == 1 ? "" : "s") + "."''', r'''"soniya."''', r'''"сек."''')
e(f, r'''PREFIX, "The warden enacted peace for", seconds, "seconds."''', r'''PREFIX, "Nazoratchi sukunat e'lon qildi:", seconds, "soniya."''', r'''PREFIX, "Командир объявил тишину на", seconds, "сек."''')
e(f, r'''"Peace was enacted for",''', r'''"Sukunat e'lon qilindi:",''', r'''"Объявлена тишина на",''')
e(f, r'''{ PREFIX, CsTeam.CounterTerrorist, "were unmuted." }''', r'''{ PREFIX, CsTeam.CounterTerrorist, "endi gapira oladi." }''', r'''{ PREFIX, CsTeam.CounterTerrorist, "снова могут говорить." }''')
e(f, r'''{ PREFIX, CsTeam.Terrorist, "were unmuted." }''', r'''{ PREFIX, CsTeam.Terrorist, "endi gapira oladi." }''', r'''{ PREFIX, CsTeam.Terrorist, "снова могут говорить." }''')
e(f, r'''"You are currently muted."''', r'''"Hozir mikrofoning o'chirilgan."''', r'''"Сейчас у тебя отключён микрофон."''')
e(f, r'''$"Peace is currently active. {ChatColors.Red}You should only be talking if absolutely necessary!"''', r'''$"Hozir sukunat. {ChatColors.Red}Faqat juda zarur bo'lsa gapir!"''', r'''$"Сейчас тишина. {ChatColors.Red}Говори только если это действительно нужно!"''')
e(f, r'''$"{ChatColors.Red}You are dead and cannot speak."''', r'''$"{ChatColors.Red}Sen o'liksan va gapira olmaysan."''', r'''$"{ChatColors.Red}Ты мёртв и не можешь говорить."''')
e(f, r'''"You are dead.",''', r'''"Sen o'liksan.",''', r'''"Ты мёртв.",''')
e(f, r'''$"{ChatColors.Red}You should only be talking if absolutely necessary!"''', r'''$"{ChatColors.Red}Faqat juda zarur bo'lsa gapir!"''', r'''$"{ChatColors.Red}Говори только если это действительно нужно!"''')
e(f, r'''"Peace is currently active."''', r'''"Hozir sukunat."''', r'''"Сейчас тишина."''')

# ---------- RTD ----------
f = L+'RTD/AutoRTDLocale.cs'
e(f, r'''"Toggling Auto-RTD is not supported on this server."''', r'''"Bu serverda Auto-RTD ni o'zgartirib bo'lmaydi."''', r'''"На этом сервере нельзя переключать Auto-RTD."''')
e(f, r'''ChatColors.Grey + "You",
      enabled ? ChatColors.Green + "enabled" : ChatColors.Red + "disabled",
      ChatColors.Grey + "Auto-RTD."''', r'''ChatColors.Grey + "Auto-RTD:",
      enabled ? ChatColors.Green + "yoqildi" : ChatColors.Red + "o'chirildi",
      ChatColors.Grey + "."''', r'''ChatColors.Grey + "Auto-RTD:",
      enabled ? ChatColors.Green + "включён" : ChatColors.Red + "выключен",
      ChatColors.Grey + "."''')
f = L+'RTD/RTDLocale.cs'
e(f, r'''"You rolled " + ChatColors.BlueGrey''', r'''"Senga tushdi: " + ChatColors.BlueGrey''', r'''"Тебе выпало: " + ChatColors.BlueGrey''')
e(f, r'''"You already rolled " + ChatColors.Red''', r'''"Sen allaqachon tashlagansan: " + ChatColors.Red''', r'''"Ты уже бросал: " + ChatColors.Red''')
e(f, r'''"You can only roll when round ends or while dead."''', r'''"Faqat raund oxirida yoki o'lganingda tashlash mumkin."''', r'''"Бросать можно только в конце раунда или когда ты мёртв."''')
e(f, r'''"Rolling is disabled."''', r'''"Tashlash o'chirilgan."''', r'''"Броски отключены."''')
e(f, r'''"won the jackpot of ",''', r'''"jekpotni yutdi: ",''', r'''"выиграл джекпот: ",''')
e(f, r'''" credits!"''', r'''" kredit!"''', r'''" кредитов!"''')

# ---------- Rebel ----------
f = L+'Rebel/C4Locale.cs'
e(f, r'''$"You picked up a {ChatColors.Red}Jihad C4{ChatColors.Grey}!"''', r'''$"Sen {ChatColors.Red}portlovchi C4{ChatColors.Grey} ni olding!"''', r'''$"Ты подобрал {ChatColors.Red}взрывчатку C4{ChatColors.Grey}!"''')
e(f, r'''$"You received a {ChatColors.Red}Jihad C4{ChatColors.Grey}!"''', r'''$"Senga {ChatColors.Red}portlovchi C4{ChatColors.Grey} berildi!"''', r'''$"Тебе выдана {ChatColors.Red}взрывчатка C4{ChatColors.Grey}!"''')
e(f, r'''$"To detonate it, hold it out and press {ChatColors.Yellow + "E" + ChatColors.Grey}."''', r'''$"Portlatish uchun uni qo'lga ol va {ChatColors.Yellow + "E" + ChatColors.Grey} ni bos."''', r'''$"Чтобы взорвать, возьми её в руки и нажми {ChatColors.Yellow + "E" + ChatColors.Grey}."''')
f = L+'Rebel/RebelLocale.cs'
e(f, r'''$" {ChatColors.DarkBlue}Game>"''', r'''$" {ChatColors.DarkBlue}O'yin>"''', r'''$" {ChatColors.DarkBlue}Игра>"''')
e(f, r'''"You are no longer red."''', r'''"Sen endi isyonchi emassan."''', r'''"Ты больше не бунтарь."''')

# ---------- SpecialDay ----------
f = L+'SpecialDay/FogDayLocale.cs'
e(f, r'''SoloDayLocale("Fog War",
  "A heavy fog is creeping in...", "Your visibility will be gone soon.",
  "Fog expands periodically — Stay alert.")''', r'''SoloDayLocale("Tuman urushi",
  "Qalin tuman yaqinlashmoqda...", "Tez orada hech narsa ko'rinmay qoladi.",
  "Tuman vaqti-vaqti bilan kengayadi — hushyor bo'l.")''', r'''SoloDayLocale("Туманная война",
  "Надвигается густой туман...", "Скоро видимость пропадёт.",
  "Туман периодически расширяется — будь начеку.")''')
e(f, r'''"Fog's rolling in!",''', r'''"Tuman kelmoqda!",''', r'''"Туман надвигается!",''')
e(f, r'''"Match Starts in 15 seconds."''', r'''"O'yin 15 soniyadan keyin boshlanadi."''', r'''"Бой начнётся через 15 сек."''')
e(f, r'''"Fog is expanding."''', r'''"Tuman kengaymoqda."''', r'''"Туман расширяется."''')
e(f, r'''"Fog will start expanding in",''', r'''"Tuman kengayishiga",''', r'''"Туман начнёт расширяться через",''')
e(f, r'''"second" + (seconds == 1 ? "" : "s")''', r'''"soniya qoldi"''', r'''"сек."''')

f = L+'SpecialDay/GunDayLocale.cs'
e(f, r'''SoloDayLocale("Gun Game",
  "Free for all! Kill players to progress through the weapons.",
  "Players will randomly respawn upon death.",
  "If you get knifed you lose some progress!",
  "Knifing someone lets you skip a gun!")''', r'''SoloDayLocale("Gun Game",
  "Hamma hammaga qarshi! Qurollar bo'ylab oldinga siljish uchun o'ldir.",
  "O'lgandan keyin tasodifiy joyda tirilasan.",
  "Seni pichoq bilan o'ldirishsa, bir pog'ona orqaga ketasan!",
  "Pichoq bilan o'ldirsang, bitta qurolni o'tkazib yuborasan!")''', r'''SoloDayLocale("Gun Game",
  "Все против всех! Убивай, чтобы продвигаться по оружию.",
  "После смерти возрождаешься в случайном месте.",
  "Если тебя убьют ножом — откатишься назад!",
  "Убийство ножом пропускает одно оружие!")''')
e(f, r'''"You were demoted due to dying to yourself."''', r'''"O'zingni o'ldirganing uchun orqaga tushding."''', r'''"Ты откатился назад из-за самоубийства."''')
e(f, r'''"You were demoted due to getting knifed."''', r'''"Seni pichoq bilan o'ldirishgani uchun orqaga tushding."''', r'''"Ты откатился назад: тебя убили ножом."''')
e(f, r'''PREFIX, "Promoted to", weapon + ".", ChatColors.Green + "LAST WEAPON!"''', r'''PREFIX, "Yangi qurol:", weapon + ".", ChatColors.Green + "OXIRGI QUROL!"''', r'''PREFIX, "Новое оружие:", weapon + ".", ChatColors.Green + "ПОСЛЕДНЕЕ ОРУЖИЕ!"''')
e(f, r'''      "Promoted to",
      weapon + ".",
      weaponsLeft,
      "weapons left."''', r'''      "Yangi qurol:",
      weapon + ".",
      "Qolgan qurollar:",
      weaponsLeft''', r'''      "Новое оружие:",
      weapon + ".",
      "Осталось оружий:",
      weaponsLeft''')
e(f, r'''"is on the last weapon!",''', r'''"oxirgi qurolda!",''', r'''"на последнем оружии!",''')
e(f, r'''ChatColors.LightRed + "Watch out!"''', r'''ChatColors.LightRed + "Ehtiyot bo'ling!"''', r'''ChatColors.LightRed + "Берегитесь!"''')
e(f, r'''{ PREFIX, player, "won the game!" }''', r'''{ PREFIX, player, "o'yinda g'olib bo'ldi!" }''', r'''{ PREFIX, player, "выиграл игру!" }''')

f = L+'SpecialDay/HNSDayLocale.cs'
e(f, r'''TeamDayLocale("Hide and Seek",
  "CTs must hide while the Ts seek!", "Ts have increased HP!")''', r'''TeamDayLocale("Berkinmachoq",
  "Qo'riqchilar yashirinadi, mahbuslar qidiradi!", "Mahbuslarning sog'lig'i oshirilgan!")''', r'''TeamDayLocale("Прятки",
  "Охрана прячется, заключённые ищут!", "У заключённых больше здоровья!")''')
e(f, r'''{ PREFIX, "Today is", Name, ", stay in the armory!" }''', r'''{ PREFIX, "Bugun", Name, ", qurolxonada qoling!" }''', r'''{ PREFIX, "Сегодня", Name, ", оставайтесь в оружейной!" }''')
e(f, r'''"Ready or not, here they come!"''', r'''"Tayyormisiz-yo'qmi, ular kelyapti!"''', r'''"Готовы или нет — они идут!"''')
e(f, r'''      Name,
      "begins in",
      seconds,
      "second" + (seconds == 1 ? "" : "s") + "."''', r'''      Name,
      "boshlanishiga",
      seconds,
      "soniya."''', r'''      Name,
      "начнётся через",
      seconds,
      "сек."''')
e(f, r'''      "You will be vulnerable to damage in",
      seconds,
      "second" + (seconds == 1 ? "" : "s") + "."''', r'''      "Senga zarar o'tishiga",
      seconds,
      "soniya."''', r'''      "Ты станешь уязвим через",
      seconds,
      "сек."''')

f = L+'SpecialDay/InfectionDayLocale.cs'
e(f, r'''TeamDayLocale("Infection",
  "CTs are infected and try to infect Ts!",
  "Ts can scavenge for any guns, but CTs can only use pistols!")''', r'''TeamDayLocale("Infeksiya",
  "Qo'riqchilar zararlangan va mahbuslarni yuqtirishga harakat qiladi!",
  "Mahbuslar istalgan qurolni topishi mumkin, qo'riqchilar faqat to'pponcha ishlatadi!")''', r'''TeamDayLocale("Заражение",
  "Охрана заражена и пытается заразить заключённых!",
  "Заключённые могут искать любое оружие, охрана — только пистолеты!")''')
e(f, r'''      Name,
      "ended.",
      (winner''', r'''      Name,
      "tugadi.",
      (winner''', r'''      Name,
      "окончено.",
      (winner''')
e(f, r'''(winner == CsTeam.CounterTerrorist ? "Zombies" : "Prisoners"),
      "won!"''', r'''(winner == CsTeam.CounterTerrorist ? "Zombilar" : "Mahbuslar"),
      "g'olib!"''', r'''(winner == CsTeam.CounterTerrorist ? "Зомби" : "Заключённые"),
      "победили!"''')
e(f, r'''$"{ChatColors.Red}You were {ChatColors.DarkRed}infected{ChatColors.Red}!"''', r'''$"{ChatColors.Red}Senga {ChatColors.DarkRed}yuqtirishdi{ChatColors.Red}!"''', r'''$"{ChatColors.Red}Тебя {ChatColors.DarkRed}заразили{ChatColors.Red}!"''')
e(f, r'''$"{ChatColors.Red}You were {ChatColors.DarkRed}infected{ChatColors.Red} by",''', r'''$"{ChatColors.Red}Senga {ChatColors.DarkRed}yuqtirdi{ChatColors.Red}:",''', r'''$"{ChatColors.Red}Тебя {ChatColors.DarkRed}заразил{ChatColors.Red}",''')
e(f, r'''$"was {ChatColors.DarkRed}infected{ChatColors.Default}! {ChatColors.Red}Watch out!"''', r'''$"{ChatColors.DarkRed}zararlandi{ChatColors.Default}! {ChatColors.Red}Ehtiyot bo'ling!"''', r'''$"{ChatColors.DarkRed}заражён{ChatColors.Default}! {ChatColors.Red}Берегитесь!"''')
e(f, r'''      "Damage will be enabled for the",
      CsTeam.Terrorist,
      "team in",
      seconds,
      "seconds."''', r'''      "Zarar yoqilishiga",
      seconds,
      "soniya qoldi, jamoa:",
      CsTeam.Terrorist''', r'''      "Урон включится через",
      seconds,
      "сек. для команды",
      CsTeam.Terrorist''')

f = L+'SpecialDay/SDLocale.cs'
e(f, r'''$" {ChatColors.DarkBlue}Game>"''', r'''$" {ChatColors.DarkBlue}O'yin>"''', r'''$" {ChatColors.DarkBlue}Игра>"''')
e(f, r'''"The current day is",''', r'''"Hozirgi kun:",''', r'''"Сейчас идёт:",''')
e(f, r'''ChatColors.Grey + "is not a valid special day."''', r'''ChatColors.Grey + "— bunday maxsus kun yo'q."''', r'''ChatColors.Grey + "— такого особого дня нет."''')
e(f, r'''      "You must wait",
      rounds,
      "more round" + (rounds == 1 ? "" : "s")
      + " before starting a special day."''', r'''      "Maxsus kunni boshlash uchun yana",
      rounds,
      "raund kutish kerak."''', r'''      "Особый день можно начать через",
      rounds,
      "раунд(а/ов)."''')
e(f, r'''      "You must start a special day within",
      maxTime,
      "second" + (maxTime == 1 ? "" : "s") + " of round start."''', r'''      "Maxsus kunni raund boshlanganidan keyin",
      maxTime,
      "soniya ichida boshlash kerak."''', r'''      "Особый день нужно начать в первые",
      maxTime,
      "сек. раунда."''')
e(f, r'''"You cannot call this special day:"''', r'''"Bu maxsus kunni boshlay olmaysan:"''', r'''"Ты не можешь начать этот особый день:"''')

for f in [L+'SpecialDay/SoloDayLocale.cs', L+'SpecialDay/TeamDayLocale.cs']:
    e(f, r'''=> new SimpleView { PREFIX, Name, "ended." };''', r'''=> new SimpleView { PREFIX, Name, "tugadi." };''', r'''=> new SimpleView { PREFIX, Name, "окончен." };''')
    e(f, r'''new SimpleView { PREFIX, Name, "begins now!" }''', r'''new SimpleView { PREFIX, Name, "boshlandi!" }''', r'''new SimpleView { PREFIX, Name, "начался!" }''')
    e(f, r'''        Name,
        "begins in",
        seconds,
        "seconds."''', r'''        Name,
        "boshlanishiga",
        seconds,
        "soniya."''', r'''        Name,
        "начнётся через",
        seconds,
        "сек."''')
    e(f, r'''{ "Today is a" + (Name[0].IsVowel() ? "n" : ""), Name, "day!" }''', r'''{ "Bugun maxsus kun:", Name + "!" }''', r'''{ "Сегодня особый день:", Name + "!" }''')
    e(f, r'''      Name,
      "ended.",''', r'''      Name,
      "tugadi.",''', r'''      Name,
      "окончен.",''')
    e(f, r'''      "won!"
    };''', r'''      "g'olib!"
    };''', r'''      "победил!"
    };''')
e(L+'SpecialDay/SoloDayLocale.cs', r'''{ PREFIX, Name, "ended. No one won!" }''', r'''{ PREFIX, Name, "tugadi. Hech kim yutmadi!" }''', r'''{ PREFIX, Name, "окончен. Никто не победил!" }''')

f = L+'SpecialDay/SpeedrunDayLocale.cs'
e(f, r'''SoloDayLocale("Speedrunners",
    $"Follow the {ChatColors.Blue}blue{ChatColors.Default} player!",
    "They will run to a spot on the map.",
    $"Each round, the {ChatColors.Red}slowest players{ChatColors.Grey} to reach the target will be eliminated.")''', r'''SoloDayLocale("Tezkor yuguruvchilar",
    $"{ChatColors.Blue}Ko'k{ChatColors.Default} o'yinchining ortidan yugur!",
    "U xaritadagi biror nuqtaga yuguradi.",
    $"Har raundda nuqtaga {ChatColors.Red}eng sekin yetganlar{ChatColors.Grey} chiqib ketadi.")''', r'''SoloDayLocale("Спидраннеры",
    $"Беги за {ChatColors.Blue}синим{ChatColors.Default} игроком!",
    "Он побежит к точке на карте.",
    $"Каждый раунд {ChatColors.Red}самые медленные{ChatColors.Grey} выбывают.")''')
e(f, r'''"Round over! The next one will start shortly."''', r'''"Raund tugadi! Keyingisi tez orada boshlanadi."''', r'''"Раунд окончен! Следующий скоро начнётся."''')
e(f, r'''"Not enough players reached the goal this round!"''', r'''"Bu raundda maqsadga yetarlicha o'yinchi yetmadi!"''', r'''"В этом раунде до цели добежало слишком мало игроков!"''')
e(f, r'''"Going off of distance to target for those who didn't."''', r'''"Yetmaganlar maqsadgacha bo'lgan masofa bo'yicha baholanadi."''', r'''"Для остальных считаем расстояние до цели."''')
e(f, r'''"No one was eliminated this round!"''', r'''"Bu raundda hech kim chiqib ketmadi!"''', r'''"В этом раунде никто не выбыл!"''')
e(f, r'''{ PREFIX, "You are the speedrunner!" }''', r'''{ PREFIX, "Sen yo'l ko'rsatuvchisan!" }''', r'''{ PREFIX, "Ты — спидраннер!" }''')
e(f, r'''PREFIX, "You have", seconds, "seconds to run to a spot to set the goal."''', r'''PREFIX, "Maqsad nuqtasiga yugurish uchun", seconds, "soniya vaqting bor."''', r'''PREFIX, "У тебя", seconds, "сек., чтобы добежать до точки цели."''')
e(f, r'''          $"Round{ChatColors.Yellow}#{round}{ChatColors.Grey} begins! The slowest",
          "player to reach the goal will be eliminated!"''', r'''          $"{ChatColors.Yellow}#{round}{ChatColors.Grey}-raund boshlandi! Maqsadga eng sekin",
          "yetgan o'yinchi chiqib ketadi!"''', r'''          $"Раунд {ChatColors.Yellow}#{round}{ChatColors.Grey} начался! Самый медленный",
          "игрок выбывает!"''')
e(f, r'''{ PREFIX, "You have", seconds, "seconds to reach the goal!" }''', r'''{ PREFIX, "Maqsadga yetish uchun", seconds, "soniya vaqting bor!" }''', r'''{ PREFIX, "У тебя", seconds, "сек., чтобы добежать до цели!" }''')
e(f, r'''        $"Round {ChatColors.Yellow}#{round}{ChatColors.Grey} begins! The slowest",
        eliminationCount, "players to reach the goal will be eliminated!"''', r'''        $"{ChatColors.Yellow}#{round}{ChatColors.Grey}-raund boshlandi! Maqsadga eng sekin yetgan",
        eliminationCount, "ta o'yinchi chiqib ketadi!"''', r'''        $"Раунд {ChatColors.Yellow}#{round}{ChatColors.Grey} начался! Выбывают самые медленные:",
        eliminationCount, "игрок(а/ов)!"''')
e(f, r'''{ PREFIX, "You have", seconds, "seconds to reach the goal." }''', r'''{ PREFIX, "Maqsadga yetish uchun", seconds, "soniya vaqting bor." }''', r'''{ PREFIX, "У тебя", seconds, "сек., чтобы добежать до цели." }''')
e(f, r'''PREFIX, "You have", seconds, "seconds left to run to a spot!"''', r'''PREFIX, "Nuqtaga yugurish uchun", seconds, "soniya qoldi!"''', r'''PREFIX, "Осталось", seconds, "сек., чтобы добежать до точки!"''')
e(f, r'''PREFIX, player, "is the speedrunner! Follow them closely!"''', r'''PREFIX, player, "— yo'l ko'rsatuvchi! Uning ortidan yuguring!"''', r'''PREFIX, player, "— спидраннер! Бегите за ним!"''')
e(f, r'''      "The original speedrunner left, so",
      player,
      "is now the speedrunner."''', r'''      "Yo'l ko'rsatuvchi chiqib ketdi, endi yo'l ko'rsatuvchi:",
      player,
      ""''', r'''      "Спидраннер вышел, теперь спидраннер —",
      player,
      ""''')
e(f, r'''      "The original speedrunner isn't moving, so",
      player,
      "is now the speedrunner."''', r'''      "Yo'l ko'rsatuvchi qimirlamayapti, endi yo'l ko'rsatuvchi:",
      player,
      ""''', r'''      "Спидраннер стоит на месте, теперь спидраннер —",
      player,
      ""''')
e(f, r'''1 => ChatColors.Green + "FIRST",''', r'''1 => ChatColors.Green + "BIRINCHI",''', r'''1 => ChatColors.Green + "ПЕРВОЕ",''')
e(f, r'''2 => ChatColors.LightYellow + "Second",''', r'''2 => ChatColors.LightYellow + "Ikkinchi",''', r'''2 => ChatColors.LightYellow + "Второе",''')
e(f, r'''3 => ChatColors.BlueGrey + "3rd",''', r'''3 => ChatColors.BlueGrey + "Uchinchi",''', r'''3 => ChatColors.BlueGrey + "Третье",''')
e(f, r'''_ => ChatColors.Grey + "" + position + "th"''', r'''_ => ChatColors.Grey + "" + position + "-"''', r'''_ => ChatColors.Grey + "" + position + "-е"''')
e(f, r'''        "finished in",
        -time,
        "seconds.",
        place,
        "place" + (position == 1 ? "!" : ".")''', r'''        "marraga yetdi:",
        -time,
        "soniya.",
        place,
        "o'rin" + (position == 1 ? "!" : ".")''', r'''        "финишировал за",
        -time,
        "сек.",
        place,
        "место" + (position == 1 ? "!" : ".")''')
e(f, r'''      "was",
      time,
      "units away from the goal,",
      place,
      "place."''', r'''      "maqsaddan",
      time,
      "birlik uzoqda,",
      place,
      "o'rin."''', r'''      "был в",
      time,
      "ед. от цели,",
      place,
      "место."''')
e(f, r'''{ PREFIX, player, "was eliminated!" }''', r'''{ PREFIX, player, "chiqib ketdi!" }''', r'''{ PREFIX, player, "выбыл!" }''')
e(f, r'''"Stay still to start the round sooner..."''', r'''"Raund tezroq boshlanishi uchun qimirlamay tur..."''', r'''"Стой на месте, чтобы раунд начался быстрее..."''')
e(f, r'''{ PREFIX, player, "won the game!" }''', r'''{ PREFIX, player, "o'yinda g'olib bo'ldi!" }''', r'''{ PREFIX, player, "выиграл игру!" }''')
e(f, r'''      "beat the best time with",
      time,
      $"seconds! {ChatColors.Green}FIRST PLACE{ChatColors.Default}!"''', r'''      "eng yaxshi vaqtni yangiladi:",
      time,
      $"soniya! {ChatColors.Green}BIRINCHI O'RIN{ChatColors.Default}!"''', r'''      "побил лучшее время:",
      time,
      $"сек.! {ChatColors.Green}ПЕРВОЕ МЕСТО{ChatColors.Default}!"''')
e(f, r'''        PREFIX, "No one on", team,
        "reached the goal. Eliminating one player on each time."''', r'''        PREFIX, "Jamoadan hech kim maqsadga yetmadi:", team,
        ". Har safar bittadan o'yinchi chiqariladi."''', r'''        PREFIX, "Никто из команды", team,
        "не добежал до цели. Выбывает по одному игроку."''')
e(f, r'''{ PREFIX, "Randomly selected the path from", player, "." }''', r'''{ PREFIX, "Tasodifiy tanlangan yo'l:", player, "." }''', r'''{ PREFIX, "Случайно выбран путь игрока", player, "." }''')

f = L+'SpecialDay/WardayInstanceLocale.cs'
e(f, r'''TeamDayLocale("Warday",
  "CTs vs Ts! CTs pick a room, Ts must go fight them!",
  "CTs MUST stay in the same room until expansion time.")''', r'''TeamDayLocale("Urush kuni",
  "Qo'riqchilar mahbuslarga qarshi! Qo'riqchilar xona tanlaydi, mahbuslar ularga hujum qiladi!",
  "Qo'riqchilar kengayish vaqtigacha shu xonada qolishi SHART.")''', r'''TeamDayLocale("Вардей",
  "Охрана против заключённых! Охрана выбирает комнату, заключённые идут штурмовать!",
  "Охрана ОБЯЗАНА оставаться в комнате до времени расширения.")''')
e(f, r'''{ PREFIX, "CTs can expand now!" }''', r'''{ PREFIX, "Qo'riqchilar endi kengayishi mumkin!" }''', r'''{ PREFIX, "Охрана может выходить из комнаты!" }''')
e(f, r'''{ PREFIX, "CTs can expand in", seconds, "seconds." }''', r'''{ PREFIX, "Qo'riqchilar kengayishiga", seconds, "soniya." }''', r'''{ PREFIX, "Охрана сможет выйти через", seconds, "сек." }''')
e(f, r'''"They will be given replenished health, armor, and speed."''', r'''"Ularga sog'lik, zirh va tezlik qayta beriladi."''', r'''"Им восстановят здоровье, броню и скорость."''')

# ---------- Warden ----------
f = L+'Warden/WardenCmdChickenLocale.cs'
e(f, r'''ChatColors.Blue + "The warden" + ChatColors.Grey + " spawned a chicken."''', r'''ChatColors.Blue + "Nazoratchi" + ChatColors.Grey + " tovuq chiqardi."''', r'''ChatColors.Blue + "Командир" + ChatColors.Grey + " заспавнил курицу."''')
e(f, r'''ChatColors.Red + "Failed to spawn a chicken."''', r'''ChatColors.Red + "Tovuq chiqarib bo'lmadi."''', r'''ChatColors.Red + "Не удалось создать курицу."''')
e(f, r'''"Too many chickens."''', r'''"Tovuqlar juda ko'p."''', r'''"Слишком много куриц."''')

f = L+'Warden/WardenCmdCountLocale.cs'
e(f, r'''      ChatColors.Grey + "There " + (prisoners == 1 ? "is" : " are"),
      prisoners,
      ChatColors.Grey + "prisoner" + (prisoners == 1 ? "" : "s")
      + " in the marker."''', r'''      ChatColors.Grey + "Belgi ichidagi mahbuslar:",
      prisoners''', r'''      ChatColors.Grey + "Заключённых в маркере:",
      prisoners''')
e(f, r'''      "You must wait",
      seconds,
      "seconds before counting prisoners."''', r'''      "Mahbuslarni sanash uchun",
      seconds,
      "soniya kut."''', r'''      "Подожди",
      seconds,
      "сек., прежде чем считать заключённых."''')
e(f, r'''"No marker set."''', r'''"Belgi qo'yilmagan."''', r'''"Маркер не установлен."''')

f = L+'Warden/WardenCmdMarkerLocale.cs'
e(f, r'''"Marker customization is not supported on this server."''', r'''"Bu serverda belgini sozlab bo'lmaydi."''', r'''"На этом сервере нельзя настраивать маркер."''')
e(f, r'''$"Changed marker type to {type}."''', r'''$"Belgi shakli o'zgartirildi: {type}."''', r'''$"Форма маркера изменена: {type}."''')
e(f, r'''$"Changed marker color to {color}."''', r'''$"Belgi rangi o'zgartirildi: {color}."''', r'''$"Цвет маркера изменён: {color}."''')

f = L+'Warden/WardenCmdOpenLocale.cs'
e(f, r'''      "You must wait",
      seconds,
      "seconds before opening the cells."''', r'''      "Kameralarni ochish uchun",
      seconds,
      "soniya kut."''', r'''      "Подожди",
      seconds,
      "сек., прежде чем открывать камеры."''')
e(f, r'''"Cells are already opened."''', r'''"Kameralar allaqachon ochiq."''', r'''"Камеры уже открыты."''')
e(f, r'''$"{ChatColors.Blue}The warden {ChatColors.Default}opened the cells."''', r'''$"{ChatColors.Blue}Nazoratchi {ChatColors.Default}kameralarni ochdi."''', r'''$"{ChatColors.Blue}Командир {ChatColors.Default}открыл камеры."''')
e(f, r'''{ WardenLocale.PREFIX, player, "opened the cells." }''', r'''{ WardenLocale.PREFIX, player, "kameralarni ochdi." }''', r'''{ WardenLocale.PREFIX, player, "открыл камеры." }''')
e(f, r'''ChatColors.Grey + "Cells were auto-opened."''', r'''ChatColors.Grey + "Kameralar avtomatik ochildi."''', r'''ChatColors.Grey + "Камеры открылись автоматически."''')
e(f, r'''      "Detected",
      prisoners,
      "prisoner" + (prisoners == 1 ? "" : "s") + " still in cells, opening..."''', r'''      "Kamerada hali",
      prisoners,
      "mahbus bor, ochilmoqda..."''', r'''      "В камерах ещё заключённых:",
      prisoners,
      ", открываем..."''')
e(f, r'''      ChatColors.Grey + "Detected",
      prisoners,
      "prisoner" + (prisoners == 1 ? "" : "s") + " still in cells..."''', r'''      ChatColors.Grey + "Kamerada hali",
      prisoners,
      "mahbus bor..."''', r'''      ChatColors.Grey + "В камерах ещё заключённых:",
      prisoners''')
e(f, r'''"Failed to open the cells."''', r'''"Kameralarni ochib bo'lmadi."''', r'''"Не удалось открыть камеры."''')

f = L+'Warden/WardenCmdRollLocale.cs'
e(f, r'''WardenLocale.PREFIX, "warden has rolled", roll, "!"''', r'''WardenLocale.PREFIX, "Nazoratchi tashladi:", roll, "!"''', r'''WardenLocale.PREFIX, "Командир выбросил", roll, "!"''')

f = L+'Warden/WardenCmdSoccerLocale.cs'
e(f, r'''ChatColors.Blue + "The warden" + ChatColors.Grey
      + " spawned a soccer ball."''', r'''ChatColors.Blue + "Nazoratchi" + ChatColors.Grey
      + " futbol to'pi chiqardi."''', r'''ChatColors.Blue + "Командир" + ChatColors.Grey
      + " заспавнил футбольный мяч."''')
e(f, r'''ChatColors.Red + "Failed to spawn a soccer ball."''', r'''ChatColors.Red + "To'p chiqarib bo'lmadi."''', r'''ChatColors.Red + "Не удалось создать мяч."''')
e(f, r'''"Too many soccer balls."''', r'''"To'plar juda ko'p."''', r'''"Слишком много мячей."''')

f = L+'Warden/WardenLocale.cs'
e(f, r'''$" {ChatColors.DarkBlue}Guard>"''', r'''$" {ChatColors.DarkBlue}Qo'riqchi>"''', r'''$" {ChatColors.DarkBlue}Охрана>"''')
e(f, r'''$"The previous command stands for 10 seconds."''', r'''$"Oldingi buyruq yana 10 soniya amal qiladi."''', r'''$"Предыдущий приказ действует ещё 10 сек."''')
e(f, r'''$"Picking a warden shortly, type {ChatColors.BlueGrey}!warden{ChatColors.Grey} to enter the queue."''', r'''$"Tez orada nazoratchi tanlanadi, navbatga turish uchun {ChatColors.BlueGrey}!warden{ChatColors.Grey} yoz."''', r'''$"Скоро будет выбран командир, напиши {ChatColors.BlueGrey}!warden{ChatColors.Grey}, чтобы встать в очередь."''')
e(f, r'''$"No one in queue. Next guard to {ChatColors.BlueGrey}!warden{ChatColors.Grey} will become warden."''', r'''$"Navbatda hech kim yo'q. {ChatColors.BlueGrey}!warden{ChatColors.Grey} yozgan birinchi qo'riqchi nazoratchi bo'ladi."''', r'''$"В очереди никого. Первый охранник, написавший {ChatColors.BlueGrey}!warden{ChatColors.Grey}, станет командиром."''')
e(f, r'''$"It is now a freeday! CTs must pursue {ChatColors.BlueGrey}!warden{ChatColors.Grey}."''', r'''$"Hozir erkin kun! Qo'riqchilar {ChatColors.BlueGrey}!warden{ChatColors.Grey} yozishi kerak."''', r'''$"Сейчас фридей! Охрана должна взять {ChatColors.BlueGrey}!warden{ChatColors.Grey}."''')
e(f, r'''"The warden left the game."''', r'''"Nazoratchi o'yindan chiqib ketdi."''', r'''"Командир вышел из игры."''')
e(f, r'''$"The warden {ChatColors.Red}died{ChatColors.Grey}. It is a freeday!"''', r'''$"Nazoratchi {ChatColors.Red}o'ldi{ChatColors.Grey}. Erkin kun!"''', r'''$"Командир {ChatColors.Red}погиб{ChatColors.Grey}. Фридей!"''')
e(f, r'''$"CTs must pursue {ChatColors.BlueGrey}!warden{ChatColors.Grey}."''', r'''$"Qo'riqchilar {ChatColors.BlueGrey}!warden{ChatColors.Grey} yozishi kerak."''', r'''$"Охрана должна взять {ChatColors.BlueGrey}!warden{ChatColors.Grey}."''')
e(f, r'''$"Type {ChatColors.BlueGrey}!warden{ChatColors.Grey} to become the warden."''', r'''$"Nazoratchi bo'lish uchun {ChatColors.BlueGrey}!warden{ChatColors.Grey} yoz."''', r'''$"Напиши {ChatColors.BlueGrey}!warden{ChatColors.Grey}, чтобы стать командиром."''')
e(f, r'''$"You {ChatColors.White}joined {ChatColors.Grey}the warden raffle."''', r'''$"Sen nazoratchi tanloviga {ChatColors.White}qo'shilding{ChatColors.Grey}."''', r'''$"Ты {ChatColors.White}записался {ChatColors.Grey}в розыгрыш командира."''')
e(f, r'''$"You {ChatColors.Red}left {ChatColors.Grey}the warden raffle."''', r'''$"Sen nazoratchi tanlovidan {ChatColors.Red}chiqding{ChatColors.Grey}."''', r'''$"Ты {ChatColors.Red}вышел {ChatColors.Grey}из розыгрыша командира."''')
e(f, r'''$"{ChatColors.LightRed}You are not the warden."''', r'''$"{ChatColors.LightRed}Sen nazoratchi emassan."''', r'''$"{ChatColors.LightRed}Ты не командир."''')
e(f, r'''"The fire command failed for some unknown reason..."''', r'''"Nazoratchini olib tashlab bo'lmadi, noma'lum xato..."''', r'''"Не удалось снять командира, неизвестная ошибка..."''')
e(f, r'''"Toggling Auto-Warden is not supported on this server."''', r'''"Bu serverda Auto-Warden ni o'zgartirib bo'lmaydi."''', r'''"На этом сервере нельзя переключать Auto-Warden."''')
e(f, r'''PREFIX, player, "resigned from warden.", COMMAND_STANDS''', r'''PREFIX, player, "nazoratchilikdan voz kechdi.", COMMAND_STANDS''', r'''PREFIX, player, "отказался от командования.", COMMAND_STANDS''')
e(f, r'''PREFIX, player, "was fired from warden.", COMMAND_STANDS''', r'''PREFIX, player, "nazoratchilikdan olindi.", COMMAND_STANDS''', r'''PREFIX, player, "снят с командира.", COMMAND_STANDS''')
e(f, r'''      admin,
      "fired",
      player,
      "from warden.",''', r'''      admin,
      "nazoratchilikdan oldi:",
      player,
      "",''', r'''      admin,
      "снял с командира игрока",
      player,
      "",''')
e(f, r'''{ PREFIX, player, "is now the warden." }''', r'''{ PREFIX, player, "endi nazoratchi." }''', r'''{ PREFIX, player, "теперь командир." }''')
e(f, r'''{ PREFIX, "The warden is", player, "." }''', r'''{ PREFIX, "Nazoratchi:", player, "." }''', r'''{ PREFIX, "Командир:", player, "." }''')
e(f, r'''{ PREFIX, "There is no warden." }''', r'''{ PREFIX, "Nazoratchi yo'q." }''', r'''{ PREFIX, "Командира нет." }''')
e(f, r'''"You cannot warden during warmup."''', r'''"Razminka paytida nazoratchi bo'lib bo'lmaydi."''', r'''"Во время разминки нельзя стать командиром."''')
e(f, r'''PREFIX, player, "was fired and is no longer the warden."''', r'''PREFIX, player, "olib tashlandi va endi nazoratchi emas."''', r'''PREFIX, player, "снят и больше не командир."''')
e(f, r'''PREFIX, "Marker placed."''', r'''PREFIX, "Belgi qo'yildi."''', r'''PREFIX, "Маркер установлен."''')
e(f, r'''$"{marker}{ChatColors.Grey} marker removed."''', r'''$"{marker}{ChatColors.Grey} belgi olib tashlandi."''', r'''$"{marker}{ChatColors.Grey} маркер удалён."''')
e(f, r'''ChatColors.Grey + "You",
      enabled ? ChatColors.Green + "enabled" : ChatColors.Red + "disabled",
      ChatColors.Grey + "Auto-Warden."''', r'''ChatColors.Grey + "Auto-Warden:",
      enabled ? ChatColors.Green + "yoqildi" : ChatColors.Red + "o'chirildi",
      ChatColors.Grey + "."''', r'''ChatColors.Grey + "Auto-Warden:",
      enabled ? ChatColors.Green + "включён" : ChatColors.Red + "выключен",
      ChatColors.Grey + "."''')

f = L+'Warden/WardenSTLocale.cs'
e(f, r'''$"You now have {ChatColors.Green}Special Treatment{ChatColors.White}!"''', r'''$"Senga {ChatColors.Green}imtiyoz{ChatColors.White} berildi!"''', r'''$"Тебе выдана {ChatColors.Green}привилегия{ChatColors.White}!"''')
e(f, r'''$"Your Special Treatment was {ChatColors.Red}removed{ChatColors.White}."''', r'''$"Imtiyozing {ChatColors.Red}olib tashlandi{ChatColors.White}."''', r'''$"Твоя привилегия {ChatColors.Red}снята{ChatColors.White}."''')
e(f, r'''$"now has {ChatColors.Green}Special Treatment{ChatColors.White}!"''', r'''$"endi {ChatColors.Green}imtiyozli{ChatColors.White}!"''', r'''$"получил {ChatColors.Green}привилегию{ChatColors.White}!"''')
e(f, r'''$"{ChatColors.Red}no longer {ChatColors.Grey}has Special Treatment."''', r'''$"{ChatColors.Red}endi {ChatColors.Grey}imtiyozli emas."''', r'''$"{ChatColors.Red}больше не {ChatColors.Grey}имеет привилегию."''')
