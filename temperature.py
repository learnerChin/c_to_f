ask = input("請問要轉華氏或攝氏溫度?\n")
if ask == "華氏":
	c = float(input("請輸入攝氏溫度\n"))
	f = c * 9 / 5 + 32
	print(f"華氏溫度為{f}")
elif ask == "攝氏":
	f = float(input("請輸入華氏溫度\n"))
	c = 5 / 9 * f - 32
	print(f"攝氏溫度為{c}")