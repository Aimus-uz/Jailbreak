E2 = []
def m(f, find, uz, ru): E2.append((f, find, uz, ru))

# ---- team names ----
f = 'public/Jailbreak.Formatting/Objects/TeamFormatObject.cs'
m(f, '''CsTeam.CounterTerrorist => "Guards",''', '''CsTeam.CounterTerrorist => "Qo'riqchilar",''', '''CsTeam.CounterTerrorist => "Охрана",''')
m(f, '''CsTeam.Terrorist => "Prisoners",''', '''CsTeam.Terrorist => "Mahbuslar",''', '''CsTeam.Terrorist => "Заключённые",''')
m(f, '''CsTeam.None => "No one",''', '''CsTeam.None => "Hech kim",''', '''CsTeam.None => "Никто",''')
m(f, '''CsTeam.Spectator => "Spectators",''', '''CsTeam.Spectator => "Kuzatuvchilar",''', '''CsTeam.Spectator => "Наблюдатели",''')

# ---- LR names ----
f = 'public/Jailbreak.Public/Mod/LastRequest/Enums/LRType.cs'
for en, uz, ru in [('Gun Toss','Qurol otish','Бросок оружия'), ('Rock Paper Scissors','Tosh-qaychi-qog\'oz','Камень-ножницы-бумага'),
                   ('Knife Fight','Pichoq jangi','Бой на ножах'), ('No Scope','No Scope','No Scope'), ('Coinflip','Tanga','Монетка'),
                   ('Shot For Shot','O\'q-o\'qqa','Выстрел за выстрел'), ('Mag For Mag','Magazin-magazinga','Магазин за магазин'), ('Race','Poyga','Гонка')]:
    m(f, f'=> "{en}",', f'=> "{uz}",', f'=> "{ru}",')
m(f, '''_                          => "Unknown"''', '''_                          => "Noma'lum"''', '''_                          => "Неизвестно"''')

# ---- SD permission: EdgeGamers donor flag -> server admins ----
f = 'public/Jailbreak.Public/Mod/SpecialDay/Enums/SDType.cs'
m(f, '''AdminManager.PlayerHasPermissions(executor, "@ego/dssilver") ?''', '''AdminManager.PlayerHasPermissions(executor, "@css/generic") ?''', '''AdminManager.PlayerHasPermissions(executor, "@css/generic") ?''')
m(f, '''$"You must be a {ChatColors.Green}Silver Supporter {ChatColors.Default}({ChatColors.LightBlue}https://edgm.rs/donate{ChatColors.Default}){ChatColors.Grey} to start this day.",''',
     '''$"Bu kunni faqat {ChatColors.Green}adminlar{ChatColors.Grey} boshlay oladi.",''',
     '''$"Этот день могут начать только {ChatColors.Green}админы{ChatColors.Grey}.",''')

# ---- LR command reasons ----
f = 'mod/Jailbreak.LastRequest/LastRequestCommand.cs'
for en, uz, ru in [('You are not a Prisoner','sen mahbus emassan','ты не заключённый'), ('You are not alive','sen tirik emassan','ты мёртв'),
                   ('No players available to LR','LR uchun o\'yinchi yo\'q','нет игроков для LR'), ('You are already in an LR','sen allaqachon LR dasan','ты уже в LR'),
                   ('They are not a Guard','u qo\'riqchi emas','он не охранник'), ('They are not alive','u tirik emas','он мёртв'),
                   ('They are already in an LR','u allaqachon LR da','он уже в LR')]:
    m(f, f'"{en}"', f'"{uz}"', f'"{ru}"')
m(f, '"An error occurred while initiating the last request. Please try again later."', '"LR ni boshlashda xatolik. Keyinroq qayta urinib ko\'r."', '"Ошибка при запуске LR. Попробуй позже."')
f = 'mod/Jailbreak.LastRequest/LastRequestRebelCommand.cs'
m(f, '"You are already in an LR"', '"sen allaqachon LR dasan"', '"ты уже в LR"')
m(f, '"You must be the last alive to !rebel"', '"!rebel uchun oxirgi tirik qolgan bo\'lishing kerak"', '"для !rebel нужно остаться последним живым"')
m('mod/Jailbreak.LastRequest/LastRequests/BulletForBullet.cs', '"equal health"', '"sog\'liq teng"', '"равное здоровье"')
m('mod/Jailbreak.LastRequest/LastRequests/BulletForBullet.cs', '"Choose Pistol"', '"To\'pponcha tanla"', '"Выбери пистолет"')
m('mod/Jailbreak.LastRequest/LastRequests/NoScope.cs', '"Choose Rifle"', '"Miltiq tanla"', '"Выбери винтовку"')
m('mod/Jailbreak.LastRequest/LastRequests/NoScope.cs', 'PrintToParticipants("Go!");', 'PrintToParticipants("Boshla!");', 'PrintToParticipants("Начали!");')

