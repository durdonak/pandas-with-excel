# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZBe4Q1N2gMhxfHK6yJzbojw5xhQCwRBd
"""

import pandas as pd
teachers = pd.DataFrame({
            'FISH': [ "Qadamova Zulayho",  "Karimov S", "Azizov I", "Ibragimov N", "To'rayeva M", "Xusanova M", "Muxtarov N","Ibragimov N"  ],
            "Fani": [ "Sun'it intellekt asoslari", "Sun'iy intelekt asoslari", "Sotib olish tamoyillari", "Mikroiqtisodiyot", "Sotib olish tamoyillari", "Kiberxavsizlik asoslari", "Mikroiqtisodiyot", "Bugalteriya hisobi va tamoyillari"   ],
            "Mashg'ulot turi": [ "amaliy", "maruza", "maruza", "maruza", "amaliyot",  "maruza", 'amaliy', 'maruza'  ],
            "Kafedrasi": [ "Axbotot texnologiyari", "Axborot texnologiyari", "Gumanitar fanlar", "Gumanitar fanlar", "iqtisodiyot",  "Kiberxavsizlik", "Gumanitar fanlar", 'Gumanitar fanlar'  ]
})
print(teachers)

teachers.to_excel("660-23 guruh's.xlsx")