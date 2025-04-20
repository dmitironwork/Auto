import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Dmytro'


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Beznosov'



#  def test_change_name(user):
#     assert user.name == 'Dmytro'   
 
# def test_change_second_name(user):
#     assert user.second_name == 'Beznosov'
  

# def test_change_name():
#     user = User()
#     user.create()    

#     assert user.name == 'Dmytro'   
#     user.remove()    

# def test_change_second_name():
#     user = User()
#     user.create()

#     assert user.second_name == 'Beznosov'
#     user.remove    