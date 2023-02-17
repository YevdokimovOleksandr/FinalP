import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_name():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user [0][0] == 'Maydan Nezalezhnosti 1'
    assert user [0][1] == 'Kyiv'
    assert user [0][2] == '3127'
    assert user [0][3] == 'Ukraine'


@pytest.mark.database
def test_update_qnt():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)
        
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_insert_product():
    db = Database()
    db.insert_product(4, 'gum', 'cheryy', 18)
    water_qnt = db.select_product_qnt_by_id(4)
        
    assert water_qnt[0][0] == 18


@pytest.mark.database
def test_delete_product():
    db = Database()
    db.insert_product(99, 'ghfjg', 'dfuue', 42)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

   
@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'