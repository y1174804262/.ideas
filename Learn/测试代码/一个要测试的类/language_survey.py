from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("输入q就可以退出")

while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调查结果
print("\n感谢参与调研的每一个人")
my_survey.show_results()