"""Generates the Pokémon detail pages in ../pokemon/.

Edit the DATA list below, then run:  python3 tools/build_pages.py
"""
from html import escape
from pathlib import Path

ART = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png"
SPR = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png"
F = "https://static.wikia.nocookie.net/pokemon/images/"  # Pokémon Fandom wiki CDN


def stage(name, dex):
    return {"name": name, "img": ART.format(dex)}


TRAINER_ASH = {
    "name": "Ash Ketchum",
    "role": "Main protagonist, Pokémon the Series (1997–2023)",
    "img": F + "7/76/Ash_anime_The_Beginning.png/revision/latest?cb=20110507193331",
}

DATA = [
    {
        "slug": "garchomp", "name": "Garchomp", "dex": 445, "types": ["dragon", "ground"], "accent": "dragon",
        "evo": [stage("Gible", 443), "Lv. 24", stage("Gabite", 444), "Lv. 48", stage("Garchomp", 445),
                "Garchompite", stage("Mega Garchomp", 10058)],
        "evo_note": None,
        "trainers": [
            {"name": "Cynthia", "role": "Sinnoh Champion",
             "img": F + "5/56/Cynthia_anime_Journeys.png/revision/latest?cb=20220727031303",
             "bio": "The Champion of the Sinnoh League and a researcher of Pokémon myths. Garchomp is her ace. "
                    "In Pokémon Journeys she is one of the Masters Eight, the world's strongest Trainers, "
                    "and her Garchomp Mega Evolves in battle.",
             "partner": F + "3/32/Cynthia_Garchomp.png/revision/latest?cb=20220715224002",
             "partner_cap": "Cynthia's Garchomp"},
            {**TRAINER_ASH,
             "bio": "Ash caught a Gible in Sinnoh. It became famous for chomping on everything, including Ash's head, "
                    "and for its long struggle to master Draco Meteor. It never evolved during the series.",
             "partner": F + "3/3e/Ash_Gible_Draco_Meteor.png/revision/latest?cb=20150912051527",
             "partner_cap": "Ash's Gible trying Draco Meteor"},
        ],
        "anime": [
            (F + "c/c3/DP040_TC_JA.png/revision/latest?cb=20250709052538",
             "DP040 “Top-Down Training!”: debut of Cynthia's Garchomp (Japanese title card)"),
            (F + "2/23/Cynthia_Garchomp_Draco_Meteor.png/revision/latest?cb=20220715225123",
             "Cynthia's Garchomp using Draco Meteor"),
            (F + "d/d1/Cynthia_Mega_Garchomp.png/revision/latest?cb=20220715225538",
             "Mega Garchomp in Pokémon Journeys"),
        ],
        "games_intro": "Garchomp debuted in Generation IV, as the final form of Gible found in Wayward Cave.",
        "games": [
            (F + "2/22/DiamondUS.jpg/revision/latest?cb=20110219042350", "Pokémon Diamond (2006)"),
            (F + "6/6f/PearlUS.jpg/revision/latest?cb=20140828053932", "Pokémon Pearl (2006)"),
        ],
        "sprite": (SPR.format("versions/generation-iv/diamond-pearl/445"), "In-game sprite from Diamond & Pearl"),
    },
    {
        "slug": "rayquaza", "name": "Rayquaza", "dex": 384, "types": ["dragon", "flying"], "accent": "flying",
        "evo": [stage("Rayquaza", 384), "Dragon Ascent", stage("Mega Rayquaza", 10079)],
        "evo_note": "Rayquaza doesn't evolve, but it can Mega Evolve by knowing the move Dragon Ascent. It needs no Mega Stone.",
        "trainers": [
            {"name": "Roy", "role": "Protagonist, Pokémon Horizons",
             "img": F + "0/08/Roy_2.png/revision/latest?cb=20250321154047",
             "bio": "One of the two lead characters of Pokémon Horizons. Roy carries the Ancient Poké Ball, "
                    "which holds the Black Rayquaza. That Rayquaza was once the partner of the legendary "
                    "explorer Lucius, and it later answers to Roy.",
             "partner": F + "e/ea/Roy_Rayquaza.png/revision/latest?cb=20260228080107",
             "partner_cap": "The Black Rayquaza"},
        ],
        "anime": [
            (F + "7/7c/MS007.png/revision/latest?cb=20110215110738",
             "Pokémon: Destiny Deoxys (2004): Rayquaza's first major anime role"),
            (F + "7/7f/PH006_TC_JA.png/revision/latest?cb=20230514000659",
             "PH006 “The Ancient Poké Ball”: debut of the Black Rayquaza (Japanese title card)"),
            (F + "8/82/Roy_Mega_Rayquaza.png/revision/latest?cb=20260502083650",
             "The Black Rayquaza Mega Evolved"),
        ],
        "games_intro": "Rayquaza debuted in Generation III. It sleeps at the top of Sky Pillar, and it is the cover Legendary of Emerald.",
        "games": [
            (F + "d/d8/Pok%C3%A9mon_Ruby_Version.png/revision/latest?cb=20260621094605", "Pokémon Ruby (2002)"),
            (F + "1/1e/Pok%C3%A9mon_Sapphire_Version.png/revision/latest?cb=20260621094453", "Pokémon Sapphire (2002)"),
            (F + "8/85/Pok%C3%A9mon_Emerald_boxart_EN-US.jpg/revision/latest?cb=20120128161444", "Pokémon Emerald (2004), with Rayquaza on the cover"),
        ],
        "sprite": (SPR.format("versions/generation-iii/ruby-sapphire/384"), "In-game sprite from Ruby & Sapphire"),
    },
    {
        "slug": "greninja", "name": "Greninja", "dex": 658, "types": ["water", "dark"], "accent": "water",
        "evo": [stage("Froakie", 656), "Lv. 16", stage("Frogadier", 657), "Lv. 36", stage("Greninja", 658),
                "Battle Bond", stage("Ash-Greninja", 10117)],
        "evo_note": None,
        "trainers": [
            {**TRAINER_ASH,
             "bio": "Ash met Froakie in the first episode of XY, and it evolved all the way to Greninja. Their bond created "
                    "Ash-Greninja, a transformation unique to them. Greninja stayed behind in Kalos to help Zygarde protect the region.",
             "partner": F + "9/90/Ash_and_Greninja.png/revision/latest?cb=20200812184056",
             "partner_cap": "Ash and Greninja"},
        ],
        "anime": [
            (F + "c/c8/XY001_TC_JA.png/revision/latest?cb=20200417174015",
             "XY001 “Kalos, Where Dreams and Adventures Begin!” (Japanese title card)"),
            (F + "a/a8/XY001_20.png/revision/latest?cb=20160504210303", "Scene from XY001"),
            (F + "e/e2/Ash%27s_Ash-Greninja.png/revision/latest?cb=20170523121310", "Ash-Greninja"),
        ],
        "games_intro": "Greninja debuted in Generation VI, as the final evolution of Froakie, the Water-type starter of Kalos.",
        "games": [
            (F + "4/45/Pokemon_X_Version_Boxart.png/revision/latest?cb=20201120113848", "Pokémon X (2013)"),
            (F + "c/c4/Pokemon_Y_Version_Boxart.png/revision/latest?cb=20201120114053", "Pokémon Y (2013)"),
        ],
        "sprite": (SPR.format("versions/generation-vi/x-y/658"), "In-game model from X & Y"),
    },
    {
        "slug": "articuno", "name": "Articuno", "dex": 144, "types": ["ice", "flying"], "accent": "ice",
        "evo": [stage("Articuno", 144), "Regional form", stage("Galarian Articuno", 10169)],
        "evo_note": "Articuno doesn't evolve. Galarian Articuno is a Psychic/Flying regional form introduced in Sword & Shield.",
        "trainers": [
            {"name": "Noland", "role": "Factory Head, Battle Frontier",
             "img": F + "c/c5/Factory_Head_Noland_anime.png/revision/latest?cb=20240312093245",
             "bio": "The Frontier Brain who runs the Battle Factory, and the first Frontier Brain Ash faced. "
                    "Unusually for a Trainer, Noland owns a Legendary Pokémon, and he used his Articuno against Ash.",
             "partner": F + "c/c2/Noland_Articuno.png/revision/latest?cb=20240227004748",
             "partner_cap": "Noland's Articuno"},
        ],
        "anime": [
            (F + "c/cc/MS002.png/revision/latest?cb=20110215105617",
             "Pokémon the Movie 2000 (The Power of One): Articuno's anime debut"),
            (F + "2/20/Articuno_Ice_Beam.png/revision/latest?cb=20151004095713", "Articuno using Ice Beam in the movie"),
            (F + "c/cd/Noland_Articuno_Ice_Beam.png/revision/latest?cb=20240227004731",
             "RS136 “Numero Uno Articuno”: Noland's Articuno"),
        ],
        "games_intro": "Articuno debuted in Generation I. It waits at the bottom of the Seafoam Islands.",
        "games": [
            (F + "7/7f/Pok%C3%A9mon_Red_Version.png/revision/latest?cb=20260621083910", "Pokémon Red (1996 JP / 1998 intl.)"),
            (F + "f/f1/Pok%C3%A9mon_Blue_Version.png/revision/latest?cb=20260621083808", "Pokémon Blue (1996 JP / 1998 intl.)"),
        ],
        "sprite": (SPR.format("versions/generation-i/red-blue/144"), "Original sprite from Red & Blue"),
    },
    {
        "slug": "pichu", "name": "Pichu", "dex": 172, "types": ["electric"], "accent": "electric",
        "evo": [stage("Pichu", 172), "High friendship", stage("Pikachu", 25), "Thunder Stone",
                [stage("Raichu", 26), stage("Alolan Raichu", 10100)]],
        "evo_note": "Pikachu becomes Alolan Raichu when it's evolved in the Alola region.",
        "trainers": [],
        "no_trainer_note": "No main anime Trainer is known for owning a Pichu. The most famous anime Pichu are the wild Pichu Brothers:",
        "featured": {"name": "The Pichu Brothers", "role": "Stars of their own anime shorts",
                     "img": F + "6/61/Pichu_Bros_promo.jpg/revision/latest?cb=20260209075745",
                     "bio": "Two mischievous Pichu siblings, the big brother and the little brother. They debuted in the "
                            "short “Pikachu & Pichu”, went on to star in more shorts, and even met Ash and his friends.",
                     "partner": F + "7/7c/Curious_Pichu_Bros..png/revision/latest?cb=20260210174958",
                     "partner_cap": "The Pichu Brothers"},
        "anime": [
            (F + "f/f1/Pikachu_%26_pichu_title.jpg/revision/latest?cb=20130904003902",
             "“Pikachu & Pichu” (2000) title: Pichu's anime debut"),
            (F + "4/46/Pichu_Brothers.png/revision/latest?cb=20110521171802", "The Pichu Brothers"),
            (F + "9/90/Thundershockpichu.jpg/revision/latest?cb=20170125233010", "Pichu using Thunder Shock"),
        ],
        "games_intro": "Pichu debuted in Generation II, one of the first “baby” Pokémon, hatched from Eggs.",
        "games": [
            (F + "8/86/Pok%C3%A9mon_Gold_Version.png/revision/latest?cb=20260621085536", "Pokémon Gold (1999)"),
            (F + "0/0c/Pok%C3%A9mon_Silver_Version.png/revision/latest?cb=20260621085627", "Pokémon Silver (1999)"),
        ],
        "sprite": (SPR.format("versions/generation-ii/gold/172"), "Original sprite from Gold"),
    },
    {
        "slug": "mimikyu", "name": "Mimikyu", "dex": 778, "types": ["ghost", "fairy"], "accent": "ghost",
        "evo": [stage("Mimikyu", 778)],
        "evo_note": "Mimikyu has no evolutions.",
        "trainers": [
            {"name": "Jessie", "role": "Team Rocket member",
             "img": F + "a/a3/Jessie_anime_Sun_and_Moon.png/revision/latest?cb=20181129161917",
             "bio": "One third of Team Rocket, with James and Meowth. In Alola, Mimikyu joined her because it shared "
                    "her goal of defeating Pikachu. It holds a deep grudge against Pikachu and is strong enough to "
                    "scare even Team Rocket.",
             "partner": F + "d/d6/Jessie_Mimikyu.png/revision/latest?cb=20170915045921",
             "partner_cap": "Jessie's Mimikyu"},
        ],
        "anime": [
            (F + "9/94/SM003_TC_JA.png/revision/latest?cb=20230509232752",
             "SM003 “Loading the Dex!”: debut of Jessie's Mimikyu (Japanese title card)"),
            (F + "2/24/Jessie_and_Mimikyu.png/revision/latest?cb=20200828195448", "Jessie and Mimikyu"),
            (F + "e/e8/Jessie_Mimikyu_Shadow_Claw.png/revision/latest?cb=20161124152513", "Mimikyu using Shadow Claw"),
        ],
        "games_intro": "Mimikyu debuted in Generation VII. It lurks in the Thrifty Megamart, an abandoned store on Ula'ula Island.",
        "games": [
            (F + "b/b6/Pok%C3%A9mon_Sun.jpg/revision/latest?cb=20231203183408", "Pokémon Sun (2016)"),
            (F + "f/f9/Pok%C3%A9mon_Moon.jpg/revision/latest?cb=20231214143314", "Pokémon Moon (2016)"),
        ],
        "sprite": (SPR.format("778"), "In-game sprite"),
    },
    {
        "slug": "jolteon", "name": "Jolteon", "dex": 135, "types": ["electric"], "accent": "electric",
        "evo": [stage("Eevee", 133), "Thunder Stone", stage("Jolteon", 135)],
        "evo_note": "Eevee can evolve into eight different Pokémon. Jolteon is one of the three originals.",
        "trainers": [
            {"name": "Sparky", "role": "One of the Eevee Brothers",
             "img": F + "8/88/Sparky.jpg/revision/latest?cb=20131130124345",
             "bio": "Sparky and his brothers Pyro and Rainer each evolved their Eevee, and they pressured their youngest "
                    "brother Mikey to do the same. Sparky's Jolteon battled Ash in “The Battling Eevee Brothers”.",
             "partner": F + "f/f6/Sparky_Jolteon_Pin_Missile.png/revision/latest?cb=20160114064711",
             "partner_cap": "Sparky's Jolteon using Pin Missile"},
            {"name": "Virgil", "role": "Eevee specialist, Unova",
             "img": F + "c/cc/Ash_and_Virgil.png/revision/latest?cb=20200701204429",
             "bio": "A member of the Pokémon Rescue Squad whose team is made of Eevee evolutions. Virgil won the Unova League "
                    "(Vertress Conference), and Jolteon was part of his winning team.",
             "partner": F + "2/28/Virgil_Jolteon_Thunderbolt.png/revision/latest?cb=20151001052937",
             "partner_cap": "Virgil's Jolteon using Thunderbolt"},
        ],
        "anime": [
            (F + "6/66/TB040_TC_JA.png/revision/latest?cb=20250614022215",
             "“The Battling Eevee Brothers”: Jolteon's anime debut (Japanese title card)"),
            (F + "6/6c/Eevee_Brother_Sparky.png/revision/latest?cb=20250906045105", "Sparky's Jolteon"),
            (F + "c/cf/BW104_TC_JA.png/revision/latest?cb=20230521224554",
             "BW104 “Team Eevee and the Pokémon Rescue Squad!”: debut of Virgil's Jolteon"),
        ],
        "games_intro": "Jolteon debuted in Generation I. Using a Thunder Stone on Eevee, from Celadon City, evolves it.",
        "games": [
            (F + "7/7f/Pok%C3%A9mon_Red_Version.png/revision/latest?cb=20260621083910", "Pokémon Red (1996 JP / 1998 intl.)"),
            (F + "f/f1/Pok%C3%A9mon_Blue_Version.png/revision/latest?cb=20260621083808", "Pokémon Blue (1996 JP / 1998 intl.)"),
        ],
        "sprite": (SPR.format("versions/generation-i/red-blue/135"), "Original sprite from Red & Blue"),
    },
    {
        "slug": "ceruledge", "name": "Ceruledge", "dex": 937, "types": ["fire", "ghost"], "accent": "fire",
        "evo": [stage("Charcadet", 935), "Malicious Armor", stage("Ceruledge", 937)],
        "evo_note": "With an Auspicious Armor instead, Charcadet evolves into Armarouge.",
        "trainers": [
            {"name": "Amethio", "role": "Member of the Explorers, Pokémon Horizons",
             "img": F + "9/91/Amethio_anime_3.png/revision/latest?cb=20250922215327",
             "bio": "A cool, serious rival of Liko and Roy who first works for the Explorers. He has been with Ceruledge "
                    "since it was a Charcadet in his childhood, and it is his strongest partner.",
             "partner": F + "9/90/Amethio_Ceruledge.png/revision/latest?cb=20230513035349",
             "partner_cap": "Amethio's Ceruledge"},
        ],
        "anime": [
            (F + "7/7b/PH001_TC_JA.png/revision/latest?cb=20230415004920",
             "PH001 “The Pendant That Starts It All”: debut of Amethio's Ceruledge (Japanese title card)"),
            (F + "9/99/Amethio_Ceruledge_Bitter_Blade.png/revision/latest?cb=20230414235410", "Ceruledge using Bitter Blade"),
            (F + "5/59/Ceruledge_and_Armarouge.png/revision/latest?cb=20260419121851", "Ceruledge and Armarouge"),
        ],
        "games_intro": "Ceruledge debuted in Generation IX. It is exclusive to Violet, the version where Charcadet evolves with Malicious Armor.",
        "games": [
            (F + "8/86/Pok%C3%A9mon_Violet.jpg/revision/latest?cb=20240614190434", "Pokémon Violet (2022)"),
        ],
        "sprite": (SPR.format("937"), "In-game sprite"),
    },
]


