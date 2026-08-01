# -*- coding: utf-8 -*-
"""
Menu data for tacoshermanos.com

Spanish is transcribed VERBATIM from the client's own printed menus:
  · "Tacos Hermanos - Menu2025" (24 pages, main menu)
  · "22 de julio PM - menu de desayunos" (July 2026 breakfast menu)
Every page of both PDFs was read visually and checked twice, including which
price belongs to which dish, because the printed layout puts the price to the
left of the name on some pages and to the right on others.

English is a natural translation. Dish names stay in Spanish on purpose: they
are the brand's own vocabulary, they are what people search for, and Erika
asked for exactly this on the 31 July call ("los nombres sí que queden como
papa taquera, no es como que la puedes traducir, pero las descripciones están
super bien").

STRUCTURE. Each section holds a list of BLOCKS. A block is one photograph plus
the dishes that photograph actually shows. The site renders the photo and then
that block's dishes directly underneath it, which is the layout Nelson and
Erika agreed on the call, instead of cutting dishes out of shared photos.

Prices are USD, exactly as printed. Change a price here and it updates the menu
page, the JSON-LD Menu node and llms-full.txt at once.
"""

D = "tacoshermanos.com"

def photo(slug):
    return f"assets/images/menu/{slug}-tacos-hermanos-{D}.webp"

