# @app.route("/random")
# def get_random_cafe():
#     cafes = db.session.query(Cafe).all()
#     random_cafe = random.choice(cafes)
#     return jsonify(cafe={
#         "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "location": random_cafe.location,
#         "seats": random_cafe.seats,
#         "has_toilet": random_cafe.has_toilet,
#         "has_wifi": random_cafe.has_wifi,
#         "has_sockets": random_cafe.has_sockets,
#         "can_take_calls": random_cafe.can_take_calls,
#         "coffee_price": random_cafe.coffee_price,
#     })
## RANDOM

# @app.route("/random")
# def get_random_cafe():
#     cafes = db.session.query(Cafe).all()
#     random_cafe = random.choice(cafes)
#     return jsonify(cafe={
#         # Omit the id from the response
#         # "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "location": random_cafe.location,
#
#         # Put some properties in a sub-category
#         "amenities": {
#             "seats": random_cafe.seats,
#             "has_toilet": random_cafe.has_toilet,
#             "has_wifi": random_cafe.has_wifi,
#             "has_sockets": random_cafe.has_sockets,
#             "can_take_calls": random_cafe.can_take_calls,
#             "coffee_price": random_cafe.coffee_price,
#         }
#     })

## USING DICTIONARY

# class Cafe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), unique=True, nullable=False)
#     map_url = db.Column(db.String(500), nullable=False)
#     img_url = db.Column(db.String(500), nullable=False)
#     location = db.Column(db.String(250), nullable=False)
#     seats = db.Column(db.String(250), nullable=False)
#     has_toilet = db.Column(db.Boolean, nullable=False)
#     has_wifi = db.Column(db.Boolean, nullable=False)
#     has_sockets = db.Column(db.Boolean, nullable=False)
#     can_take_calls = db.Column(db.Boolean, nullable=False)
#     coffee_price = db.Column(db.String(250), nullable=True)
#
#     def to_dict(self):
#         # Method 1.
#         dictionary = {}
#         # Loop through each column in the data record
#         for column in self.__table__.columns:
#             # Create a new dictionary entry;
#             # where the key is the name of the column
#             # and the value is the value of the column
#             dictionary[column.name] = getattr(self, column.name)
#         return dictionary
#
#         # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
#         return {column.name: getattr(self, column.name) for column in self.__table__.columns}
#
#
# @app.route("/random")
# def get_random_cafe():
#     cafes = db.session.query(Cafe).all()
#     random_cafe = random.choice(cafes)
#     # Simply convert the random_cafe data record to a dictionary of key-value pairs.
#     return jsonify(cafe=random_cafe.to_dict())


# @app.route("/all")
# def get_all_cafes():
#     cafes = db.session.query(Cafe).all()
#     all_cafes = []
#     for cafe in cafes:
#         all_cafes.append({
#                 "id": cafe.id,
#                 "name": cafe.name,
#                 "map_url": cafe.map_url,
#                 "img_url": cafe.img_url,
#                 "location": cafe.location,
#                 "seats": cafe.seats,
#                 "has_toilet": cafe.has_toilet,
#                 "has_wifi": cafe.has_wifi,
#                 "has_sockets": cafe.has_sockets,
#                 "can_take_calls": cafe.can_take_calls,
#                 "coffee_price": cafe.coffee_price
#         })
#     return jsonify(cafe=all_cafes)