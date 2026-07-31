#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Page bodies + writer for tacoshermanos.com. Run: python3 _source/pages.py"""
import pathlib, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *          # noqa
from menu_data import *      # noqa

W = {}   # (key, lang) -> body html

def L(lang, es, en):  return es if lang == "es" else en

# =========================================================================
# HOME
# =========================================================================
def home(lang):
    es = lang == "es"
    b = lambda k: href(lang, k)
    out = [hero(lang, f"hero-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Salón principal de Tacos Hermanos lleno de familias","The main Tacos Hermanos dining room full of families"),
        L(lang,"El Salvador · Desde 2021","El Salvador · Since 2021"),
        L(lang,'Tacos que se comparten en familia, en seis casas de <span class="hl">El Salvador</span>',
                'Tacos worth sharing with family, in six houses across <span class="hl">El Salvador</span>'),
        L(lang,"Desayunos, tacos, burros y tortas. Un producto espectacular, un servicio memorable y el mejor valor por su dinero.",
                "Breakfast, tacos, burritos and tortas. A spectacular product, memorable service and the best value for your money."),
        [f'<a class="btn btn--primary" href="{b("menu")}">{L(lang,"Ver el menú","See the menu")}</a>',
         f'<a class="btn btn--ghost" href="{b("info")}">{L(lang,"Horarios y ubicaciones","Hours and locations")}</a>'])]

    out.append(marquee(["Lo bonito se comparte", "¡Ya somos hermanos!",
                        L(lang,"Aquí es donde la vida se celebra","This is where life gets celebrated"),
                        "Est. 2021"]))

    # --- la esencia
    out.append(f"""<section class="section" aria-labelledby="esencia">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">{L(lang,"La esencia","What we are about")}</span>
      <h2 id="esencia">{L(lang,"Creemos que un saludo puede cambiar una vida","We believe a greeting can change a life")}</h2>
      <p class="lead mt-2">{L(lang,
        "Tacos Hermanos nació como el sueño de hacer un restaurante diferente, un restaurante que cambie vidas. Creemos en el efecto mariposa: que el movimiento de una mariposa puede afectar el clima al otro lado del mundo, y que las reacciones en cadena son reales.",
        "Tacos Hermanos was born as the dream of building a different kind of restaurant, one that changes lives. We believe in the butterfly effect: that the movement of a butterfly can change the weather on the other side of the world, and that chain reactions are real.")}</p>
      <p class="mt-2">{L(lang,
        "Son pequeñas cosas que ajustan ángulos chiquitos, pero que a largo plazo tienen efectos bien grandes. Atendemos a miles de personas al día. Hacerlo con amabilidad, con gentileza y con cariño, junto a la mejor comida que podamos servir, es nuestra manera de hacer del mundo un mejor lugar.",
        "They are small things that shift tiny angles, and over the long run those tiny angles have enormous effects. We serve thousands of people every day. Doing it with kindness, with gentleness and with care, alongside the best food we can put on a plate, is our way of making the world a better place.")}</p>
    </div>
    <div class="reveal" data-delay="1">
      <blockquote class="quote">
        <p>{L(lang,
          "Tenemos literalmente una regla de oro en Tacos Hermanos: que cada persona que entra por nuestras puertas viva una experiencia extraordinaria, una experiencia que cambia vidas.",
          "We literally have a golden rule at Tacos Hermanos: every single person who walks through our doors lives an extraordinary experience, an experience that changes lives.")}</p>
        <cite>{L(lang,"Alfonso Díaz-Bazán, cofundador","Alfonso Díaz-Bazán, co-founder")}</cite>
      </blockquote>
      <div class="mt-3">{img(lang, f"assets/images/gallery/servicio-memorable-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Un colaborador de Tacos Hermanos sirviendo un plato","A Tacos Hermanos team member serving a plate"), cls_="")}</div>
    </div>
  </div>
</section>""")

    # --- pilares
    P = [(L(lang,"Un producto espectacular","A spectacular product"),
          L(lang,"Nuestro menú está en constante evolución, para sorprender a las familias salvadoreñas.",
                 "Our menu is always evolving, to keep surprising Salvadoran families.")),
         (L(lang,"Un servicio memorable","Memorable service"),
          L(lang,"La regla de oro no es un eslogan. Es lo que medimos todos los días en cada una de las casas.",
                 "The golden rule is not a slogan. It is what we measure every single day in every house.")),
         (L(lang,"El mejor valor por su dinero","The best value for money"),
          L(lang,"Que una familia entera coma bien, se sienta vista y salga diciendo que valió cada centavo.",
                 "A whole family eats well, feels seen, and leaves saying it was worth every cent."))]
    cards = "".join(f'<div class="pillar reveal" data-delay="{i}"><h3>{t}</h3><p>{d}</p></div>'
                    for i,(t,d) in enumerate(P))
    out.append(f"""<section class="section section--tight">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Nuestro modelo","Our model")}</span>
      <h2>{L(lang,"Tres cosas que no negociamos","Three things we do not negotiate")}</h2>
    </div>
    <div class="pillars">{cards}</div>
  </div>
</section>""")

    # --- menú teaser
    out.append(f"""<section class="section band-cream" aria-labelledby="menu-teaser">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"El menú","The menu")}</span>
      <h2 id="menu-teaser">{L(lang,"Se sirven de 4 en 4, y se combinan de 2 en 2","Served four at a time, mixed two and two")}</h2>
      <p class="lead mt-2 narrow">{L(lang,
        "Cada taco tiene su personalidad y todos nos hacen sentir orgullosos. Desde 2026 también servimos desayunos.",
        "Every taco has its own personality and every one of them makes us proud. Since 2026 we also serve breakfast.")}</p>
    </div>
    {dish_photos(lang, [("quesabirrias", L(lang,"Quesabirrias","Quesabirrias")),
                        ("tacos-clasicos", L(lang,"Los clásicos","The classics")),
                        ("burros", L(lang,"Burros","Burritos")),
                        ("bowl-hermano", L(lang,"Bowl Hermano","Bowl Hermano"))])}
    <div class="hero__cta mt-3" style="justify-content:center">
      <a class="btn btn--primary" href="{b('almuerzo')}">{L(lang,"Almuerzo y cena","Lunch and dinner")}</a>
      <a class="btn btn--ghost" href="{b('desayunos')}">{L(lang,"Desayunos","Breakfast")}</a>
    </div>
  </div>
</section>""")

    # --- casas
    rows = "".join(
      f'<div class="timeline__row reveal"><span class="timeline__name">{c[0]}</span>'
      f'<span class="timeline__date">{L(lang,c[1],c[2])}</span>'
      f'<span class="timeline__n">0{i+1}</span></div>' for i,c in enumerate(CASAS))
    out.append(f"""<section class="section" aria-labelledby="casas">
  <div class="wrap">
    <div class="reveal mb-3">
      <span class="eyebrow">{L(lang,"Nuestras casas","Our houses")}</span>
      <h2 id="casas">{L(lang,"En cinco años construimos seis casas en todo el país","In five years we built six houses across the country")}</h2>
      <p class="lead mt-2">{L(lang,
        "Cada una pensada con propósito, donde cada detalle refleja nuestro compromiso con la calidad y la excelencia.",
        "Each one designed with purpose, where every detail reflects our commitment to quality and excellence.")}</p>
    </div>
    <div class="timeline">{rows}</div>
    <p class="price-note">{L(lang,
      "Horarios exactos por sucursal en la página de Info.","Exact hours per location are on the Info page.")}
      <a href="{b('info')}">{L(lang,"Ver horarios","See hours")}</a></p>
  </div>
</section>""")

    # --- regala tacos teaser
    out.append(f"""<section class="section band-dark" aria-labelledby="regala-teaser">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">{L(lang,"Próximamente","Coming soon")}</span>
      <h2 id="regala-teaser">{L(lang,"Mandales tacos, no solo saludos","Send them tacos, not just greetings")}</h2>
      <p class="lead mt-2">{L(lang,
        "Si estás fuera del país, vas a poder comprar un voucher en línea y mandarlo a tu familia en El Salvador. Ellos lo canjean en cualquiera de nuestras casas y se sientan a la mesa por vos.",
        "If you are outside the country, you will be able to buy a voucher online and send it to your family in El Salvador. They redeem it at any of our houses and sit down at the table for you.")}</p>
      <div class="hero__cta mt-3">
        <a class="btn btn--sun" href="{b('regala')}">{L(lang,"Ver cómo funciona","See how it works")}</a>
      </div>
    </div>
    <div class="reveal" data-delay="1">{mapa(lang)}</div>
  </div>
</section>""")

    out.append(faq_block(L(lang,"Preguntas frecuentes","Frequently asked questions"), FAQ[lang]))

    out.append(cta_band(L(lang,"¡Aquí es donde la vida se celebra!","This is where life gets celebrated"),
      L(lang,"Somos el lugar por excelencia para celebrar cumpleaños, días especiales y momentos únicos en familia.",
             "We are the place to celebrate birthdays, special days and unique family moments."),
      [f'<a class="btn btn--sun" href="{b("menu")}">{L(lang,"Ver el menú","See the menu")}</a>',
       f'<a class="btn btn--ghost" href="{b("info")}">{L(lang,"Cómo llegar","Find us")}</a>']))
    return "\n".join(out)