# =========================================================================
# ALMUERZO Y CENA  (main menu, 24 printed pages)
# =========================================================================
ALMUERZO = [
 {
  "id": "compartir",
  "es": "Para compartir", "en": "To share",
  "note_es": "¡Al centro y para compartir! Donde come uno, comen todos.",
  "note_en": "Straight to the middle of the table. Where one eats, everyone eats.",
  "blocks": [
   {"photo": "tacos-dorados", "cap_es": "Tacos Dorados", "cap_en": "Tacos Dorados", "items": [
     {"n":"Tacos Dorados","p":"8.95",
      "es":"Crujientes, dorados y rellenos de pollo chipotle con papa. Coronados con chicharrones adobados, cebolla morada curtida, queso rallado, crema y cilantro fresco. Acompañados de nuestra espectacular salsa verde.",
      "en":"Crispy, golden and filled with chipotle chicken and potato. Crowned with marinated chicharrones, pickled red onion, grated cheese, cream and fresh coriander. Served with our spectacular salsa verde."}]},

   {"photo": "sopa-de-tortilla-y-nachos-elegantes",
    "cap_es": "Sopa de Tortilla y Nachos Elegantes", "cap_en": "Sopa de Tortilla and Nachos Elegantes", "items": [
     {"n":"Sopa de Tortilla","p":"5.50",
      "es":"Nuestro caldo familiar, aguacate, tortilla crocante, queso fundido y jardín de cilantro.",
      "en":"Our family broth, avocado, crispy tortilla, melted cheese and a garden of coriander."},
     {"n":"Nachos Elegantes","p":"5.50",
      "es":"Receta familiar, única y celebrada por todos. Cada nacho viene armado y lleno de sabor: pollo chipotle, frijoles hermanos, crema, aguacate y pico de gallo.",
      "en":"A family recipe, one of a kind and loved by everyone. Every nacho comes built and full of flavour: chipotle chicken, frijoles hermanos, cream, avocado and pico de gallo."}]},

   {"photo": "esquite-y-nachos-hermanos",
    "cap_es": "Esquite y Nachos Hermanos", "cap_en": "Esquite and Nachos Hermanos", "items": [
     {"n":"Esquite","p":"4.95",
      "es":"Maíz dulce salteado en mantequilla, mayo chipotle, queso rallado, limón y Tajín. ¡Este esquite, anda en todo!",
      "en":"Sweet corn sauteed in butter, chipotle mayo, grated cheese, lime and Tajín. This esquite goes with absolutely everything."},
     {"n":"Nachos Hermanos","p":"8.95",
      "es":"¡Donde come uno, comen todos! Nachos crocantes, frijoles, salsa de aguacate, queso rallado, crema chipotle y la carne de tu elección.",
      "en":"Where one eats, everyone eats. Crispy nachos, beans, avocado sauce, grated cheese, chipotle cream and the meat of your choice.",
      "hint_es":"Elige tu carne favorita.","hint_en":"Choose your favourite meat."}]},

   {"photo": "pizza-jalapena", "cap_es": "Pizza Jalapeña", "cap_en": "Pizza Jalapeña", "items": [
     {"n":"Pizza Jalapeña","p":"9.95",
      "es":"¡Al centro y para compartir! Nuestra asada, jalapeños, aguacate, cebolla salteada, crema jalapeña, nuestra mezcla de queso gratinado, frijoles y cilantro. Sobre una base crocante de harina.",
      "en":"Straight to the middle of the table. Our grilled steak, jalapeños, avocado, sauteed onion, jalapeño cream, our gratinated cheese blend, beans and coriander, on a crispy flour base.",
      "hint_es":"Sí, le puedes quitar el jalapeño.","hint_en":"Yes, you can ask for it without the jalapeño."}]},

   {"photo": "papas-taqueras", "cap_es": "Papas Taqueras", "cap_en": "Papas Taqueras", "items": [
     {"n":"Papas Taqueras","p":"8.95",
      "es":"¡Celebradas por todos los hermanos! Papas crocantes sazonadas, queso rallado, salsa chipotle, cebolla dulce, jardín de cilantro y la carne de tu elección.",
      "en":"Celebrated by every hermano. Crispy seasoned potatoes, grated cheese, chipotle sauce, sweet onion, a garden of coriander and the meat of your choice.",
      "hint_es":"Asada · Carnitas Mita Mita · Jalada","hint_en":"Asada · Carnitas Mita Mita · Jalada"}]},

   {"photo": "papa-asada", "cap_es": "Papa Asada", "cap_en": "Papa Asada", "items": [
     {"n":"Papa Asada","p":"8.95",
      "es":"¡Tal como la soñamos! Papa asada con mantequilla, queso y crema jalapeña. Servida con asada, pastor, cebolla parrillera, guacamole y nachos crocantes.",
      "en":"Exactly as we dreamed it. Baked potato with butter, cheese and jalapeño cream. Served with grilled steak, pastor, grilled onion, guacamole and crispy nachos."}]},
  ]},

 {
  "id": "tacos",
  "es": "Tacos", "en": "Tacos",
  "note_es": "Nuestros tacos los servimos de 4 en 4. Los puedes combinar de 2 en 2. Cada taco tiene su personalidad, todos nos hacen sentir orgullosos.",
  "note_en": "Our tacos are served four at a time. You can mix them two and two. Every taco has its own personality, and every one of them makes us proud.",
  "blocks": [
   {"photo": "tacos-clasicos", "cap_es": "Los clásicos, todos a 6.95", "cap_en": "The classics, all at 6.95", "items": [
     {"n":"Asada","p":"6.95",
      "es":"¡A la parrilla, jugosa y bien hecha! Servidos con queso, guacamole, cebolla y cilantro.",
      "en":"Off the grill, juicy and done right. Served with cheese, guacamole, onion and coriander."},
     {"n":"Carnitas Mita Mita","p":"6.95",
      "es":"Mitad carnitas, mitad chicharrón ¡Así, nos gusta a los hermanos! Acompañado de guacamole, cebolla y cilantro.",
      "en":"Half carnitas, half chicharrón. That is how we hermanos like it. Served with guacamole, onion and coriander."},
     {"n":"Pastor","p":"6.95",
      "es":"¡Un pastor muy bien logrado! Enamora de taco en taco y se sirve con piña asada, cebolla y jardín de cilantro.",
      "en":"A pastor done properly. It wins you over taco by taco, served with grilled pineapple, onion and a garden of coriander."},
     {"n":"Pollo Chipotle","p":"6.95",
      "es":"Nuestro pollo anda en todo, jugoso y lleno de sabor, servido con guacamole y pico de gallo. ¡Todos los que lo prueban regresan!",
      "en":"Our chicken goes with everything, juicy and full of flavour, served with guacamole and pico de gallo. Everyone who tries it comes back."},
     {"n":"Jalada","p":"6.95",
      "es":"Cerdo jalado, cebolla morada curtida y guacamole… Una receta familiar de los hermanos.",
      "en":"Pulled pork, pickled red onion and guacamole. A family recipe from the hermanos."}]},

   {"photo": "tacos-fundidos", "cap_es": "Fundidos", "cap_en": "Fundidos", "items": [
     {"n":"Fundidos","p":"7.95",
      "es":"Nuestros tacos con costra de tres quesos y tu carne favorita.",
      "en":"Our tacos with a three-cheese crust and your favourite meat.",
      "hint_es":"Puedes combinarlos de 2 en 2.","hint_en":"You can mix them two and two."}]},

   {"photo": "tacos-de-costilla-y-emperador",
    "cap_es": "Los de Costilla y Tacos Emperador", "cap_en": "Los de Costilla and Tacos Emperador", "items": [
     {"n":"Los de Costilla","p":"9.95",
      "es":"¡Una libra de costilla St. Louis! Servidos sobre una cama de guacamole, coronados con cilantro y cebolla morada curtida.",
      "en":"A full pound of St. Louis ribs. Served on a bed of guacamole, crowned with coriander and pickled red onion."},
     {"n":"Tacos Emperador","p":"8.95",
      "es":"¡Los tacos más esperados! Tortilla de harina, asada, camarones al chipotle, costra de quesos, guacamole, tortilla crocante y cilantro.",
      "en":"The most anticipated tacos of all. Flour tortilla, grilled steak, chipotle shrimp, cheese crust, guacamole, crispy tortilla and coriander."}]},

   {"photo": "tacos-parrilleros-trompo-gobernador",
    "cap_es": "Parrilleros, al Trompo y Gobernador", "cap_en": "Parrilleros, al Trompo and Gobernador", "items": [
     {"n":"Tacos Parrilleros","p":"8.95",
      "es":"¡Lo mejor de la parrilla en un taco! Chorizo gaucho, asada, aguacate, cebolla parrillera, costra de quesos y crema jalapeña.",
      "en":"The best of the grill in one taco. Gaucho chorizo, grilled steak, avocado, grilled onion, cheese crust and jalapeño cream."},
     {"n":"Tacos al Trompo","p":"8.95",
      "es":"¡Al trompo y con estilo! Pastor, piña asada envuelta en tocino, guacamole y costra de quesos.",
      "en":"Off the trompo and with style. Pastor, grilled pineapple wrapped in bacon, guacamole and a cheese crust."},
     {"n":"Tacos Gobernador","p":"8.95",
      "es":"¡Ustedes los hicieron famosos! Camarones dorados, costra de quesos, mayo chipotle, cebolla salteada, tortilla crocante y cilantro.",
      "en":"You made these famous. Golden shrimp, cheese crust, chipotle mayo, sauteed onion, crispy tortilla and coriander."}]},

   {"photo": "quesabirrias", "cap_es": "Quesabirrias", "cap_en": "Quesabirrias", "items": [
     {"n":"Quesabirrias","p":"8.95",
      "es":"¡Receta famosa de Tacos Hermanos! Cuatro tacos hechos con nuestra birria de res, costra de tres quesos y caldo para chuponear que llega al alma…",
      "en":"The famous Tacos Hermanos recipe. Four tacos made with our beef birria, a three-cheese crust and broth for dipping that reaches the soul."}]},

   {"photo": "tacos-banados", "cap_es": "Tacos Bañados", "cap_en": "Tacos Bañados", "items": [
     {"n":"Tacos Bañados","p":"9.95",
      "es":"¡Bañados en nuestra espectacular salsa verde! Tortillas de maíz con tu carne favorita, frijoles hermanos, aguacate y queso gratinado. Coronados con cebolla morada, jalapeño, queso rallado y jardín de cilantro.",
      "en":"Bathed in our spectacular salsa verde. Corn tortillas with your favourite meat, frijoles hermanos, avocado and gratinated cheese. Crowned with red onion, jalapeño, grated cheese and a garden of coriander.",
      "hint_es":"Elige tu carne favorita.","hint_en":"Choose your favourite meat."}]},
  ]},

 {
  "id": "burros",
  "es": "Burros, tortas y quesadillas", "en": "Burritos, tortas and quesadillas",
  "note_es": "Nuestras carnes: Carnitas Mita y Mita · Asada · Pastor · Pollo Chipotle · Jalada",
  "note_en": "Our meats: Carnitas Mita y Mita · Asada · Pastor · Pollo Chipotle · Jalada",
  "blocks": [
   {"photo": "torta-birria-y-burro-de-birria",
    "cap_es": "Torta Birria y Burro de Birria", "cap_en": "Torta Birria and Burro de Birria", "items": [
     {"n":"Torta Birria","p":"9.95",
      "es":"¡Para chuponear! Birria de res, frijoles hermanos, mayo chipotle, guacamole, cebolla y cilantro. Acompañada con abundante caldo.",
      "en":"Made for dipping. Beef birria, frijoles hermanos, chipotle mayo, guacamole, onion and coriander. Served with plenty of broth."},
     {"n":"Burro de Birria","p":"8.95",
      "es":"¡El burrito más esperado! Jugosa birria de res, frijoles hermanos, aguacate, cebolla morada, mayo chipotle y tortilla crocante. Servido con nuestra espectacular salsa verde y caldo de birria para chuponear.",
      "en":"The most anticipated burrito. Juicy beef birria, frijoles hermanos, avocado, red onion, chipotle mayo and crispy tortilla. Served with our spectacular salsa verde and birria broth for dipping."}]},

   {"photo": "burros", "cap_es": "Burros y Burro Emperador", "cap_en": "Burros and Burro Emperador", "items": [
     {"n":"Burros","p":"7.50",
      "es":"¡Hechos con estilo y logrados con pasión! Rellenos de: arroz rojo, frijoles, aguacate, cebolla chipotle, mezcla de quesos, salsa de la casa y tu carne favorita.",
      "en":"Made with style and achieved with passion. Filled with red rice, beans, avocado, chipotle onion, our cheese blend, house sauce and your favourite meat.",
      "hint_es":"Agrega costra de queso por $1.00","hint_en":"Add a cheese crust for $1.00"},
     {"n":"Burro Emperador","p":"8.95",
      "es":"¡El Emperador! Camarones dorados, carne asada, salteado de cebolla, aguacate, frijoles hermanos, arroz rojo, tortilla crocante, cilantro, mayo chipotle y salsa de la casa. Todo cubierto con una costra de tres quesos.",
      "en":"The Emperor. Golden shrimp, grilled steak, sauteed onion, avocado, frijoles hermanos, red rice, crispy tortilla, coriander, chipotle mayo and house sauce, all covered in a three-cheese crust."}]},

   {"photo": "burro-mixto", "cap_es": "Burro Mixto", "cap_en": "Burro Mixto", "items": [
     {"n":"Burro Mixto","p":"8.95",
      "es":"¡Asada, pastor, chicharrón, jalada y carnitas! Relleno de guacamole, frijoles hermanos, cebolla chipotle, tortilla crocante, cilantro y costra de quesos. ¡Un poco de todo Tacos Hermanos!",
      "en":"Asada, pastor, chicharrón, jalada and carnitas. Filled with guacamole, frijoles hermanos, chipotle onion, crispy tortilla, coriander and a cheese crust. A little bit of all of Tacos Hermanos."}]},

   {"photo": "torta-derretida", "cap_es": "Torta Derretida", "cap_en": "Torta Derretida", "items": [
     {"n":"Torta Derretida","p":"8.95",
      "es":"¡Tenemos las tortas! Pan artesanal, frijoles hermanos, mayo chipotle, aguacate, cebolla, cilantro, cebolla dulce, costra de quesos y la carne de tu elección.",
      "en":"We have the tortas. Artisan bread, frijoles hermanos, chipotle mayo, avocado, onion, coriander, sweet onion, a cheese crust and the meat of your choice.",
      "hint_es":"Elige tu carne favorita.","hint_en":"Choose your favourite meat."}]},

   {"photo": "gringas-y-el-machete", "cap_es": "Gringas y El Machete", "cap_en": "Gringas and El Machete", "items": [
     {"n":"Gringas","p":"7.50",
      "es":"¡Clásicas pero sabrosas! Costra de tres quesos, frijoles hermanos, aguacate y la carne de tu elección.",
      "en":"Classic but delicious. A three-cheese crust, frijoles hermanos, avocado and the meat of your choice."},
     {"n":"El Machete","p":"9.95",
      "es":"¡Asada, pastor, chicharrón, jalada y carnitas! Todo en una quesadilla gigante con aguacate, salsa verde especial, cebolla asada y cilantro. Acompañado de crema jalapeña.",
      "en":"Asada, pastor, chicharrón, jalada and carnitas, all inside a giant quesadilla with avocado, special salsa verde, grilled onion and coriander. Served with jalapeño cream."}]},
  ]},

 {
  "id": "bowls",
  "es": "Bowls y sombreritos", "en": "Bowls and sombreritos",
  "note_es": "", "note_en": "",
  "blocks": [
   {"photo": "bowl-hermano", "cap_es": "Bowl Hermano", "cap_en": "Bowl Hermano", "items": [
     {"n":"Bowl Hermano","p":"9.95",
      "es":"¡El más esperado! Arroz cilantro - limón, maíz dulce, frijoles, pico de gallo, aguacate, queso rallado, tortilla crocante y cilantro. Servida con nuestra espectacular salsa verde.",
      "en":"The most anticipated of all. Coriander and lime rice, sweet corn, beans, pico de gallo, avocado, grated cheese, crispy tortilla and coriander. Served with our spectacular salsa verde.",
      "hint_es":"Asada · Pollo Chipotle","hint_en":"Asada · Pollo Chipotle"}]},

   {"photo": "sombreritos", "cap_es": "Sombreritos, escoge 2 de 3", "cap_en": "Sombreritos, choose two of three", "items": [
     {"n":"Sombreritos","p":"7.95",
      "es":"¡Crocantes, gratinados y espectaculares! Escoge 2 de 3.",
      "en":"Crispy, gratinated and spectacular. Choose two out of three."},
     {"n":"Camarón","p":"",
      "es":"Base de harina crocante, quesos gratinados, aguacate, salteado especial y camarones al ajillo con mayo chipotle.",
      "en":"Crispy flour base, gratinated cheeses, avocado, special saute and garlic shrimp with chipotle mayo."},
     {"n":"Pastor","p":"",
      "es":"Base de harina crocante, pastor, quesos gratinados, piña asada, frijoles hermanos, salsa de trompo y jardín de cilantro.",
      "en":"Crispy flour base, pastor, gratinated cheeses, grilled pineapple, frijoles hermanos, trompo sauce and a garden of coriander."},
     {"n":"Pollo Chipotle","p":"",
      "es":"Base de harina crocante, pollo chipotle, esquite, quesos gratinados, frijoles hermanos, aguacate, salsa chipotle y queso rallado.",
      "en":"Crispy flour base, chipotle chicken, esquite, gratinated cheeses, frijoles hermanos, avocado, chipotle sauce and grated cheese."}]},
  ]},

 {
  "id": "postres",
  "es": "Postres", "en": "Desserts",
  "note_es": "", "note_en": "",
  "blocks": [
   {"photo": "postres", "cap_es": "Brownie, Flan de Cajeta y Arroz con Leche",
    "cap_en": "Brownie, Flan de Cajeta and Arroz con Leche", "items": [
     {"n":"Brownie","p":"4.65","es":"","en":""},
     {"n":"Flan de Cajeta","p":"4.65","es":"","en":""},
     {"n":"Arroz con Leche","p":"4.65","es":"¡Tal como suena!","en":"Exactly as it sounds."}]},
  ]},
]