f = 'mod/Jailbreak.LastRequest/LastRequests/Coinflip.cs'
m(f, '''    "A glint of silver flashes through the air...", "The coin does a 180...!",
    "Gravity seems so much heavier...", "A quiet clink is heard...",
    "An arrow hits the coin!", "The coin is shot in mid-air.",
    "The answer is 42", "And yet...", "A sliver of copper falls off...",
    "Lucky number 7...", "The coin lands on its side!",
    "A bald eagle soars above",
    "There wasn't enough room for the two of ya anyways...",
    "Woosh woosh woosh", "banana rotate"''',
'''    "Havoda kumush yaltirab ketdi...", "Tanga 180 gradus aylandi...!",
    "Tortishish kuchi og'irlashgandek...", "Sekin jaranglagan ovoz eshitildi...",
    "Tangaga o'q tegdi!", "Tangani havoda otib yuborishdi.",
    "Javob — 42", "Va baribir...", "Tangadan mis parchasi uchib ketdi...",
    "Omadli 7 raqami...", "Tanga qirrasi bilan tushdi!",
    "Tepada burgut uchib o'tdi",
    "Baribir ikkalangizga joy yetmas edi...",
    "Vuush vuush vuush", "banan aylanmoqda"''',
'''    "В воздухе блеснуло серебро...", "Монета перевернулась на 180...!",
    "Гравитация будто стала тяжелее...", "Раздался тихий звон...",
    "Стрела попала в монету!", "Монету подстрелили в воздухе.",
    "Ответ — 42", "И всё же...", "От монеты отлетел кусочек меди...",
    "Счастливое число 7...", "Монета упала на ребро!",
    "Над головой пролетел орёл",
    "Вам двоим всё равно было тесно...",
    "Вжух вжух вжух", "банан крутится"''')
m(f, 'new ChatMenu("Heads or Tails?")', 'new ChatMenu("Gerbmi yoki raqam?")', 'new ChatMenu("Орёл или решка?")')
m(f, 'menu.AddMenuOption("Heads",', 'menu.AddMenuOption("Gerb",', 'menu.AddMenuOption("Орёл",')
m(f, 'menu.AddMenuOption("Tails",', 'menu.AddMenuOption("Raqam",', 'menu.AddMenuOption("Решка",')
m(f, 'menu.Title = "Heads or Tails? - "', 'menu.Title = "Gerbmi yoki raqam? - "', 'menu.Title = "Орёл или решка? - "')

f = 'mod/Jailbreak.LastRequest/LastRequests/RockPaperScissors.cs'
m(f, 'new ChatMenu("Rock Paper Scissors")', 'new ChatMenu("Tosh, qaychi, qog\'oz")', 'new ChatMenu("Камень, ножницы, бумага")')
m(f, '["Rock", "Paper", "Scissors"]', '["Tosh", "Qog\'oz", "Qaychi"]', '["Камень", "Бумага", "Ножницы"]')
m(f, 'new[] { "Rock", "Paper", "Scissors" }', 'new[] { "Tosh", "Qog\'oz", "Qaychi" }', 'new[] { "Камень", "Бумага", "Ножницы" }')
m(f, '$"Rock Paper Scissors - {Prisoner.PlayerName} vs {Guard.PlayerName}"', '$"Tosh, qaychi, qog\'oz - {Prisoner.PlayerName} vs {Guard.PlayerName}"', '$"Камень, ножницы, бумага - {Prisoner.PlayerName} vs {Guard.PlayerName}"')