# --- shared FAQ (visible + JSON-LD) --------------------------------------
FAQ = {
 "es": [
  ("¿Tacos Hermanos acepta reservaciones?",
   "No, no manejamos reservaciones en ninguna de nuestras seis casas. Atendemos por orden de llegada. Lo hacemos así para que la mesa que se desocupa sea de quien ya está esperando, y no de quien llamó primero. En horas pico puede haber espera, y vale la pena."),
  ("¿Tacos Hermanos tiene delivery?",
   "No hacemos delivery propio. La razón es simple: queremos estar seguros de que la comida llega a la mesa con nuestro estándar. Cuando un plato pasa a otras manos, se guarda en una caja y viaja por la calle, no podemos garantizar que llegue como salió de la cocina. Preferimos que la primera vez que lo pruebes sea como debe ser."),
  ("¿Dónde están ubicados y a qué hora abren?",
   "Tenemos seis casas: San Benito, La Gran Vía, Paseo Venecia en Soyapango, Las Ramblas en Santa Ana, San Miguel y Plaza Mundo en Usulután. Los horarios exactos de cada sucursal están en la página de Info."),
  ("¿Tacos Hermanos sirve desayunos?",
   "Sí. El menú de desayunos es lo más nuevo de la casa e incluye Súper Típico Hermano, Huevos Rotos, Burro Asado y Tostadas a la Francesa, entre otros. Todos los desayunos incluyen café con refill, un pan artesanal y salsa roja tatemada o salsa verde."),
  ("¿Cuánto cuesta comer en Tacos Hermanos?",
   "Los tacos clásicos cuestan $6.95 por orden de cuatro, los burros arrancan en $7.50 y los desayunos van de $6.95 a $9.95. Una familia completa suele comer bien por alrededor de $30."),
  ("¿Se puede celebrar un cumpleaños en Tacos Hermanos?",
   "Sí, y pasa todos los días. Somos el lugar por excelencia para celebrar cumpleaños, días especiales y momentos únicos en familia. No hace falta avisar, aunque en grupos grandes conviene llegar temprano."),
 ],
 "en": [
  ("Does Tacos Hermanos take reservations?",
   "No, we do not take reservations at any of our six houses. We seat guests in the order they arrive. We do it this way so that the next free table belongs to whoever is already waiting, not to whoever called first. At peak hours there can be a wait, and it is worth it."),
  ("Does Tacos Hermanos deliver?",
   "We do not run our own delivery. The reason is simple: we want to be certain the food reaches the table at our standard. Once a plate passes to other hands, sits in a box and travels down the road, we cannot guarantee it arrives the way it left the kitchen. We would rather your first taste be the way it is meant to be."),
  ("Where are you located and what are your hours?",
   "We have six houses: San Benito, La Gran Vía, Paseo Venecia in Soyapango, Las Ramblas in Santa Ana, San Miguel, and Plaza Mundo in Usulután. Exact hours for each location are on the Info page."),
  ("Does Tacos Hermanos serve breakfast?",
   "Yes. The breakfast menu is the newest thing in the house and includes Súper Típico Hermano, Huevos Rotos, Burro Asado and Tostadas a la Francesa, among others. Every breakfast comes with coffee and free refills, an artisan bread roll, and either roasted red salsa or salsa verde."),
  ("How much does it cost to eat at Tacos Hermanos?",
   "Classic tacos are $6.95 for an order of four, burritos start at $7.50, and breakfasts run from $6.95 to $9.95. A whole family usually eats well for around $30."),
  ("Can I celebrate a birthday at Tacos Hermanos?",
   "Yes, and it happens every single day. We are the place to celebrate birthdays, special days and unique family moments. There is no need to let us know in advance, though larger groups do better arriving early."),
 ]}

