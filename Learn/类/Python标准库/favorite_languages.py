from collections import OrderedDict #创建字典并记录其中的键一值对的添加顺序

favorite_languages = OrderedDict()

favorite_languages['张凯'] = 'python'
favorite_languages['袁鹏'] = 'java'
favorite_languages['周子琦'] = 'C++'

for name,language in favorite_languages.items():
    print(name.title() + "最喜欢的语言是：" + language.title())