# ---- RTD rewards ----
R = 'mod/Jailbreak.RTD/Rewards/'
m(R+'ArmorReward.cs', '"You will spawn with " + armor + " Armor next round."', '"Keyingi raundda " + armor + " zirh bilan tug\'ilasan."', '"В следующем раунде у тебя будет " + armor + " брони."')
m(R+'BombReward.cs', '"Bomb"', '"Bomba"', '"Бомба"')
m(R+'BombReward.cs', '"You will receive the bomb next round."', '"Keyingi raundda senga bomba beriladi."', '"В следующем раунде ты получишь бомбу."')
m(R+'CannotLeftKnife.cs', '"Cannot Left-Knife"', '"Pichoq chap tugmasiz"', '"Без левого удара ножом"')
m(R+'CannotLeftKnife.cs', '"You will not be able to left-click knife next round."', '"Keyingi raundda pichoqni chap tugma bilan ishlatolmaysan."', '"В следующем раунде нельзя бить ножом левой кнопкой."')
m(R+'CannotRightKnife.cs', '"Cannot Right-Knife"', '"Pichoq o\'ng tugmasiz"', '"Без правого удара ножом"')
m(R+'CannotRightKnife.cs', '"You will not be able to right-click knife next round."', '"Keyingi raundda pichoqni o\'ng tugma bilan ishlatolmaysan."', '"В следующем раунде нельзя бить ножом правой кнопкой."')
m(R+'CannotScope.cs', '"Cannot Scope"', '"Pritselsiz"', '"Без прицела"')
m(R+'CannotScope.cs', '"You will not be able to scope next round."', '"Keyingi raundda pritseldan foydalana olmaysan."', '"В следующем раунде нельзя использовать прицел."')
m(R+'CannotUseReward.cs', '$"Cannot Use {NameShort}"', '$"{NameShort} ishlatib bo\'lmaydi"', '$"Нельзя: {NameShort}"')
m(R+'CannotUseReward.cs', '$"You will not be able to use {NameShort} next round."', '$"Keyingi raundda {NameShort} ishlata olmaysan."', '$"В следующем раунде нельзя использовать {NameShort}."')
m(R+'ChatSpyReward.cs', '"Chat Spy"', '"Chat josusi"', '"Шпион чата"')
m(R+'ChatSpyReward.cs', '"You will be able to read all team chats next round."', '"Keyingi raundda barcha jamoa chatlarini o\'qiy olasan."', '"В следующем раунде ты будешь читать все командные чаты."')
m(R+'ColorReward.cs', '$"You will spawn {ChatColor}{ColorName}{ChatColors.Grey} next round."', '$"Keyingi raundda {ChatColor}{ColorName}{ChatColors.Grey} rangda tug\'ilasan."', '$"В следующем раунде ты будешь цвета {ChatColor}{ColorName}{ChatColors.Grey}."')
m(R+'ColorReward.cs', 'public virtual string Name => "Spawn " + ColorName;', 'public virtual string Name => "Rang: " + ColorName;', 'public virtual string Name => "Цвет: " + ColorName;')
m(R+'FakeBombReward.cs', '"Fake Bomb"', '"Soxta bomba"', '"Фальшивая бомба"')
m(R+'FakeBombReward.cs', '"You will spawn with a fake bomb next round."', '"Keyingi raundda soxta bomba bilan tug\'ilasan."', '"В следующем раунде у тебя будет фальшивая бомба."')
m(R+'GuaranteedWardenReward.cs', '"Guaranteed Warden"', '"Kafolatlangan nazoratchi"', '"Гарантированный командир"')
m(R+'GuaranteedWardenReward.cs', '"You are guaranteed to be the warden next round if you queue for it."', '"Navbatga tursang, keyingi raundda albatta nazoratchi bo\'lasan."', '"Если встанешь в очередь, в следующем раунде точно станешь командиром."')
m(R+'HPReward.cs', '"You won " + hp + " HP next round."', '"Keyingi raund uchun " + hp + " HP yutding."', '"Ты выиграл " + hp + " HP на следующий раунд."')
m(R+'NoWeaponReward.cs', '"No Weapon"', '"Qurolsiz"', '"Без оружия"')
m(R+'NoWeaponReward.cs', '"You will not spawn with a knife next round."', '"Keyingi raundda pichoqsiz tug\'ilasan."', '"В следующем раунде у тебя не будет ножа."')
m(R+'NothingReward.cs', '"Nothing"', '"Hech narsa"', '"Ничего"')
m(R+'NothingReward.cs', '"You won nothing."', '"Hech narsa yutmading."', '"Ты ничего не выиграл."')
m('mod/Jailbreak.RTD/RTDRewarder.cs', 'reward.Name != "Nothing"', 'reward.Name != "Hech narsa"', 'reward.Name != "Ничего"')
m(R+'RandomTeleportReward.cs', '"Random Teleport"', '"Tasodifiy teleport"', '"Случайный телепорт"')
m(R+'RandomTeleportReward.cs', '"You will be teleported to a random location next round."', '"Keyingi raundda tasodifiy joyga teleport bo\'lasan."', '"В следующем раунде тебя телепортирует в случайное место."')
m(R+'TransparentReward.cs', '"Spawn Transparent"', '"Shaffof bo\'lish"', '"Прозрачность"')
m(R+'TransparentReward.cs', '"You will spawn transparent next round."', '"Keyingi raundda shaffof tug\'ilasan."', '"В следующем раунде ты будешь прозрачным."')
m(R+'WeaponReward.cs', '"You won a" + (weapon.GetFriendlyWeaponName()[0].IsVowel() ? "n" : "")', '"Keyingi raund uchun yutding:"', '"Ты выиграл на следующий раунд:"')
m(R+'WeaponReward.cs', '+ " " + weapon.GetFriendlyWeaponName() + " next round."', '+ " " + weapon.GetFriendlyWeaponName() + "."', '+ " " + weapon.GetFriendlyWeaponName() + "."')
m(R+'CreditReward.cs', '$"{credits} credit{(credits == 1 ? "" : "s")}"', '$"{credits} kredit"', '$"{credits} кредит(ов)"')
m(R+'CreditReward.cs', '$"You won {Name}', '$"Yutuq: {Name}', '$"Ты выиграл {Name}')

