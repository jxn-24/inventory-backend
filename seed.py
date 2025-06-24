from app import create_app
from app.models import db, Category, Inventory

def seed_database():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create categories
        electronics = Category(name="Electronics")
        furniture = Category(name="Furniture")
        db.session.add_all([electronics, furniture])
        db.session.commit()  # Commit categories first to get their IDs

        # Create inventory items with all 16 products
        inventory_items = [
            Inventory(
                name="Laptop",
                category=electronics,  # Pass the category object, not string
                quantity=5,
                price=58000,
                image="https://m.media-amazon.com/images/I/71kBeFDgCkL._AC_SL1500_.jpg"
            ),
            Inventory(
                name="Chair",
                category=furniture,  # Pass the category object
                quantity=10,
                price=75050,
                image="https://cdn11.bigcommerce.com/s-9nl27vlw/images/stencil/532x532/products/7338/16667/PXL_20250123_121512348.PORTRAIT__89721.1737709019.jpg?c=2"
            ),
            Inventory(
                name="Charger",
                category=electronics,
                quantity=20,
                price=1500,
                image="https://hotpoint.co.ke/media/cache/6e/b9/6eb9197bfae67dc9f4aeab1afcbb650d.webp"
            ),
            Inventory(
                name="Desk",
                category=furniture,
                quantity=7,
                price=30800,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJa5GDLH6MT5UEfFzdExIh_ziJ3wCnbMg7RhCsnrwqJFZ-bSBytFViHUjFrsHeI4p1ki0&usqp=CAU"
            ),
            Inventory(
                name="Headphones",
                category=electronics,
                quantity=12,
                price=35000,
                image="https://techbramtechnologies.co.ke/wp-content/uploads/2016/03/Gaming-headphones.jpg"
            ),
            Inventory(
                name="Monitor",
                category=electronics,
                quantity=8,
                price=108000,
                image="https://electronicwhiteboardswarehouse.com/cdn/shop/files/download_0ff07200-461d-4089-a749-b43a91c639a1_1024x.jpg?v=1696165971"
            ),
            Inventory(
                name="Keyboard",
                category=electronics,
                quantity=15,
                price=4500,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQ_Lh6UEIII0PjjmVzMMMDtPnrp_peP9deiYIyrNmuY78_ioLcwkquiwMEYOlXy9Ex8nA&usqp=CAU"
            ),
            Inventory(
                name="Mouse",
                category=electronics,
                quantity=25,
                price=2000,
                image="https://m.media-amazon.com/images/I/61Mk3YqYHpL._AC_SL1500_.jpg"
            ),
            Inventory(
                name="Office Table",
                category=furniture,
                quantity=4,
                price=31000,
                image="https://i0.wp.com/myoffice.co.ke/wp-content/uploads/2024/12/r9kfok6c.png?fit=1200%2C1200&ssl=1"
            ),
            Inventory(
                name="Gaming Chair",
                category=furniture,
                quantity=2,
                price=48000,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTddIMbLZQQnUlsQkTqrMF0BNJxHaUklVAdl8WwAHJhj7dC0ZNkk0DmQIF2KP-BIWZ3CYE&usqp=CAU"
            ),
            Inventory(
                name="Smartphone",
                category=electronics,
                quantity=10,
                price=128000,
                image="https://res.cloudinary.com/jerrick/image/upload/d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,q_auto,w_1024/66f307779c1020001d4ed3b8.jpg"
            ),
            Inventory(
                name="Printer",
                category=electronics,
                quantity=3,
                price=12650,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyE5GjkOIROLmovVOs3J1X8gZ4sHcTCLY3UhwLVacdgRPIvmZBYh7t8zN3ETS_Tcpi_OA&usqp=CAU"
            ),
            Inventory(
                name="Tablet",
                category=electronics,
                quantity=6,
                price=45000,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1r7v2xX3g5qk4j8m1JcYbZz4G5l0a2nqKXw&usqp=CAU"
            ),
            Inventory(
                name="External Hard Drive",
                category=electronics,
                quantity=18,
                price=1500,
                image="https://arcticcomputershop.com/wp-content/uploads/2022/07/4.jpg"
            ),
            Inventory(
                name="Couch",
                category=furniture,
                quantity=2,
                price=73000,
                image="https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1678558293-98a1e29126ae46ae5eeab549cd9f913a.jpg?crop=1xw:1.00xh;center,top&resize=980:*"
            ),
            Inventory(
                name="Sofa",
                category=furniture,
                quantity=3,
                price=120000,
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1r7v2xX3g5qk4j8m1JcYbZz4G5l0a2nqKXw&usqp=CAU"
            )
        ]
        
        db.session.add_all(inventory_items)
        db.session.commit()
        print("Successfully seeded all 16 inventory items!")

if __name__ == '__main__':
    seed_database()