# --- drinks on the main menu ---------------------------------------------
MARGARITAS = [("Tradicional","Tradicional","5.50"),("Maracuyá","Maracuyá","5.50"),("Fresa","Fresa","5.50")]
FROZENS = [("Arrayanada","Arrayanada","3.50"),("Mango Sazón","Mango Sazón","3.50"),
           ("Carretón","Carretón","3.50"),("Chocobanano","Chocobanano","3.50"),("Maracuyá","Maracuyá","3.50")]
CERVEZAS = [("Pilsener","Pilsener","2.45"),("Golden","Golden","2.45"),("Suprema","Suprema","3.25"),
            ("Corona","Corona","3.25"),("Michelob Ultra","Michelob Ultra","3.25"),
            ("Stella Artois","Stella Artois","3.25"),("Modelo","Modelo","3.25"),
            ("Regia Chola","Regia Chola","4.50"),("Mix de michelada","Michelada mix","1.00"),
            ("Mix de tamarindo","Tamarind mix","1.50")]
BEBIDAS_MAIN = [
 ("Limonada natural","Fresh lemonade","2.25"),("Limonada con soda","Lemonade with soda","2.50"),
 ("Limonada piña hierba buena","Pineapple and mint lemonade","2.95"),
 ("Limonada cilantro","Coriander lemonade","2.95"),("Limonada de fresa","Strawberry lemonade","2.95"),
 ("Naranjada natural","Fresh orangeade","2.25"),("Naranjada con soda","Orangeade with soda","2.50"),
 ("Cimarrona","Cimarrona","2.75"),("Té helado","Iced tea","2.95"),
 ("Horchata de maní","Peanut horchata","2.95"),("Horchata de morro","Morro horchata","2.95"),
 ("Jugo de tomate preparado","Prepared tomato juice","2.95"),("Café","Coffee","1.95"),
 ("Agua mineral","Sparkling water","1.95"),("Botella de agua","Bottled water","1.95"),
 ("Gaseosa","Soft drink","1.95")]

