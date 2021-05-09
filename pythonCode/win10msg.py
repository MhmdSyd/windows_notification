from win10toast import ToastNotifier

title = "from my python application 😎 hahaha 👌 💪"
msg = str(input("Enter your massage: ").strip())
toaster = ToastNotifier()
toaster.show_toast(title, msg, icon_path=None, duration=10, threaded=True)