# ---- Special days (mod) ----
S = 'mod/Jailbreak.SpecialDay/SpecialDays/'
m(S+'GhostDay.cs', '''new SoloDayLocale("Ghost War",
      "Now you see me… now you don’t! Fight through flickering visibility!")''', '''new SoloDayLocale("Arvohlar urushi",
      "Hozir ko'rinasan... endi ko'rinmaysan! Miltillovchi ko'rinishda jang qil!")''', '''new SoloDayLocale("Война призраков",
      "То видно... то не видно! Сражайся при мерцающей видимости!")''')
m(S+'GhostDay.cs', '''? "Visible" : "Hidden")} for: {timeLeft}s"''', '''? "Ko'rinasan" : "Yashiringansan")}: {timeLeft}s"''', '''? "Тебя видно" : "Ты невидим")}: {timeLeft}с"''')
m(S+'NoScopeDay.cs', '''new SoloDayLocale("No Scope",
      "Your scope broke! Fight against everyone else. No camping!")''', '''new SoloDayLocale("No Scope",
      "Pritseling buzildi! Hammaga qarshi jang qil. Bir joyda poylab o'tirma!")''', '''new SoloDayLocale("No Scope",
      "Прицел сломан! Сражайся против всех. Не кемпери!")''')
m(S+'TeleportDay.cs', '''new SoloDayLocale("Teleport",
      "Free for all! If you damage someone, you will swap places with them!")''', '''new SoloDayLocale("Teleport",
      "Hamma hammaga qarshi! Kimgadir zarar yetkazsang, u bilan joy almashasan!")''', '''new SoloDayLocale("Телепорт",
      "Все против всех! Ранишь кого-то — поменяешься с ним местами!")''')
m(S+'HEDay.cs', '''new SoloDayLocale("HE Only",
      "Grenades Only—No guns. Fight against everyone else. No Camping!")''', '''new SoloDayLocale("Faqat HE",
      "Faqat granatalar, qurol yo'q. Hammaga qarshi jang qil. Poylab o'tirma!")''', '''new SoloDayLocale("Только HE",
      "Только гранаты, без оружия. Сражайся против всех. Не кемпери!")''')
m(S+'RocketJumpDay.cs', '''new SoloDayLocale("Rocket Jump",
      "Your shotgun is now an RPG that fires grenades! "
      + "Shoot the ground to launch! " + "Mid-air knives Insta-kill!")''', '''new SoloDayLocale("Raketa sakrash",
      "Drobovigingiz endi granata otadigan RPG! "
      + "Uchish uchun yerga oting! " + "Havodagi pichoq zarbasi darhol o'ldiradi!")''', '''new SoloDayLocale("Рокет-джамп",
      "Твой дробовик теперь RPG, стреляющий гранатами! "
      + "Стреляй в землю, чтобы взлететь! " + "Удар ножом в воздухе убивает сразу!")''')
m(S+'CustomDay.cs', '''new TeamDayLocale("Custom",
      "Listen to the Warden's orders. Anything goes!")''', '''new TeamDayLocale("Maxsus o'yin",
      "Nazoratchining buyruqlarini tinglang. Hamma narsa mumkin!")''', '''new TeamDayLocale("Свой день",
      "Слушайте приказы командира. Возможно всё!")''')
m(S+'BHopDay.cs', '''new TeamDayLocale("Bunny Hop",
      "Auto-Bunny hopping is on, otherwise normal day!")''', '''new TeamDayLocale("Bunny Hop",
      "Avto-bunnyhop yoqilgan, qolgani oddiy kun!")''', '''new TeamDayLocale("Распрыжка",
      "Включён авто-банихоп, в остальном обычный день!")''')
