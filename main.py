import calculations as c


if __name__ == '__main__':

    circle_rs = [5, 4, 2]
    result = c.sum_circle_areas(circle_rs)
    print("="*80)
    print(f"Result is: {result}")
    print("="*80)
    assert result == 141.37