# =========================================================================
# NUESTRA HISTORIA
# =========================================================================
def historia(lang):
    es = lang == "es"
    out = [hero(lang, f"hero-historia-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"El equipo completo de Tacos Hermanos frente a una de sus casas","The full Tacos Hermanos team in front of one of their houses"),
        L(lang,"Nuestra historia","Our story"),
        L(lang,"No éramos dos hermanos poniendo un negocio","We were not two brothers opening a business"),
        L(lang,"Éramos hermanos que creían tanto en la filosofía de la hermandad que querían compartirla con el mundo.",
                "We were brothers who believed so much in the philosophy of brotherhood that we wanted to share it with the world."),
        [f'<a class="btn btn--primary" href="{href(lang,"menu")}">{L(lang,"Ver el menú","See the menu")}</a>'])]

    out.append(f"""<section class="section">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"El porqué del nombre","Where the name comes from")}</span>
    <h2 class="reveal">{L(lang,"El nombre no vino del parentesco, vino del trato","The name did not come from blood, it came from how we treat people")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "Sí somos hermanos. Pero el nombre no salió por eso. Salió por el trato de hermanos y la filosofía de hermanos. Lo que para nosotros significaba la hermandad lo queríamos compartir con el mundo.",
      "We are brothers, yes. But the name did not come from that. It came from treating people like family, and from the philosophy behind it. What brotherhood meant to us was something we wanted to share with the world.")}</p>
    <p class="mt-2 reveal">{L(lang,
      "Si logramos que la gente lo entienda, y que la gente se empiece a tratar un poquito más como hermanos, con un poquito más de empatía y un poquito más de cariño, grandes cosas pueden pasar.",
      "If we can get people to understand it, and get people to treat each other a little more like family, with a little more empathy and a little more care, big things can happen.")}</p>

    <blockquote class="quote mt-4 reveal">
      <p>{L(lang,
        "Un saludo bien puesto en el momento correcto puede cambiar una vida. Un abrazo, un oído empático, un buen gesto, puede cambiar el rumbo de una vida.",
        "A greeting placed well at the right moment can change a life. A hug, an empathetic ear, a kind gesture, can change the course of a life.")}</p>
      <cite>{L(lang,"Alfonso Díaz-Bazán, cofundador","Alfonso Díaz-Bazán, co-founder")}</cite>
    </blockquote>
  </div>
</section>""")

    out.append(f"""<section class="section band-cream">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"El principio","The beginning")}</span>
    <h2 class="reveal">{L(lang,"Mayo de 2021, San Benito","May 2021, San Benito")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "La primera casa abrió el 21 de mayo de 2021 en San Benito, San Salvador. En cinco años se convirtieron en seis casas en todo el país.",
      "The first house opened on May 21, 2021 in San Benito, San Salvador. Within five years it became six houses across the country.")}</p>
    <p class="mt-3 reveal">{pend(L(lang,
      "PENDIENTE DEL CLIENTE: cómo fueron las primeras semanas, los retos del arranque, y qué NO ha cambiado desde el día uno. Alfonso y Erika quedaron en escribir este párrafo con sus propias palabras.",
      "PENDING FROM CLIENT: what the first weeks were like, the early challenges, and what has NOT changed since day one. Alfonso and Erika agreed to write this paragraph in their own words."), block=True)}</p>
    <div class="mt-4 reveal">{img(lang, f"assets/images/gallery/equipo-hermanos-tacos-hermanos-{DOMAIN}.webp",
      L(lang,"El equipo de Tacos Hermanos reunido bajo el rótulo","The Tacos Hermanos team gathered under the sign"))}</div>
  </div>
</section>""")

    out.append(f"""<section class="section">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"Para quién","Who it is for")}</span>
    <h2 class="reveal">{L(lang,"Para la familia salvadoreña","For the Salvadoran family")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "Pensamos en ese papá que ahorró para poder traer a toda su familia y escogió un lugar donde todo el valor de su dinero va a ser recompensado. Donde se va a sentir acogido, especial y visto.",
      "We think about the father who saved up to bring his whole family and chose a place where every cent of his money would be repaid. Where he would feel welcomed, special, and seen.")}</p>
    <p class="mt-2 reveal">{L(lang,
      "Que salgan diciendo: comimos riquísimo, con treinta dólares comió toda la familia, nos atendieron bien, nos cantaron el cumpleaños y estuvieron pendientes de nuestra mesa.",
      "So that they leave saying: the food was superb, thirty dollars fed the whole family, we were looked after, they sang happy birthday, and someone was watching over our table the whole time.")}</p>
  </div>
</section>""")

    out.append(f"""<section class="section band-dark">
  <div class="wrap center">
    {badge_img(lang)}
    <p class="lead mt-3 narrow reveal">{L(lang,
      "Aperturamos hace más de cinco años con el propósito de generar bendición y prosperidad para nuestros clientes, colaboradores y aliados. Generamos valor real en cada interacción. Innovamos y servimos.",
      "We opened more than five years ago with the purpose of generating blessing and prosperity for our guests, our team and our partners. We create real value in every interaction. We innovate and we serve.")}</p>
  </div>
</section>""")
    out.append(cta_band(L(lang,"Vení a probarlo","Come and taste it"),
      L(lang,"Seis casas en El Salvador, abiertas todos los días.","Six houses across El Salvador, open every day."),
      [f'<a class="btn btn--sun" href="{href(lang,"info")}">{L(lang,"Ver ubicaciones","See locations")}</a>']))
    return "\n".join(out)

