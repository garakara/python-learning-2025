def test(n):
    print(f"→{n}")
    if n > 2:
        return
    test(n + 1)
    print(f"←{n}")

test(0)