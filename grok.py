# d.py
import grokv8        # اسم ماژولی که فایل .so بهش مربوطه

# اگر ماژول تابعی به نام foo داشته باشه:
if hasattr(grokv8, "foo"):
    print("calling c.foo():", grokv8.foo())
else:
    # لیست اعضا رو چاپ کن تا ببینی چه چیزی صادر شده
    print("module members:", dir(grokv8))