# =========================================================================
# MENU HUB
# =========================================================================
def menu_hub(lang):
    b = lambda k: href(lang, k)
    out = [hero(lang, f"hero-menu-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Tacos parrilleros, al trompo y gobernador servidos en tabla","Parrilleros, trompo and gobernador tacos served on a board"),
        L(lang,"El menú","The menu"),
        L(lang,"El menú completo de Tacos Hermanos","The complete Tacos Hermanos menu"),
        L(lang,"En línea, legible y siempre al día. Sin PDF que descargar.",
                "Online, readable and always current. No PDF to download."),
        [f'<a class="btn btn--primary" href="{b("almuerzo")}">{L(lang,"Almuerzo y cena","Lunch and dinner")}</a>',
         f'<a class="btn btn--ghost" href="{b("desayunos")}">{L(lang,"Desayunos","Breakfast")}</a>'])]

    out.append(f"""<section class="section">
  <div class="wrap">
    {menu_nav(lang,"menu")}
    <div class="grid grid--2">
      <a class="card reveal" href="{b('desayunos')}" style="text-decoration:none">
        <span class="card__num">01</span>
        <h3>{L(lang,"Desayunos","Breakfast")}</h3>
        <p>{L(lang,
          "Lo más nuevo de la casa. Ocho desayunos, de $6.95 a $9.95, todos con café con refill y pan artesanal.",
          "The newest thing in the house. Eight breakfasts, from $6.95 to $9.95, all with bottomless coffee and artisan bread.")}</p>
      </a>
      <a class="card reveal" data-delay="1" href="{b('almuerzo')}" style="text-decoration:none">
        <span class="card__num">02</span>
        <h3>{L(lang,"Almuerzo y cena","Lunch and dinner")}</h3>
        <p>{L(lang,
          "Tacos, burros, tortas, bowls, postres y bebidas. Los tacos clásicos van desde $6.95 la orden de cuatro.",
          "Tacos, burritos, tortas, bowls, desserts and drinks. Classic tacos start at $6.95 for an order of four.")}</p>
      </a>
    </div>
    {dish_photos(lang, [("tacos-dorados", L(lang,"Tacos Dorados","Tacos Dorados")),
                        ("pizza-jalapena", L(lang,"Pizza Jalapeña","Pizza Jalapeña")),
                        ("torta-derretida", L(lang,"Torta Derretida","Torta Derretida")),
                        ("margaritas", L(lang,"Margaritas","Margaritas"))])}
    <p class="price-note">{L(lang,
      "Precios en dólares estadounidenses. El menú está en constante evolución, así que algún plato puede variar según la casa.",
      "Prices in US dollars. The menu is always evolving, so a dish may vary by location.")}</p>
  </div>
</section>""")
    return "\n".join(out)

