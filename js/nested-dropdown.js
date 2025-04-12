// JavaScript برای کنترل منوی کشویی سطح دوم

document.addEventListener('DOMContentLoaded', function() {
  // انتخاب همه آیتم‌های منو
  const menuItems = document.querySelectorAll('.menu-list-item');
  const subDropdownParents = document.querySelectorAll('.menu-list-item-dropdown li.group');
  
  // بستن همه منوهای کشویی سطح دوم با کلیک روی سایر گزینه‌ها
  document.addEventListener('click', function(e) {
    // اگر کلیک روی آیتم منوی کشویی سطح دوم نبود، همه منوهای کشویی سطح دوم را ببند
    if (!e.target.closest('.group')) {
      document.querySelectorAll('.sub-dropdown').forEach(dropdown => {
        dropdown.classList.remove('block');
        dropdown.classList.add('hidden');
      });
    }
  });
  
  // نمایش منوی کشویی سطح دوم با کلیک
  subDropdownParents.forEach(item => {
    const link = item.querySelector('a');
    const subDropdown = item.querySelector('.sub-dropdown');
    
    if (link && subDropdown) {
      link.addEventListener('click', function(e) {
        e.preventDefault(); // جلوگیری از هدایت به صفحه دیگر
        
        // بستن همه منوهای کشویی سطح دوم
        document.querySelectorAll('.sub-dropdown').forEach(dropdown => {
          if (dropdown !== subDropdown) {
            dropdown.classList.remove('block');
            dropdown.classList.add('hidden');
          }
        });
        
        // تغییر وضعیت نمایش منوی کشویی سطح دوم
        if (subDropdown.classList.contains('hidden')) {
          subDropdown.classList.remove('hidden');
          subDropdown.classList.add('block');
        } else {
          subDropdown.classList.remove('block');
          subDropdown.classList.add('hidden');
        }
        
        // هل دادن گزینه‌های پایین در حالت موبایل
        if (window.innerWidth <= 768) {
          const nextItems = [];
          let nextItem = item.parentElement.nextElementSibling;
          
          while (nextItem) {
            nextItems.push(nextItem);
            nextItem = nextItem.nextElementSibling;
          }
          
          if (subDropdown.classList.contains('block')) {
            nextItems.forEach(item => {
              item.style.marginTop = subDropdown.offsetHeight + 'px';
              item.style.transition = 'margin-top 0.3s ease';
            });
          } else {
            nextItems.forEach(item => {
              item.style.marginTop = '0';
            });
          }
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
