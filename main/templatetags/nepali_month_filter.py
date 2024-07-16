from django import template
from main.models import AayatNiryat
from django.db.models import Sum

register = template.Library()

MONTH_NAMES_NP = {
    '01': 'बैशाख',
    '02': 'जेठ',
    '03': 'असार',
    '04': 'श्रावण',
    '05': 'भदौ',
    '06': 'आश्विन',
    '07': 'कार्तिक',
    '08': 'मंसिर',
    '09': 'पुष',
    '10': 'माघ',
    '11': 'फाल्गुन',
    '12': 'चैत्र',
}

@register.filter
def nepali_month_name(month_number):
    return MONTH_NAMES_NP.get(month_number, '')


quarter_dict = {
    1: [4, 5, 6],
    2: [7, 8, 9],
    3: [10, 11, 12],
    4: [1, 2, 3]
}

def get_quarter(month, quarter_dict):
    data = []
    for qtr, values in quarter_dict.items():
        if month in values:
            # data.append(month)
            month_list = quarter_dict[qtr]
            if month == month_list[-1]:
                return month_list
            for m in month_list:
                if month >= m:
                    data.append(m)
    print(data)
    return data


    return None

@register.simple_tag
def quarterly_progress(obj):
    months=get_quarter(obj.related_month,quarter_dict)
    data=AayatNiryat.objects.filter(
       type=obj.type,
       related_month__in=months 
    ).aggregate(total= Sum('m_pragati'))['total']
    print(data)
    return data