# =========================================================================
# DESAYUNOS
# =========================================================================
def desayunos(lang):
    out = [hero(lang, f"hero-desayunos-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Desayuno Súper Típico Hermano servido en sartén","Súper Típico Hermano breakfast served in a skillet"),
        L(lang,"Menú","Menu"),
        L(lang,"Desayunos","Breakfast"),
        L(lang,"La mejor forma de comenzar la mañana. Todos incluyen café con refill.",
                "The best way to start the morning. Every one comes with bottomless coffee."),
        [f'<a class="btn btn--primary" href="{href(lang,"almuerzo")}">{L(lang,"Ver almuerzo y cena","See lunch and dinner")}</a>'])]

    incluye = L(lang, DESAYUNOS_INCLUYE_ES, DESAYUNOS_INCLUYE_EN)
    out.append(f"""<section class="section">
  <div class="wrap narrow">
    {menu_nav(lang,"desayunos")}
    <div class="menu-includes reveal"><strong>{L(lang,"Todos nuestros desayunos incluyen:","Every breakfast includes:")}</strong> {incluye}</div>
    {dish_photos(lang, [("super-tipico-hermano", L(lang,"Súper Típico Hermano","Súper Típico Hermano")),
                        ("huevos-rotos", L(lang,"Huevos Rotos","Huevos Rotos")),
                        ("omelette-asado", L(lang,"Omelette Asado","Omelette Asado")),
                        ("tostadas-a-la-francesa", L(lang,"Tostadas a la Francesa","Tostadas a la Francesa"))])}
    <div class="menu-group mt-4">
      <div class="menu-group__head"><h2>{L(lang,"Desayunos","Breakfast")}</h2>
        <span class="menu-group__note">{L(lang,"Servidos por la mañana","Served in the morning")}</span></div>
      {dish_rows(lang, DESAYUNOS)}
    </div>
    <div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Batidos y cremosos","Shakes and cremosos")}</h2></div>
      {dish_photos(lang, [("batido-de-cafe", L(lang,"Batido de Café","Coffee Shake")),
                          ("batidos-y-cremosos", L(lang,"Cremosos","Cremosos")),
                          ("desayuno-completo", L(lang,"El desayuno completo","The full breakfast")),
                          ("desayunos-hermanos", L(lang,"Con horchata","With horchata"))])}
      <div class="mt-3">{drink_list(lang, DESAYUNO_ESPECIALES)}</div>
    </div>
    <div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Bebidas","Drinks")}</h2></div>
      {drink_list(lang, DESAYUNO_BEBIDAS)}
    </div>
    <p class="price-note">{L(lang,
      "Precios en dólares estadounidenses, tomados del menú de desayunos de julio de 2026.",
      "Prices in US dollars, taken from the July 2026 breakfast menu.")}</p>
    <p class="price-note">{pend(L(lang,
      "POR CONFIRMAR CON EL CLIENTE: el horario exacto en que se sirven los desayunos, y en qué sucursales.",
      "TO CONFIRM WITH CLIENT: the exact hours breakfast is served, and at which locations."))}</p>
  </div>
</section>""")
    out.append(cta_band(L(lang,"¿Y para el almuerzo?","And for lunch?"),
      L(lang,"Tacos, burros, tortas, bowls y postres. Todo el menú en línea.",
             "Tacos, burritos, tortas, bowls and desserts. The whole menu, online."),
      [f'<a class="btn btn--sun" href="{href(lang,"almuerzo")}">{L(lang,"Ver almuerzo y cena","See lunch and dinner")}</a>']))
    return "\n".join(out)

# =========================================================================
# ALMUERZO Y CENA
# =========================================================================
def almuerzo(lang):
    out = [hero(lang, f"hero-menu-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Tacos parrilleros, al trompo y gobernador en tabla de madera","Parrilleros, trompo and gobernador tacos on a wooden board"),
        L(lang,"Menú","Menu"),
        L(lang,"Almuerzo y cena","Lunch and dinner"),
        L(lang,"Nuestros tacos los servimos de 4 en 4, y los podés combinar de 2 en 2.",
                "Our tacos are served four at a time, and you can mix them two and two."),
        [f'<a class="btn btn--primary" href="{href(lang,"desayunos")}">{L(lang,"Ver desayunos","See breakfast")}</a>'])]

    body = [menu_nav(lang, "almuerzo")]
    for sec in ALMUERZO:
        note = sec.get(f"note_{lang}") or sec.get("note_es" if lang=="es" else "note_en")
        note_html = f'<div class="menu-includes reveal">{note}</div>' if note else ""
        photos = dish_photos(lang, [(s, c) for s, c in sec["photos"]]) if sec.get("photos") else ""
        body.append(f"""<div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang, sec['es'], sec['en'])}</h2></div>
      {note_html}
      {photos}
      <div class="mt-3">{dish_rows(lang, sec['items'])}</div>
    </div>""")
    body.append(f"""<div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Margaritas","Margaritas")}</h2>
        <span class="menu-group__note">{L(lang,"Estas llegan al alma","These ones reach the soul")}</span></div>
      {drink_list(lang, MARGARITAS)}
    </div>
    <div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Frozens","Frozens")}</h2></div>
      {drink_list(lang, FROZENS)}
    </div>
    <div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Cervezas","Beers")}</h2></div>
      {drink_list(lang, CERVEZAS)}
    </div>
    <div class="menu-group">
      <div class="menu-group__head"><h2>{L(lang,"Bebidas","Drinks")}</h2></div>
      {drink_list(lang, BEBIDAS_MAIN)}
    </div>
    <p class="price-note">{L(lang,
      "Precios en dólares estadounidenses, tomados del menú impreso de Tacos Hermanos.",
      "Prices in US dollars, taken from the printed Tacos Hermanos menu.")}</p>""")

    out.append('<section class="section"><div class="wrap narrow">' + "\n".join(body) + "</div></section>")
    out.append(cta_band(L(lang,"Vení con toda la familia","Bring the whole family"),
      L(lang,"Seis casas en El Salvador. Sin reservaciones, por orden de llegada.",
             "Six houses across El Salvador. No reservations, first come first served."),
      [f'<a class="btn btn--sun" href="{href(lang,"info")}">{L(lang,"Ver ubicaciones","See locations")}</a>']))
    return "\n".join(out)

