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
    out = [f"""<section class="hero hero--concepto">
  <div class="hero__media">{img(lang,'assets/images/hero/hero-tacos-hermanos-'+DOMAIN+'.webp',
       L(lang,"Salón principal de Tacos Hermanos lleno de familias","The main Tacos Hermanos dining room full of families"), priority=True)}</div>
  <div class="wrap hero__inner">
    <span class="eyebrow">{L(lang,"El Salvador · Desde 2021","El Salvador · Since 2021")}</span>
    {concepto(lang)}
    <h1 class="hero__h1">{L(lang,
      "Tacos, desayunos y celebraciones en familia, en seis casas de El Salvador.",
      "Tacos, breakfast and family celebrations, in six houses across El Salvador.")}</h1>
    <div class="hero__quick">
      <a class="is-primary" href="{b('menu')}">{L(lang,"Ver el menú","See the menu")}</a>
      <a href="{b('info')}#horarios">{L(lang,"Horarios","Hours")}</a>
      <a href="{b('info')}">{L(lang,"Sucursales","Locations")}</a>
      <a href="{b('regala')}">{L(lang,"Enviar tacos","Send tacos")}</a>
    </div>
  </div>
</section>"""]

    # --- la esencia
    out.append(f"""<section class="section" aria-labelledby="esencia">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">{L(lang,"La esencia","What we are about")}</span>
      <h2 id="esencia">{L(lang,"Creemos que un saludo puede cambiar una vida","We believe a greeting can change a life")}</h2>
      <p class="lead mt-2">{L(lang,
        "Tacos Hermanos nació como el sueño de hacer un restaurante diferente, un restaurante que cambie vidas. Somos uno, somos la suma de nuestros sueños y de nuestras luchas. El viaje de cada uno se integra al viaje del otro.",
        "Tacos Hermanos was born as the dream of building a different kind of restaurant, one that changes lives. We are one, we are the sum of our dreams and of our struggles. Each person's journey folds into everyone else's.")}</p>
      <p class="mt-2">{L(lang,
        "Son pequeñas cosas que ajustan ángulos chiquitos, pero que a largo plazo tienen efectos bien grandes. Atendemos a miles de personas al día. Hacerlo con amabilidad, con gentileza y con cariño, junto a la mejor comida que podamos servir, es nuestra manera de hacer del mundo un mejor lugar.",
        "They are small things that shift tiny angles, and over the long run those tiny angles have enormous effects. We serve thousands of people every day. Doing it with kindness, with gentleness and with care, alongside the best food we can put on a plate, is our way of making the world a better place.")}</p>
    </div>
    <div class="reveal" data-delay="1">
      <blockquote class="quote">
        <p>{L(lang,
          "Tenemos literalmente una regla de oro en Tacos Hermanos: que cada persona que entra por nuestras puertas viva una experiencia extraordinaria, una experiencia que cambia vidas.",
          "We literally have a golden rule at Tacos Hermanos: every single person who walks through our doors lives an extraordinary experience, an experience that changes lives.")}</p>
        <cite>Tacos Hermanos</cite>
      </blockquote>
      <div class="mt-3">{img(lang, f"assets/images/gallery/servicio-memorable-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Un colaborador de Tacos Hermanos sirviendo un plato","A Tacos Hermanos team member serving a plate"), cls_="")}</div>
    </div>
  </div>
</section>""")

    # --- pilares (positive framing, Erika's own wording, 31 July call)
    P = [("Un producto espectacular","A spectacular product",
          "Nuestro menú está en constante evolución.","Our menu is always evolving.","taco"),
         ("Un servicio memorable","Memorable service",
          "Cada persona que entra vive una experiencia extraordinaria.",
          "Everyone who walks in lives an extraordinary experience.","arco"),
         ("El mejor valor por su dinero","The best value for your money",
          "Que toda la familia coma bien y salga feliz.",
          "The whole family eats well and leaves happy.","tostada")]
    cards = "".join(
      f'<div class="pillar reveal" data-delay="{i}">{icono(lang, ic)}'
      f'<h3 class="mt-1">{L(lang,t_es,t_en)}</h3><p>{L(lang,d_es,d_en)}</p></div>'
      for i,(t_es,t_en,d_es,d_en,ic) in enumerate(P))
    out.append(f"""<section class="section section--tight">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Nuestro modelo","Our model")}</span>
      <h2>{L(lang,"Lo que siempre vas a encontrar aquí","What you will always find here")}</h2>
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
      "Cada sucursal tiene su propio horario.","Each location has its own hours.")}
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
   "Tenemos seis casas: San Benito, La Gran Vía, Paseo Venecia en Soyapango, Las Ramblas en Santa Ana, San Miguel y Plaza Mundo en Usulután. Los horarios exactos de cada sucursal están en la página de Sucursales."),
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
   "We have six houses: San Benito, La Gran Vía, Paseo Venecia in Soyapango, Las Ramblas in Santa Ana, San Miguel, and Plaza Mundo in Usulután. Exact hours for each location are on the Locations page."),
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
        "Somos tres, somos hermanos. Junto a ti, somos invencibles. Y lo mejor de todo es que, sin habernos conocido, ya somos hermanos.",
        "There are three of us, and we are brothers. Together with you, we are unstoppable. And the best part is that, without ever having met, we are already brothers.")}</p>
      <cite>Tacos Hermanos</cite>
    </blockquote>
  </div>
</section>""")

    # --- cultura, verbatim from the client's own Cultura artwork
    out.append(f"""<section class="section band-cream">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"Cultura","Culture")}</span>
    <h2 class="reveal">{L(lang,"Somos uno","We are one")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "Somos uno, somos la suma de nuestros sueños, de nuestras luchas. Somos hermanos. El viaje de cada uno se integra al viaje del otro, coincidimos en la misma cancha, en la misma tierra. La cuidamos entre todos.",
      "We are one, we are the sum of our dreams and of our struggles. We are brothers. Each person's journey folds into everyone else's, we meet on the same field, on the same soil. We look after it together.")}</p>
    <p class="mt-2 reveal">{L(lang,
      "Nuestras acciones siempre afectan a un hermano. Somos conscientes de esta realidad y la honramos con agradecimiento, responsabilidad y alegría. Nuestra victoria personal es la victoria de la empresa. Cuando triunfa uno, triunfamos todos. Juntos, somos invencibles.",
      "What we do always touches a brother. We are aware of that, and we honour it with gratitude, responsibility and joy. A personal victory is a victory for the whole company. When one of us wins, all of us win. Together, we are unstoppable.")}</p>
  </div>
</section>""")

    # --- valores, the five words from their brand book
    VAL = [("Honestidad","Honesty"),("Hermandad","Brotherhood"),("Valentía","Courage"),
           ("Excelencia","Excellence"),("Alegría","Joy")]
    vcards = "".join(f'<div class="card reveal" data-delay="{i%3}"><h3>{L(lang,a,b)}</h3></div>'
                     for i,(a,b) in enumerate(VAL))
    out.append(f"""<section class="section">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Valores","Values")}</span>
      <h2>{L(lang,"Cinco palabras que se sostienen solas","Five words that stand on their own")}</h2>
    </div>
    <div class="grid grid--3">{vcards}</div>
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
      "PENDIENTE DEL CLIENTE: cómo fueron las primeras semanas, los retos del arranque, y qué NO ha cambiado desde el día uno.",
      "PENDING FROM CLIENT: what the first weeks were like, the early challenges, and what has NOT changed since day one."), block=True)}</p>
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
      [f'<a class="btn btn--sun" href="{href(lang,"info")}">{L(lang,"Ver sucursales","See locations")}</a>']))
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
    """The old Info page, rebuilt as Sucursales: a card per branch with its own
    photo, its own opening video and its own hours. Erika asked for exactly this."""
    out = [hero(lang, f"hero-info-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"Fachada de Tacos Hermanos San Benito","The Tacos Hermanos San Benito storefront"),
        L(lang,"Sucursales","Locations"),
        L(lang,"Seis casas en El Salvador","Six houses across El Salvador"),
        L(lang,"Cada una con su propio horario, su propia historia y el día que abrió sus puertas.",
                "Each with its own hours, its own story and the day it opened its doors."),
        [f'<a class="btn btn--primary" href="#horarios">{L(lang,"Ver horarios","See hours")}</a>',
         f'<a class="btn btn--ghost" href="https://www.instagram.com/tacoshermanossv" target="_blank" rel="noopener">Instagram</a>'])]

    out.append(f"""<section class="section" id="horarios" aria-labelledby="sucursales-title">
  <div class="wrap">
    <div class="reveal mb-3">
      <span class="eyebrow">{L(lang,"Nuestras casas","Our houses")}</span>
      <h2 id="sucursales-title">{L(lang,"Dónde encontrarnos y a qué hora","Where to find us, and when")}</h2>
      <p class="lead mt-2">{L(lang,
        "Tocá el play en cualquiera de las casas para ver cómo fue el día que abrimos.",
        "Hit play on any of the houses to see the day we opened it.")}</p>
    </div>
    {sucursal_cards(lang)}
    <p class="price-note mt-3">{pend(L(lang,
      "PENDIENTE DEL CLIENTE: direcciones exactas o links de Google Maps, teléfonos por sucursal, el correo para business inquiries, y los videos de San Benito y Paseo Venecia. Los horarios de La Gran Vía cambian cuando arranquen los desayunos.",
      "PENDING FROM CLIENT: exact addresses or Google Maps links, phone numbers per location, the business inquiries email, and the videos for San Benito and Paseo Venecia. La Gran Vía hours change once breakfast launches."), block=True)}</p>
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
    """Somos Hermanos. Content taken verbatim from the client's own in-store
    stand artwork. The section carries the foundation's blue, not restaurant green."""
    es = lang == "es"
    out = [hero(lang, f"hero-fundacion-tacos-hermanos-{DOMAIN}.webp",
        L(lang,"El equipo de Tacos Hermanos reunido","The Tacos Hermanos team together"),
        L(lang,"Somos Hermanos · Est. 2021","Somos Hermanos · Est. 2021"),
        L(lang,"El mundo es un mejor lugar si nos tratamos como hermanos",
                "The world is a better place when we treat each other like family"),
        L(lang,"Nuestra fundación nace hace cinco años con una firme creencia.",
                "Our foundation was born five years ago out of one firm belief."),
        [f'<a class="btn btn--primary" href="#como-ayudar">{L(lang,"Cómo ser parte","How to take part")}</a>'])]

    out.append(f"""<section class="section band-somos">
  <div class="wrap narrow center">
    <blockquote class="versiculo reveal">
      {L(lang,"&laquo;El que ama a Dios, ame también a su hermano.&raquo;",
              "&laquo;Whoever loves God must also love their brother.&raquo;")}
      <cite>1 Juan 4:21</cite>
    </blockquote>
    <div class="cifras">
      <div class="reveal">
        <span class="cifra__n">+300</span>
        <span class="cifra__t">{L(lang,"canastas donadas todos los domingos del año por Tacos Hermanos",
                                        "aid baskets donated every Sunday of the year by Tacos Hermanos")}</span>
      </div>
      <div class="reveal" data-delay="1">
        <span class="cifra__n">+5</span>
        <span class="cifra__t">{L(lang,"años apoyando a niños que lo necesitan en Sonsonate",
                                        "years supporting children who need it in Sonsonate")}</span>
      </div>
    </div>
  </div>
</section>""")

    # the butterfly effect lives here now, where it belongs
    out.append(f"""<section class="section somos">
  <div class="wrap split">
    <div class="reveal">
      <span class="eyebrow">{L(lang,"Por qué","Why")}</span>
      <h2>{L(lang,"El efecto mariposa","The butterfly effect")}</h2>
      <p class="lead mt-2">{L(lang,
        "Creemos que el movimiento de una mariposa puede afectar el clima al otro lado del mundo. Creemos en las reacciones en cadena: son pequeñas cosas que ajustan ángulos chiquitos, pero que a largo plazo tienen efectos bien grandes.",
        "We believe the movement of a butterfly can change the weather on the other side of the world. We believe in chain reactions: small things that shift tiny angles, and over the long run those tiny angles have enormous effects.")}</p>
      <p class="mt-2">{L(lang,
        "Una canasta cada domingo es uno de esos ángulos chiquitos.",
        "A basket every Sunday is one of those tiny angles.")}</p>
    </div>
    <div class="reveal" data-delay="1">{img(lang, f"assets/images/gallery/equipo-completo-tacos-hermanos-{DOMAIN}.webp",
      L(lang,"Todo el equipo de Tacos Hermanos frente a una de sus casas","The entire Tacos Hermanos team in front of one of their houses"))}</div>
  </div>
</section>""")

    PASOS = [("¡Comprá una canasta de ayuda, o las que quieras!","Buy an aid basket, or as many as you like",
              "En cualquiera de nuestros restaurantes, en caja.","At any of our restaurants, at the till."),
             ("¡Escribile un mensaje a los niños!","Write the children a message",
              "Esa carta les llegará junto con tu canasta.","Your note travels with your basket."),
             ("¡Tu canasta será entregada este domingo!","Your basket is delivered this Sunday",
              "Si tu donación se realiza después del jueves, tu canasta será entregada el siguiente domingo.",
              "If you donate after Thursday, your basket goes out the following Sunday.")]
    pasos = "".join(f'<div class="step reveal" data-delay="{i%3}"><h3>{L(lang,a,b)}</h3><p>{L(lang,c,d)}</p></div>'
                    for i,(a,b,c,d) in enumerate(PASOS))
    out.append(f"""<section class="section band-cream somos" id="como-ayudar">
  <div class="wrap">
    <div class="center reveal mb-3">
      <span class="eyebrow">{L(lang,"Cómo puedo ser parte","How can I take part")}</span>
      <h2>{L(lang,"Tres pasos, y una canasta llega a un niño","Three steps, and a basket reaches a child")}</h2>
    </div>
    <div class="steps">{pasos}</div>
    <p class="price-note center mt-3">{pend(L(lang,
      "PENDIENTE DEL CLIENTE: cuánto cuesta una canasta y qué lleva dentro. Erika confirmó que por contabilidad no se puede facturar la donación en el restaurante, así que la vía en línea queda para la fase dos, junto con las gift cards.",
      "PENDING FROM CLIENT: the price of a basket and what it contains. Erika confirmed that for accounting reasons the donation cannot be invoiced at the restaurant, so an online route waits for phase two, alongside the gift cards."), block=True)}</p>
  </div>
</section>""")

    out.append(f"""<section class="section band-somos">
  <div class="wrap narrow center">
    <p class="lead reveal">{L(lang,
      "Trabajamos de la mano con el programa Escuela Bíblica Dominical, de la Iglesia Bitinia, para entregar estas canastas de ayuda a los niños.",
      "We work hand in hand with the Escuela Bíblica Dominical programme, from Iglesia Bitinia, to get these aid baskets to the children.")}</p>
    <h2 class="mt-3 reveal">{L(lang,"Nada de esto sería posible sin la ayuda de Dios","None of this would be possible without God's help")}</h2>
  </div>
</section>""")

    out.append(cta_band(L(lang,"¿Querés saber más?","Want to know more?"),
      L(lang,"Estamos construyendo el sitio propio de Somos Hermanos. Mientras tanto, escribinos.",
             "We are building the Somos Hermanos site of its own. In the meantime, write to us."),
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
# EMPLEADOS  (unlisted, not in the nav, not in the sitemap, noindex)
# =========================================================================
def empleados(lang):
    es = lang == "es"
    VIS = [("Somos la cadena más grande, fuerte y próspera de comida mexicana en el mundo.",
            "We are the largest, strongest and most prosperous Mexican food chain in the world."),
           ("Multiplicamos nuestro modelo de negocios con éxito, consolidando alianzas idóneas.",
            "We multiply our business model successfully, building the right alliances."),
           ("Generamos bendición y prosperidad a nuestros clientes, colaboradores y aliados.",
            "We generate blessing and prosperity for our guests, our team and our partners."),
           ("Generamos valor real en cada interacción. Innovamos y servimos.",
            "We create real value in every interaction. We innovate and we serve."),
           ("Tacos Hermanos en todo el mundo.","Tacos Hermanos all over the world.")]
    vis = "".join(f'<div class="card reveal" data-delay="{i%3}"><span class="card__num">0{i+1}</span>'
                  f'<p>{L(lang,a,b)}</p></div>' for i,(a,b) in enumerate(VIS))
    VAL = [("Honestidad","Honesty"),("Hermandad","Brotherhood"),("Valentía","Courage"),
           ("Excelencia","Excellence"),("Alegría","Joy")]
    val = "".join(f'<div class="card reveal" data-delay="{i%3}"><h3>{L(lang,a,b)}</h3></div>'
                  for i,(a,b) in enumerate(VAL))
    out = [f"""<section class="section band-dark">
  <div class="wrap narrow center">
    {badge_img(lang)}
    <span class="eyebrow mt-3">{L(lang,"Sólo para el equipo","Team only")}</span>
    <h1 class="mt-1">{L(lang,"Bienvenido a la familia","Welcome to the family")}</h1>
    <p class="lead mt-2">{L(lang,
      "Esta página no aparece en el menú ni en los buscadores. Es para que cualquier persona nueva entienda en cinco minutos quiénes somos y cómo trabajamos.",
      "This page is not in the menu and not in search engines. It exists so anyone new understands who we are and how we work, in five minutes.")}</p>
  </div>
</section>""",
    f"""<section class="section">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"Cultura","Culture")}</span>
    <h2 class="reveal">{L(lang,"Somos uno","We are one")}</h2>
    <p class="lead mt-2 reveal">{L(lang,
      "Somos uno, somos la suma de nuestros sueños, de nuestras luchas. Somos hermanos. El viaje de cada uno se integra al viaje del otro, coincidimos en la misma cancha, en la misma tierra. La cuidamos entre todos. Nuestras acciones siempre afectan a un hermano. Somos conscientes de esta realidad y la honramos con agradecimiento, responsabilidad y alegría. Nuestra victoria personal es la victoria de la empresa. Cuando triunfa uno, triunfamos todos. Juntos, somos invencibles.",
      "We are one, we are the sum of our dreams and of our struggles. We are brothers. Each person's journey folds into everyone else's, we meet on the same field, on the same soil. We look after it together. What we do always touches a brother. We are aware of that, and we honour it with gratitude, responsibility and joy. A personal victory is a victory for the whole company. When one of us wins, all of us win. Together, we are unstoppable.")}</p>
  </div>
</section>""",
    f"""<section class="section band-cream">
  <div class="wrap">
    <div class="center reveal mb-3"><span class="eyebrow">{L(lang,"Visión","Vision")}</span>
      <h2>{L(lang,"A dónde vamos","Where we are going")}</h2></div>
    <div class="grid grid--3">{vis}</div>
    <p class="center mt-3 tagline reveal">{L(lang,"Claridad · Unidad · Propósito · Compromiso · Fe",
                                                   "Clarity · Unity · Purpose · Commitment · Faith")}</p>
  </div>
</section>""",
    f"""<section class="section">
  <div class="wrap">
    <div class="center reveal mb-3"><span class="eyebrow">{L(lang,"Valores","Values")}</span>
      <h2>{L(lang,"Cómo nos comportamos","How we behave")}</h2></div>
    <div class="grid grid--3">{val}</div>
  </div>
</section>""",
    f"""<section class="section band-cream">
  <div class="wrap narrow">
    <span class="eyebrow reveal">{L(lang,"Protocolo de servicio","Service protocol")}</span>
    <h2 class="reveal">{L(lang,"La regla de oro, paso a paso","The golden rule, step by step")}</h2>
    <div class="mt-3 reveal">{pend(L(lang,
      "PENDIENTE DE ERIKA: el protocolo de servicio y el protocolo de bienvenida. Ella los está actualizando porque la versión actual es del año pasado.",
      "PENDING FROM ERIKA: the service protocol and the welcome protocol. She is updating them because the current version is from last year."), block=True)}</div>
  </div>
</section>"""]
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
 "empleados": {
  "es": ("Equipo Tacos Hermanos, cultura, visión y valores",
         "Página interna para el equipo de Tacos Hermanos: nuestra cultura, la visión, los valores y los protocolos de servicio.",
         "cultura Tacos Hermanos, visión, valores, protocolo de servicio"),
  "en": ("Tacos Hermanos team, culture, vision and values",
         "Internal page for the Tacos Hermanos team: our culture, the vision, the values and the service protocols.",
         "Tacos Hermanos culture, vision, values, service protocol")},
 "regala": {
  "es": ("Regala tacos a tu familia en El Salvador",
         "Comprá un voucher desde Estados Unidos y mandalo a tu familia en El Salvador. Diez, veinte o cincuenta dólares que se canjean en cualquiera de nuestras seis casas.",
         "regalar comida El Salvador, voucher restaurante El Salvador, mandar comida a El Salvador, remesas, gift card Tacos Hermanos"),
  "en": ("Gift tacos to your family in El Salvador",
         "Buy a voucher from the United States and send it to your family in El Salvador. Ten, twenty or fifty dollars, redeemable at any of our six houses.",
         "gift food El Salvador, restaurant voucher El Salvador, send food to El Salvador, remittances, Tacos Hermanos gift card")},
}
HEROES = {"empleados":"hero-historia-tacos-hermanos","home":"hero-tacos-hermanos","historia":"hero-historia-tacos-hermanos",
          "menu":"hero-menu-tacos-hermanos","desayunos":"hero-desayunos-tacos-hermanos",
          "almuerzo":"hero-menu-tacos-hermanos","info":"hero-info-tacos-hermanos",
          "fundacion":"hero-fundacion-tacos-hermanos","regala":"hero-regala-tacos-hermanos"}
BODY = {"home":home,"historia":historia,"menu":menu_hub,"desayunos":desayunos,
        "almuerzo":almuerzo,"info":info,"fundacion":fundacion,"regala":regala,
        "empleados":empleados}

def build():
    n = 0
    for key, (es_f, en_f) in PAGES.items():
        for lang, fn in (("es", es_f), ("en", en_f)):
            title, desc, kw = META[key][lang]
            extra = faq_jsonld(FAQ[lang]) if key in ("home", "info") else ""
            if key == "empleados":
                extra += "  <!-- unlisted: not in the nav, not in the sitemap -->\n"
            html = (head(lang, key, title, desc, kw, hero=f"{HEROES[key]}-{DOMAIN}.webp", extra=extra,
                         with_menu=key in ("menu", "desayunos", "almuerzo"),
                         noindex=key == "empleados")
                    + header(lang, key) + BODY[key](lang) + footer(lang, key))
            p = ROOT / fn
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(html, encoding="utf-8")
            n += 1
    print(f"wrote {n} pages")

if __name__ == "__main__":
    build()
