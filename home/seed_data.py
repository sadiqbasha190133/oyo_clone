from accounts.models import Hotel, HotelVendor, Ameneties
from accounts.templates.utils.sendEmail import generate_slug

from faker import Faker
import random

fake = Faker()

def generate_fake_hotel(total_hotels = 100):
    hotels = []
    for _ in range(total_hotels):
        hotel_name = fake.company() + " Hotel"
        hotel_description = fake.text(max_nb_chars=200)
        hotel_price = round(random.uniform(1000, 5000), 2)  # e.g. ₹1000–₹5000
        hotel_offer_price = round(hotel_price * random.uniform(0.6, 0.9), 2)  # 10–40% off
        hotel_location = fake.address().replace("\n", ", ")
        amenity_ids = random.sample(range(8, 14), random.randint(4, 6))

        hotel_vendor = HotelVendor.objects.get(id = 16)
        hotel_obj = Hotel.objects.create(
            hotel_name = hotel_name,
            hotel_description = hotel_description,
            hotel_slug = generate_slug(hotel_name),
            hotel_owner = hotel_vendor,
            hotel_price = hotel_price,
            hotel_offer_price = hotel_offer_price,
            hotel_location = hotel_location,
        )

        for id in amenity_ids:
            amenity = Ameneties.objects.get(id = id)
            hotel_obj.ameneties.add(amenity)
            hotel_obj.save()

        hotels.append(hotel_obj)
    Hotel.objects.bulk_create(hotels)


    







# def bulkDB(num_records = 10000):
#     start_time = time.time()
#     students_list = []
#     for record in range(num_records):
#         college = College.objects.all().order_by('?')[0]
#         department = Department.objects.all().order_by('?')[0]
#         skills = Skills.objects.all().order_by('?')[0:random.randint(1, 3)]

#         name = fake.name()
#         age = random.randint(18, 34)
#         gender = random.choice(['Male', 'Female'])
#         phone_number = random.randint(1000000000, 9999999999)
#         student_bio = fake.sentence()
#         email = fake.email()
#         date_of_birth = fake.date_of_birth(minimum_age=age-18, maximum_age=age-18)
#         percentage = round(random.uniform(70.0, 100.0), 2)


#         student = Student(
#             name=name,
#             age=age,
#             gender=gender,
#             phone_number=phone_number,
#             bio=student_bio,
#             email=email,
#             percentage = percentage,
#             DOB=date_of_birth,
#             college_name=college,
#             department_name=department
#         )

#         students_list.append(student)
#     Student.objects.bulk_create(students_list)

#         # student.skills.set(skills)
#     print(f"Time taken to bulk the database: {time.time() - start_time} seconds")