def e(s):
    return escape(s, quote=True)


def img(src, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{e(src)}" alt="{e(alt)}" loading="lazy" />'


def evo_html(p):
    parts = []
    for item in p["evo"]:
        if isinstance(item, str):
            parts.append(f'<div class="evo-arrow"><span>{e(item)}</span></div>')
        elif isinstance(item, list):
            inner = "".join(evo_stage(s, p) for s in item)
            parts.append(f'<div class="evo-branch">{inner}</div>')
        else:
            parts.append(evo_stage(item, p))
    return "".join(parts)


def evo_stage(s, p):
    current = " evo-stage--current" if s["name"] == p["name"] else ""
    return f'<figure class="evo-stage{current}">{img(s["img"], s["name"])}<figcaption>{e(s["name"])}</figcaption></figure>'


def trainer_html(t):
    return f"""
        <article class="trainer">
          <div class="trainer__portrait">{img(t["img"], t["name"])}</div>
          <div class="trainer__body">
            <h3>{e(t["name"])}</h3>
            <p class="trainer__role">{e(t["role"])}</p>
            <p>{e(t["bio"])}</p>
          </div>
          <figure class="trainer__partner">{img(t["partner"], t["partner_cap"])}<figcaption>{e(t["partner_cap"])}</figcaption></figure>
        </article>"""


def gallery(items, cls):
    return "".join(f'<figure class="{cls}">{img(src, cap)}<figcaption>{e(cap)}</figcaption></figure>' for src, cap in items)


def page(p):
    types = "".join(f'<span class="type {t}">{t.title()}</span>' for t in p["types"])
    if p["trainers"]:
        trainers = "".join(trainer_html(t) for t in p["trainers"])
    else:
        trainers = f'<p class="muted">{e(p["no_trainer_note"])}</p>' + trainer_html(p["featured"])
    note = f'<p class="muted">{e(p["evo_note"])}</p>' if p["evo_note"] else ""
    sprite_src, sprite_cap = p["sprite"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- Wiki images only load when no referrer is sent -->
  <meta name="referrer" content="no-referrer" />
  <title>{e(p["name"])} · Our Favorite Pokémon</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&family=Inter:wght@400;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body class="detail" style="--accent: var(--{p["accent"]})">

  <header class="detail-hero">
    <div class="detail-hero__inner">
      <a class="back" href="../index.html">← All Pokémon</a>
      <div class="detail-hero__main">
        {img(ART.format(p["dex"]), p["name"], "detail-hero__art")}
        <div>
          <span class="dex">#{p["dex"]:04d}</span>
          <h1>{e(p["name"])}</h1>
          <div class="types">{types}</div>
        </div>
      </div>
      <nav class="detail-nav">
        <a href="#evolution">Evolution line</a>
        <a href="#trainers">Trainers</a>
        <a href="#debut">First appearances</a>
      </nav>
    </div>
  </header>

  <main class="detail-main">

    <section id="evolution" class="panel">
      <h2>Evolution Line</h2>
      <div class="evo-line">{evo_html(p)}</div>
      {note}
    </section>

    <section id="trainers" class="panel">
      <h2>Trainers in the Anime</h2>
      {trainers}
    </section>

    <section id="debut" class="panel">
      <h2>First Appearances</h2>

      <h3 class="sub">In the animated series</h3>
      <div class="gallery">{gallery(p["anime"], "shot")}</div>

      <h3 class="sub">In the video games</h3>
      <p class="muted">{e(p["games_intro"])}</p>
      <div class="gallery gallery--games">
        {gallery(p["games"], "boxart")}
        <figure class="boxart sprite">{img(sprite_src, sprite_cap)}<figcaption>{e(sprite_cap)}</figcaption></figure>
      </div>
    </section>

  </main>

  <footer class="footer">
    Pokémon and all related names are trademarks of Nintendo, Game Freak and Creatures.
    Artwork via <a href="https://pokeapi.co">PokeAPI</a> · Anime and box-art images via the
    <a href="https://pokemon.fandom.com">Pokémon Wiki (Fandom)</a>.
  </footer>

</body>
</html>
"""


def main():
    out = Path(__file__).resolve().parent.parent / "pokemon"
    out.mkdir(exist_ok=True)
    for p in DATA:
        (out / f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
        print("wrote", out / f"{p['slug']}.html")


if __name__ == "__main__":
    main()