# photos that belong to the drinks sections
FOTO_MARGARITAS = "margaritas"
FOTO_FROZENS = "frozens"
FOTO_LIFESTYLE = "coca-cola-hermanos"

# =========================================================================
# DESAYUNOS  (breakfast menu, July 2026). Every dish has its own photograph.
# =========================================================================
DESAYUNOS_INCLUYE_ES = "Todos nuestros desayunos incluyen café con refill, un pan artesanal y salsa roja tatemada o salsa verde."
DESAYUNOS_INCLUYE_EN = "Every breakfast includes coffee with free refills, an artisan bread roll, and either roasted red salsa or salsa verde."

DESAYUNOS_BLOQUES = [
 {"photo":"desayuno-super-tipico-hermano","cap_es":"Súper Típico Hermano","cap_en":"Súper Típico Hermano","items":[
   {"n":"Súper Típico Hermano","p":"7.95",
    "es":"¡La mejor forma de comenzar la mañana! Huevos al gusto, chorizo hecho en casa, aguacate, plátano frito, frijoles hermanos, queso y crema.",
    "en":"The best way to start the morning. Eggs your way, house-made chorizo, avocado, fried plantain, frijoles hermanos, cheese and cream."}]},
 {"photo":"desayuno-los-dorados","cap_es":"Los Dorados","cap_en":"Los Dorados","items":[
   {"n":"Los Dorados","p":"6.95",
    "es":"¡Crocantes, dorados y llenos de sabor! Huevos al gusto, frijoles hermanos, aguacate y nuestros Tacos Dorados rellenos de pollo y papa, bañados con Espectacular Salsa Verde.",
    "en":"Crispy, golden and full of flavour. Eggs your way, frijoles hermanos, avocado and our Tacos Dorados filled with chicken and potato, bathed in our Espectacular Salsa Verde."}]},
 {"photo":"desayuno-huevos-rotos","cap_es":"Huevos Rotos","cap_en":"Huevos Rotos","items":[
   {"n":"Huevos Rotos","p":"7.95",
    "es":"Cazuela de papas fritas crocantes, huevos estrellados, chorizo hecho en casa, cilantro y nuestra salsa especial.",
    "en":"A skillet of crispy fried potatoes, sunny-side-up eggs, house-made chorizo, coriander and our special sauce."}]},
 {"photo":"desayuno-los-enchorizados","cap_es":"Los Enchorizados","cap_en":"Los Enchorizados","items":[
   {"n":"Los Enchorizados","p":"7.45",
    "es":"¡Simplemente espectaculares! Huevos estrellados montados en tortillas crocantes, frijoles hermanos, chorizo hecho en casa y Espectacular Salsa Verde. Servidos con aguacate, plátano y queso.",
    "en":"Simply spectacular. Sunny-side-up eggs on crispy tortillas, frijoles hermanos, house-made chorizo and Espectacular Salsa Verde. Served with avocado, plantain and cheese."}]},
 {"photo":"desayuno-tostada-de-aguacate","cap_es":"Tostada de Aguacate","cap_en":"Tostada de Aguacate","items":[
   {"n":"Tostada de Aguacate","p":"7.95",
    "es":"Tostada de masa madre, guacamole fresco, champiñones salteados y huevos revueltos. Todo coronado con espinaca fresca. Acompañada de frijoles hermanos y queso.",
    "en":"Sourdough toast, fresh guacamole, sauteed mushrooms and scrambled eggs, crowned with fresh spinach. Served with frijoles hermanos and cheese.",
    "hint_es":"Podés pedirla con claras de huevos.","hint_en":"You can order it with egg whites."}]},
 {"photo":"desayuno-burro-asado","cap_es":"Burro Asado","cap_en":"Burro Asado","items":[
   {"n":"Burro Asado","p":"9.95",
    "es":"¡Poderoso e inolvidable! Nuestro burro relleno de asada, costra de quesos, frijoles hermanos y cebolla chipotle. Dos huevos estrellados montados con Espectacular Salsa Verde. Acompañado con plátanos fritos y aguacate.",
    "en":"Powerful and unforgettable. Our burrito filled with grilled steak, a cheese crust, frijoles hermanos and chipotle onion. Two sunny-side-up eggs on top with Espectacular Salsa Verde. Served with fried plantain and avocado."}]},
 {"photo":"desayuno-omelette-asado","cap_es":"Omelette Asado","cap_en":"Omelette Asado","items":[
   {"n":"Omelette Asado","p":"8.95",
    "es":"¡Como debe ser! Nuestro omelette en su punto, con carne asada y queso gratinado. Acompañado de frijoles hermanos y aguacate fresco.",
    "en":"Exactly as it should be. Our omelette cooked just right, with grilled steak and gratinated cheese. Served with frijoles hermanos and fresh avocado."}]},
 {"photo":"desayuno-tostadas-a-la-francesa","cap_es":"Tostadas a la Francesa","cap_en":"Tostadas a la Francesa","items":[
   {"n":"Tostadas a la Francesa","p":"7.95",
    "es":"Inspiradas en el sabor de nuestro Arroz con Leche. Doradas y suaves tostadas a la francesa con fresas, arándanos, crocante de galleta y nuestra salsa de leche.",
    "en":"Inspired by the flavour of our Arroz con Leche. Golden, soft French toast with strawberries, blueberries, cookie crumble and our milk sauce."}]},
]

