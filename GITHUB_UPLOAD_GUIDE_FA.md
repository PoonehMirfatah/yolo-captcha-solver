# راهنمای قرار دادن پروژه در GitHub

این فایل ZIP برای انتقال پروژه آماده شده است. برای اینکه فایل‌های کد، مدل، صفحه HTML و نتایج به‌صورت جداگانه در مخزن دیده شوند، **ZIP را اول Extract کنید**؛ فایل ZIP را به‌عنوان یک فایل واحد در مخزن آپلود نکنید.

## روش پیشنهادی: GitHub Desktop

1. فایل `YOLO_GitHub_Ready.zip` را Extract کنید.
2. در GitHub Desktop یک ریپوزیتوری محلی جدید با مسیر پوشه استخراج‌شده بسازید یا آن را به برنامه اضافه کنید.
3. فایل‌های تغییرکرده را بررسی و Commit کنید.
4. با `Publish repository` یا `Push origin` پروژه را به GitHub بفرستید.

## روش با Git (داخل پوشه استخراج‌شده)

```bash
git init
git add .
git commit -m "Add YOLO classification project"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

نشانی `USERNAME/REPO` را با آدرس واقعی مخزن خودتان عوض کنید. قبل از اجرا، مخزن خالی را در GitHub بسازید. اگر مخزن قبلاً فایل یا کامیت دارد، دستورهای ادغام ممکن است متفاوت باشند.

## نکات مهم

- فایل `models/best.pt` و همه کدهای اصلی بدون تغییر نگه داشته شده‌اند.
- تنها ویدئوی خروجی `resultVideo.mp4` از بسته اصلی جدا شده و در `YOLO_Demo_Video.zip` قابل دریافت است.
- `dataset/` و `dataset_9/` در فایل ارسالی اولیه وجود نداشتند؛ برای آموزش دوباره باید آن‌ها را از نسخه اصلی خود بازیابی کنید.
- فایل `chromedriver.exe` نیز در بسته اولیه وجود نداشت؛ اسکریپت Selenium به آن احتیاج دارد.
- آپلود یک فایل ZIP به گیت‌هاب، آن را خودکار Extract نمی‌کند.