m(S+'OneInTheChamberDay.cs', '''new SoloDayLocale("One in the Chamber", "You only have one bullet.",
      "Kill someone to get another bullet.", "One-Hit-Kills! No camping!")''', '''new SoloDayLocale("Bitta o'q", "Senda faqat bitta o'q bor.",
      "Yana o'q olish uchun kimnidir o'ldir.", "Bir zarbada o'lim! Poylab o'tirma!")''', '''new SoloDayLocale("Один патрон", "У тебя только один патрон.",
      "Убей кого-нибудь, чтобы получить ещё один.", "Убийство с одного попадания! Не кемпери!")''')
m(S+'FFADay.cs', '''new SoloDayLocale("Free for All",
      "Everyone for themselves! No camping, actively pursue!")''', '''new SoloDayLocale("Hamma hammaga qarshi",
      "Har kim o'zi uchun! Poylab o'tirma, faol hujum qil!")''', '''new SoloDayLocale("Все против всех",
      "Каждый сам за себя! Не кемпери, атакуй!")''')
m(S+'AbstractArmoryRestrictedDay.cs', '''$"{ChatColors.Grey}Today is {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, so stay in armory!"''', '''$"{ChatColors.Grey}Bugun {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, qurolxonada qoling!"''', '''$"{ChatColors.Grey}Сегодня {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, оставайтесь в оружейной!"''')
m(S+'AbstractArmoryRestrictedDay.cs', '''ChatColors.Grey + "Stay in armory!"''', '''ChatColors.Grey + "Qurolxonada qoling!"''', '''ChatColors.Grey + "Оставайтесь в оружейной!"''')
m(S+'AbstractCellRestrictedDay.cs', '''$"{ChatColors.Grey}Today is {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, so stay in cells!"''', '''$"{ChatColors.Grey}Bugun {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, kameralarda qoling!"''', '''$"{ChatColors.Grey}Сегодня {ChatColors.White}{messaged.Locale.Name}{ChatColors.Grey}, оставайтесь в камерах!"''')
m(S+'AbstractCellRestrictedDay.cs', '''ChatColors.Grey + "Stay in cells!"''', '''ChatColors.Grey + "Kameralarda qoling!"''', '''ChatColors.Grey + "Оставайтесь в камерах!"''')

# ---- Warden countdown & menus ----
f = 'mod/Jailbreak.Warden/Commands/CountdownCommandBehavior.cs'
m(f, '''$" {ChatColors.DarkBlue}Countdown>"''', '''$" {ChatColors.DarkBlue}Sanoq>"''', '''$" {ChatColors.DarkBlue}Отсчёт>"''')
m(f, '''$"A {duration} second countdown has begun!"''', '''$"{duration} soniyalik sanoq boshlandi!"''', '''$"Начался отсчёт: {duration} сек.!"''')
m(f, '''"GO! GO! GO!"''', '''"OLG'A! OLG'A! OLG'A!"''', '''"ВПЕРЁД! ВПЕРЁД! ВПЕРЁД!"''')
m(f, '''generics.InvalidParameter(command.GetArg(1), "number");''', '''generics.InvalidParameter(command.GetArg(1), "son");''', '''generics.InvalidParameter(command.GetArg(1), "число");''')
m(f, '''"number greater than 0"''', '''"0 dan katta son"''', '''"число больше 0"''')
m(f, '''$"number greater than or equal to {CV_WARDEN_MIN_COUNTDOWN.Value}"''', '''$"{CV_WARDEN_MIN_COUNTDOWN.Value} yoki undan katta son"''', '''$"число не меньше {CV_WARDEN_MIN_COUNTDOWN.Value}"''')
m(f, '''$"number less than or equal to {CV_WARDEN_MAX_COUNTDOWN.Value}"''', '''$"{CV_WARDEN_MAX_COUNTDOWN.Value} yoki undan kichik son"''', '''$"число не больше {CV_WARDEN_MAX_COUNTDOWN.Value}"''')
f = 'mod/Jailbreak.Warden/Commands/MarkerCommandBehavior.cs'
m(f, '''new CenterHtmlMenu("Marker Type", plugin)''', '''new CenterHtmlMenu("Belgi shakli", plugin)''', '''new CenterHtmlMenu("Форма маркера", plugin)''')
m(f, '''new CenterHtmlMenu("Marker Color", plugin)''', '''new CenterHtmlMenu("Belgi rangi", plugin)''', '''new CenterHtmlMenu("Цвет маркера", plugin)''')