DESAYUNO_BEBIDAS_BLOQUES = [
 {"photo":"desayuno-batido-de-cafe-y-cebada","cap_es":"Batido de Café y Cebada de Fresa",
  "cap_en":"Batido de Café and Cebada de Fresa","drinks":[
   ("Batido de Café","Coffee Shake","3.50"),("Cebada de Fresa","Strawberry Cebada","2.95")]},
 {"photo":"desayuno-cremosos","cap_es":"Los cremosos","cap_en":"The cremosos","drinks":[
   ("Cremoso de Banano","Banana Cremoso","3.50"),("Cremoso de Chocolate","Chocolate Cremoso","3.50"),
   ("Cremoso de Maní","Peanut Cremoso","3.50")]},
]

DESAYUNO_BEBIDAS = [("Café americano con refill","American coffee with refills","1.95"),
  ("Jugo de naranja","Orange juice","2.50"),("Jugo de naranja con piña","Orange and pineapple juice","2.50"),
  ("Horchata de maní","Peanut horchata","2.95"),("Horchata de morro","Morro horchata","2.95"),
  ("Gaseosa","Soft drink","1.95"),("Botella de agua","Bottled water","1.95")]

# kept so the JSON-LD Menu node and llms-full.txt can iterate a flat dish list
DESAYUNOS = [i for b in DESAYUNOS_BLOQUES for i in b["items"]]
DESAYUNO_ESPECIALES = [d for b in DESAYUNO_BEBIDAS_BLOQUES for d in b["drinks"]]