# =========================================================================
# INFO
# =========================================================================
def info(lang):
    cards = "".join(
      f"""<div class="card loc reveal" data-delay="{i%3}">
        <h3>{c[0]}</h3>
        <span class="loc__meta">{c[4]}</span>
        <span class="loc__meta">{pend(L(lang,"Horario por confirmar","Hours to confirm"))}</span>
        <span class="loc__since">{L(lang,"Desde el "+c[1], "Since "+c[2])}</span>
      </div>""" for i,c in enumerate(CASAS))
    out = [hero(lang, f"hero-info-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Fachada de Tacos Hermanos San Benito","The Tacos Hermanos San Benito storefront"),
        L(lang,"Info","Info"),
        L(lang,"Horarios, ubicaciones y todo lo que preguntan","Hours, locations and everything people ask"),
        L(lang,"Seis casas en El Salvador. Sin reservaciones y sin delivery, y aquí explicamos por qué.",
                "Six houses across El Salvador. No reservations and no delivery, and here is why."),
        [f'<a class="btn btn--primary" href="https://www.instagram.com/tacoshermanossv" target="_blank" rel="noopener">Instagram</a>'])]

    out.append(f"""<section class="section">
  <div class="wrap">
    <div class="reveal mb-3">
      <span class="eyebrow">{L(lang,"Nuestras casas","Our houses")}</span>
      <h2>{L(lang,"Dónde encontrarnos","Where to find us")}</h2>
    </div>
    <div class="grid grid--3">{cards}</div>
    <p class="price-note mt-3">{pend(L(lang,
      "PENDIENTE DEL CLIENTE: direcciones exactas o links de Google Maps, horarios por sucursal, teléfonos de contacto y el correo para business inquiries.",
      "PENDING FROM CLIENT: exact addresses or Google Maps links, hours per location, contact phone numbers and the business inquiries email."), block=True)}</p>
  </div>
</section>""")
    out.append(faq_block(L(lang,"Preguntas frecuentes","Frequently asked questions"), FAQ[lang]))
    out.append(cta_band(L(lang,"¿Sos empresa o querés una franquicia?","Are you a business, or interested in a franchise?"),
      L(lang,"Nunca cerramos las puertas. Escribinos y lo conversamos.",
             "We never close the door. Write to us and let us talk."),
      [f'<a class="btn btn--sun" href="https://www.instagram.com/tacoshermanossv" target="_blank" rel="noopener">{L(lang,"Escribinos por Instagram","Message us on Instagram")}</a>']))
    return "\n".join(out)

# =========================================================================
# FUNDACIÓN
# =========================================================================
def fundacion(lang):
    out = [hero(lang, f"hero-fundacion-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"El equipo de Tacos Hermanos reunido","The Tacos Hermanos team together"),
        L(lang,"La Fundación","The Foundation"),
        L(lang,"El efecto mariposa, fuera del restaurante","The butterfly effect, beyond the restaurant"),
        L(lang,"La misma filosofía que aplicamos en cada mesa, llevada un paso más allá.",
                "The same philosophy we apply at every table, taken one step further."),
        [])]
    out.append(f"""<section class="section">
  <div class="wrap narrow">
    <p class="lead reveal">{L(lang,
      "Tacos Hermanos tiene una fundación. Nació de la misma idea que el restaurante: que las pequeñas acciones, repetidas todos los días, cambian el rumbo de una vida.",
      "Tacos Hermanos has a foundation. It was born from the same idea as the restaurant: that small actions, repeated every day, change the course of a life.")}</p>
    <div class="mt-3 reveal">{pend(L(lang,
      "PENDIENTE DEL CLIENTE: el nombre oficial de la fundación, qué hace exactamente, a quiénes ha ayudado y en qué números, y cómo una persona o una empresa puede colaborar o donar. Con dos o tres párrafos y un par de datos concretos esta página queda lista.",
      "PENDING FROM CLIENT: the foundation's official name, exactly what it does, who it has helped and in what numbers, and how a person or a company can support or donate. Two or three paragraphs plus a couple of concrete figures and this page is ready."), block=True)}</div>
    <div class="mt-4 reveal">{img(lang, f"assets/images/gallery/equipo-completo-tacos-hermanos-{DOMAIN}.webp",
      L(lang,"Todo el equipo de Tacos Hermanos frente a una de sus casas","The entire Tacos Hermanos team in front of one of their houses"))}</div>
  </div>
</section>""")
    out.append(cta_band(L(lang,"¿Querés apoyar?","Want to help?"),
      L(lang,"Escribinos por Instagram mientras publicamos los datos completos de la fundación.",
             "Message us on Instagram while we publish the foundation's full details."),
      [f'<a class="btn btn--sun" href="https://www.instagram.com/tacoshermanossv" target="_blank" rel="noopener">Instagram</a>']))
    return "\n".join(out)

