from my_time_date.current_time import calculate_current_time

def test_it_should_return_the_current_time():
    current_time = calculate_current_time()
    assert "2020.04.23 16:00:00" == current_time

def test_it_should_return_moon_phase():


