from django import forms


class AdvertisingForm(forms.Form):
    Full_Name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "py-4 pl-5 bg-backgroundBody dark:bg-dark focus:outline-none focus:border-primary border dark:border-dark w-full text-colorText dark:text-backgroundBody/70 text-xl leading-[1.4] tracking-[0.4px] mt-3",
            "placeholder": "نام و نام خانوادگی",
            "name": "name",
            "aria-label": "نام کامل",
            "aria-required": "true"
        }),

    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "py-4 text-right pl-5 bg-backgroundBody dark:bg-dark focus:outline-none focus:border-primary border dark:border-dark w-full text-colorText dark:text-backgroundBody/70 text-xl leading-[1.4] tracking-[0.4px] mt-3",
            "placeholder": "09123456789",
            "name": "tel",
            "type": "tel",
            "aria-label": "شماره تلفن",
            "aria-required": "true"
        }),

    )
    SERVICE_CHOICES = [
        ('کابینت', 'کابینت'),
        ('کمد دیواری', 'کمد دیواری'),
        ('محصولات چوبی', 'محصولات چوبی'),
        ('محصولات آشپزخانه', 'محصولات آشپزخانه'),
        ('سایر موارد', 'سایر موارد'),
    ]

    service_type = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'py-4 px-5 bg-backgroundBody dark:bg-dark focus:outline-none focus:border-primary border dark:border-dark w-full text-colorText dark:text-backgroundBody/70 text-xl leading-[1.4] tracking-[0.4px] mt-3 appearance-none indent-px text-ellipsis',
            'aria-label': 'نوع سرویس',
            'aria-required': 'true',
        }),
        label='Select your Service',
        required=True,
    )

    text = forms.CharField(
        strip=False,
        widget=forms.Textarea(attrs={
            "class": "py-4 pl-5 bg-backgroundBody dark:bg-dark focus:outline-none focus:border-primary border dark:border-dark w-full text-colorText dark:text-backgroundBody/70 text-xl leading-[1.4] tracking-[0.4px] mt-3",
            "placeholder": "توضیج کوتاه",
            "name": "Message",
            "aria-label": "توضیحات پروژه",
            "aria-required": "true",
        }),
    )