# =========================================================================
# REGALA TACOS  (phase two)
# =========================================================================
def regala(lang):
    es = lang == "es"
    cards = []
    for amt, t_es, t_en, d_es, d_en, feat in VOUCHERS:
        flag = f'<span class="voucher__flag">{L(lang,"El más regalado","Most gifted")}</span>' if feat else ""
        cards.append(f"""<div class="voucher reveal{' voucher--featured' if feat else ''}">
        {flag}
        <span class="voucher__amount">${amt}</span>
        <span class="voucher__title">{L(lang,t_es,t_en)}</span>
        <span class="voucher__for">{L(lang,d_es,d_en)}</span>
        <button class="btn btn--primary" type="button" disabled aria-disabled="true">{L(lang,"Regalar $"+amt,"Gift $"+amt)}</button>
      </div>""")
    steps = [(L(lang,"Elegís el monto","Pick the amount"),
              L(lang,"Diez dólares para una persona, veinte para una pareja, cincuenta para toda la familia.",
                     "Ten dollars for one person, twenty for two, fifty for the whole family.")),
             (L(lang,"Ponés a quién se lo mandás","Say who it is for"),
              L(lang,"Su nombre, su número o su correo, y un mensaje tuyo si querés.",
                     "Their name, their number or their email, and a message from you if you want.")),
             (L(lang,"Les llega el voucher","The voucher arrives"),
              L(lang,"Con un código que pueden mostrar desde el celular.",
                     "With a code they can show straight from their phone.")),
             (L(lang,"Se sientan a la mesa","They sit down to eat"),
              L(lang,"Lo canjean en cualquiera de nuestras seis casas en El Salvador.",
                     "They redeem it at any of our six houses in El Salvador."))]
    steps_html = "".join(f'<div class="step reveal" data-delay="{i%3}"><h3>{t}</h3><p>{d}</p></div>'
                         for i,(t,d) in enumerate(steps))

    out = [hero(lang, f"hero-regala-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Familias salvadoreñas compartiendo la mesa en Tacos Hermanos","Salvadoran families sharing a table at Tacos Hermanos"),
        L(lang,"Próximamente","Coming soon"),
        L(lang,'Mandales tacos a tu familia en <span class="hl">El Salvador</span>',
                'Send tacos to your family in <span class="hl">El Salvador</span>'),
        L(lang,"Igual que una remesa, pero llega a la mesa. Vos lo comprás desde donde estés y ellos lo canjean en cualquiera de nuestras seis casas.",
                "Just like a remittance, except it arrives at the table. You buy it from wherever you are and they redeem it at any of our six houses."),
        [f'<a class="btn btn--primary" href="#vouchers">{L(lang,"Ver los vouchers","See the vouchers")}</a>'])]

    out.append(f"""<section class="section">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Cómo funciona","How it works")}</span>
      <h2>{L(lang,"De tu celular a su mesa","From your phone to their table")}</h2>
    </div>
    {mapa(lang)}
    <div class="steps mt-4">{steps_html}</div>
  </div>
</section>""")

    out.append(f"""<section class="section band-cream" id="vouchers" aria-labelledby="vouchers-title">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Los vouchers","The vouchers")}</span>
      <h2 id="vouchers-title">{L(lang,"Tres formas de sentarte con ellos","Three ways to sit down with them")}</h2>
    </div>
    <div class="voucher-grid">{''.join(cards)}</div>
    <p class="price-note center mt-3">{pend(L(lang,
      "FASE 2: los botones están desactivados a propósito. La compra en línea se construye después de que el sitio esté publicado. Falta definir la pasarela de pago, el formato del código y cómo se canjea en caja.",
      "PHASE 2: the buttons are disabled on purpose. Online purchase gets built after the site goes live. Still to define: the payment gateway, the code format, and how it is redeemed at the till."), block=True)}</p>
  </div>
</section>""")

    out.append(f"""<section class="section band-dark">
  <div class="wrap narrow center">
    {badge_img(lang)}
    <h2 class="mt-3 reveal">{L(lang,"Lo bonito se comparte","Beautiful things are meant to be shared")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "Miles de salvadoreños mandan dinero a casa todos los meses. Esto es lo mismo, pero termina en una mesa llena, con el cumpleaños cantado y toda la familia junta.",
      "Thousands of Salvadorans send money home every month. This is the same thing, except it ends at a full table, with the birthday song sung and the whole family together.")}</p>
  </div>
</section>""")
    return "\n".join(out)

