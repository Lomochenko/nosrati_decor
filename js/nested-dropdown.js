// JavaScript برای کنترل منوی کشویی سطح دوم

document.addEventListener('DOMContentLoaded', function() {
  // انتخاب همه آیتم‌های منو
  const menuItems = document.querySelectorAll('.menu-list-item');
  const subDropdownParents = document.querySelectorAll('.menu-list-item-dropdown li.group');

  // متغیر برای نگهداری منوی کشویی سطح دوم فعلی
  let currentOpenDropdown = null;

  // بستن همه منوهای کشویی سطح دوم با کلیک روی سایر گزینه‌ها
  document.addEventListener('click', function(e) {
    // اگر کلیک روی آیتم منوی کشویی سطح دوم نبود، همه منوهای کشویی سطح دوم را ببند
    if (!e.target.closest('.group')) {
      closeAllDropdowns();
    }
  });

  // تابع برای بستن همه منوهای کشویی سطح دوم
  function closeAllDropdowns() {
    document.querySelectorAll('.sub-dropdown').forEach(dropdown => {
      dropdown.classList.remove('block');
      dropdown.classList.add('hidden');
    });

    // ریست کردن استایل‌های margin-top برای آیتم‌های بعدی
    if (window.innerWidth <= 768) {
      document.querySelectorAll('.menu-list-item-dropdown li').forEach(item => {
        item.style.marginTop = '0';
      });
    }

    // ریست کردن منوی کشویی سطح دوم فعلی
    currentOpenDropdown = null;
  }

  // نمایش منوی کشویی سطح دوم با کلیک
  subDropdownParents.forEach(item => {
    const link = item.querySelector('a');
    const subDropdown = item.querySelector('.sub-dropdown');

    if (link && subDropdown) {
      // حذف عملکرد hover برای نمایش منوی کشویی سطح دوم
      item.addEventListener('mouseenter', function(e) {
        e.preventDefault();
        // هیچ کاری انجام نده - hover غیرفعال شده است
      });

      // اضافه کردن عملکرد کلیک برای نمایش منوی کشویی سطح دوم
      link.addEventListener('click', function(e) {
        e.preventDefault(); // جلوگیری از هدایت به صفحه دیگر
        e.stopPropagation(); // جلوگیری از انتشار رویداد به عناصر والد

        // اگر روی همان منوی کشویی سطح دوم کلیک شده که قبلاً باز بوده، آن را ببند
        if (currentOpenDropdown === subDropdown && subDropdown.classList.contains('block')) {
          subDropdown.classList.remove('block');
          subDropdown.classList.add('hidden');
          currentOpenDropdown = null;

          // ریست کردن استایل‌های margin-top برای آیتم‌های بعدی در حالت موبایل
          if (window.innerWidth <= 768) {
            const nextItems = [];
            let nextItem = item.parentElement.nextElementSibling;

            while (nextItem) {
              nextItems.push(nextItem);
              nextItem = nextItem.nextElementSibling;
            }

            nextItems.forEach(item => {
              item.style.marginTop = '0';
            });
          }

          return;
        }

        // بستن منوی کشویی سطح دوم قبلی
        closeAllDropdowns();

        // باز کردن منوی کشویی سطح دوم جدید
        subDropdown.classList.remove('hidden');
        subDropdown.classList.add('block');
        currentOpenDropdown = subDropdown;

        // هل دادن گزینه‌های پایین در حالت موبایل
        if (window.innerWidth <= 768) {
          const nextItems = [];
          let nextItem = item.parentElement.nextElementSibling;

          while (nextItem) {
            nextItems.push(nextItem);
            nextItem = nextItem.nextElementSibling;
          }

          nextItems.forEach(item => {
            item.style.marginTop = subDropdown.offsetHeight + 'px';
            item.style.transition = 'margin-top 0.3s ease';
          });
        }
      });
    }
  });

  // تنظیم مجدد استایل‌ها در هنگام تغییر اندازه صفحه
  window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
      document.querySelectorAll('.menu-list-item-dropdown li').forEach(item => {
        item.style.marginTop = '0';
      });
    }
  });
});
