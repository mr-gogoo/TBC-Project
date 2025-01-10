from ext import app, db
from models import Product, User, Item, Pro

users = [{"username": "მარიამი",
          "password": "12345678",
          "role": "Admin"}]

products = [{
    "text": "1 საათი - 80 ლარი",
    "img": "https://cdn.swoop.ge/ImagesStorage/f629cb12-08e1-465e-ab62-c65fa6c0526b.png",
    "name": "ანიმატორი ნინი"},

    {"text": "1 საათი 30 წუთი - 100 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/f79bfa28-31f6-4ed8-ada6-5410f1713a0e.png",
     "name": "ანიმატორი ჯეკო"},
    {
        "text": "1 საათი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/585653fe-4ed1-4e52-b48f-2911e60ee6eb.png",
        "name": "ანიმატორი თაზო"},
    {
        "text": "1 საათი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/fabad37c-b522-4465-88a0-590a748717a3.jpg",
        "name": "ანიმატორი ქეთა"},

    {"text": "40 წუთი - 60 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/99770d8d-6492-4518-a46f-7175e5bc22c6.jpg",
     "name": "ანიმატორი პიტი"},
    {
        "text": "1 საათი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/3add022e-2864-49b3-b07f-3b8bc8e26be9.png",
        "name": "ანიმატორი ნიკა"},
    {
        "text": "1 საათი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/663a4bb2-3a41-4663-9426-dfb0af4100d5.png",
        "name": "ანიმატორი გია"},
    {
        "text": "1 საათი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/7d4fc0d9-e125-4071-94fd-32e6b9ab022b.png",
        "name": "ანიმატორი ანა"}
]
items = [{
    "text": "30 წუთი - 40 ლარი",
    "img": "https://cdn.swoop.ge/ImagesStorage/6e5501c7-df8d-4202-b873-240b19e7b4da.jpg",
    "name": "ლოლი გამოძახებით"},
     {
        "text": "30 წუთი - 40 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/0c7463df-374e-4ba9-b1fa-85378c8f68c4.jpg",
     "name": "მინიონი გამოძახებით"},
    {
        "text": "30 წუთი - 40 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/13a39217-f810-409a-97db-01c94270baf5.jpg",
        "name": "ვენსდეი გამოძახებით"},
    {
        "text": "30 წუთი - 40 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/7e927d93-3794-4676-b80b-ec8d8dd8b32f.jpg",
        "name": "ბარბი გამოძახებით"},

    {"text": "30 წუთი - 40 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/d23f4f69-b031-439f-82fd-e65415e6622c.png",
     "name": "ფიფქია გამოძახებით"},
    {
        "text": "45 წუთი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/af1d97bb-a28d-4d69-94f8-c9a5ca2e954c.png",
        "name": "ელზა და ანნა გამოძახებით"},
    {
        "text": "45 წუთი - 80 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/fe311e79-46f4-43f4-9c73-d58c3d048a00.png",
        "name": "რაპუნცელი და ბელი გამოძახებით"},
    {
        "text": "30 წუთი - 40 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/bc3eb78f-90f7-4090-aa69-4f4577d4fa19.png",
        "name": "ბეტმენი გამოძახებით"}

]

pros = [{
    "text": "2 საათი - 250 ლარი",
    "img": "https://cdn.swoop.ge/ImagesStorage/34b444dd-a14e-4e65-aded-94ddee82d03b.png",
    "name": "პროგრამა (ჯამბაზი, ელზა, ანნა)"},
     {
        "text": "1 საათი - 100 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/6ecc29b3-e174-4e09-87a0-4690bed109b6.jpg",
     "name": "პროგრამა (მინი, ლოლი"},
    {
        "text": "1 საათი 30 წუთი - 450 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/252ff26f-1406-469a-b361-df5db4d47f46.jpg",
        "name": "პროგრამა (ტროლი, კუნინძა, გოჭი პეპა, სტიჩი, დათუნია"},
    {
        "text": "1 საათი - 100 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/b501debc-469f-483a-b789-f31da43193c5.jpg",
        "name": "პროგრამა (ნარუტო, სონიკი)"},

    {"text": "1 საათი 30 წუთი - 200 ლარი",
     "img": "https://cdn.swoop.ge/ImagesStorage/4e413e9e-863a-432e-8b73-653fd914054e.jpg",
     "name": "პროგრამა (პეპა გოჭი, ჰელოუ კიტი, მინიონი)"},
    {
        "text": "1 საათი - 100 ლარი",
        "img": "https://cdn.swoop.ge/ImagesStorage/1815d43f-d078-4912-be7a-bd51c9bcada3.jpg",
        "name": "პროგრამა (მიკი მაუსი, მინი მაუსი)"}
]

with app.app_context():

    db.drop_all()
    db.create_all()

    for product in products:
        new_product = Product(name=product["name"], text=product["text"], img=product["img"])
        db.session.add(new_product)
    db.session.commit()

    for user in users:
        new_user = User(username=user["username"], password=user["password"], role=user["role"])
        db.session.add(new_user)
    db.session.commit()

    for item in items:
        new_item = Item(text=item["text"], img=item["img"], name=item["name"])
        db.session.add(new_item)
    db.session.commit()

    for pro in pros:
        new_pro = Pro(text=pro["text"], img=pro["img"], name=pro["name"])
        db.session.add(new_pro)
    db.session.commit()