# =========================================================================
# assemble
# =========================================================================
META = {
 "home": {
  "es": ("Tacos Hermanos, tacos y desayunos en El Salvador",
         "¿Buscás dónde comer tacos en familia en El Salvador? Seis casas, desayunos desde $6.95 y el mejor valor por su dinero. Mirá el menú completo en línea.",
         "tacos El Salvador, Tacos Hermanos, restaurante tacos San Salvador, desayunos El Salvador, quesabirrias, tacos San Benito, La Gran Vía, Santa Ana, San Miguel, Usulután"),
  "en": ("Tacos Hermanos, tacos and breakfast in El Salvador",
         "Looking for tacos with the family in El Salvador? Six locations, breakfast from $6.95 and the best value for money. See the full menu online.",
         "tacos El Salvador, Tacos Hermanos, taco restaurant San Salvador, breakfast El Salvador, quesabirrias, San Benito, La Gran Via")},
 "historia": {
  "es": ("Nuestra historia, Tacos Hermanos desde 2021",
         "Cómo nació Tacos Hermanos: el efecto mariposa, la regla de oro y por qué el nombre no vino del parentesco sino del trato. La historia contada por sus fundadores.",
         "historia Tacos Hermanos, fundadores, efecto mariposa, regla de oro, restaurante salvadoreño"),
  "en": ("Our story, Tacos Hermanos since 2021",
         "How Tacos Hermanos began: the butterfly effect, the golden rule, and why the name came from how we treat people, not from blood. Told by the founders.",
         "Tacos Hermanos story, founders, butterfly effect, golden rule, Salvadoran restaurant")},
 "menu": {
  "es": ("Menú Tacos Hermanos, precios y platos completos",
         "Todo el menú de Tacos Hermanos en línea: tacos desde $6.95, burros, tortas, bowls, postres y desayunos. Precios actualizados, sin PDF que descargar.",
         "menú Tacos Hermanos, precios tacos El Salvador, carta, quesabirrias precio, burros, desayunos"),
  "en": ("Tacos Hermanos menu, full dishes and prices",
         "The complete Tacos Hermanos menu online: tacos from $6.95, burritos, tortas, bowls, desserts and breakfast. Current prices, no PDF to download.",
         "Tacos Hermanos menu, taco prices El Salvador, quesabirrias price, burritos, breakfast")},
 "desayunos": {
  "es": ("Menú de desayunos, Tacos Hermanos El Salvador",
         "Desayunos en Tacos Hermanos desde $6.95: Súper Típico Hermano, Huevos Rotos, Burro Asado y más. Todos con café con refill y pan artesanal.",
         "desayunos El Salvador, desayuno típico salvadoreño, huevos rotos, Tacos Hermanos desayuno, café con refill"),
  "en": ("Breakfast menu, Tacos Hermanos El Salvador",
         "Breakfast at Tacos Hermanos from $6.95: Super Tipico Hermano, Huevos Rotos, Burro Asado and more. All with bottomless coffee and artisan bread.",
         "breakfast El Salvador, Salvadoran breakfast, huevos rotos, Tacos Hermanos breakfast")},
 "almuerzo": {
  "es": ("Menú de almuerzo y cena, Tacos Hermanos",
         "Tacos desde $6.95 la orden de cuatro, quesabirrias, burros, tortas, bowls y postres. El menú completo de almuerzo y cena de Tacos Hermanos, en línea.",
         "tacos precio El Salvador, quesabirrias, burro de birria, torta derretida, el machete, bowl hermano, margaritas"),
  "en": ("Lunch and dinner menu, Tacos Hermanos",
         "Tacos from $6.95 for an order of four, quesabirrias, burritos, tortas, bowls and desserts. The full Tacos Hermanos lunch and dinner menu, online.",
         "taco prices El Salvador, quesabirrias, birria burrito, torta derretida, el machete, bowl hermano")},
 "info": {
  "es": ("Horarios, ubicaciones y contacto, Tacos Hermanos",
         "Las seis casas de Tacos Hermanos en El Salvador, sus horarios y por qué no manejamos reservaciones ni delivery. Todo lo que la gente pregunta, respondido.",
         "Tacos Hermanos ubicaciones, horarios, San Benito, La Gran Vía, Soyapango, Santa Ana, San Miguel, Usulután, reservaciones, delivery"),
  "en": ("Hours, locations and contact, Tacos Hermanos",
         "The six Tacos Hermanos houses in El Salvador, their hours, and why we do not take reservations or deliver. Everything people ask, answered.",
         "Tacos Hermanos locations, hours, San Benito, La Gran Via, Soyapango, Santa Ana, San Miguel, Usulutan")},
 "fundacion": {
  "es": ("La Fundación Tacos Hermanos",
         "Tacos Hermanos tiene una fundación, nacida de la misma idea que el restaurante: las pequeñas acciones repetidas cambian el rumbo de una vida. Conocé su labor.",
         "fundación Tacos Hermanos, labor social El Salvador, donaciones, responsabilidad social"),
  "en": ("The Tacos Hermanos Foundation",
         "Tacos Hermanos has a foundation, born from the same idea as the restaurant: small actions, repeated, change the course of a life. See what it does.",
         "Tacos Hermanos foundation, social work El Salvador, donations")},
 "regala": {
  "es": ("Regala tacos a tu familia en El Salvador",
         "Comprá un voucher desde Estados Unidos y mandalo a tu familia en El Salvador. Diez, veinte o cincuenta dólares que se canjean en cualquiera de nuestras seis casas.",
         "regalar comida El Salvador, voucher restaurante El Salvador, mandar comida a El Salvador, remesas, gift card Tacos Hermanos"),
  "en": ("Gift tacos to your family in El Salvador",
         "Buy a voucher from the United States and send it to your family in El Salvador. Ten, twenty or fifty dollars, redeemable at any of our six houses.",
         "gift food El Salvador, restaurant voucher El Salvador, send food to El Salvador, remittances, Tacos Hermanos gift card")},
}
HEROES = {"home":"hero-tacos-hermanos","historia":"hero-historia-tacos-hermanos",
          "menu":"hero-menu-tacos-hermanos","desayunos":"hero-desayunos-tacos-hermanos",
          "almuerzo":"hero-menu-tacos-hermanos","info":"hero-info-tacos-hermanos",
          "fundacion":"hero-fundacion-tacos-hermanos","regala":"hero-regala-tacos-hermanos"}
BODY = {"home":home,"historia":historia,"menu":menu_hub,"desayunos":desayunos,
        "almuerzo":almuerzo,"info":info,"fundacion":fundacion,"regala":regala}

def build():
    n = 0
    for key, (es_f, en_f) in PAGES.items():
        for lang, fn in (("es", es_f), ("en", en_f)):
            title, desc, kw = META[key][lang]
            extra = faq_jsonld(FAQ[lang]) if key in ("home", "info") else ""
            html = (head(lang, key, title, desc, kw, hero=f"{HEROES[key]}-{DOMAIN}.webp", extra=extra,
                         with_menu=key in ("menu", "desayunos", "almuerzo"))
                    + header(lang, key) + BODY[key](lang) + footer(lang, key))
            p = ROOT / fn
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(html, encoding="utf-8")
            n += 1
    print(f"wrote {n} pages")

if __name__ == "__main__":
    build()
