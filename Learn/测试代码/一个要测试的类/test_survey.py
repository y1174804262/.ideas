import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "你最早学的语言是"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinese','English','Spanish']

    def test_store_single_response(self):
            self.my_survey.store_response(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
            """测试三个答案会被妥善地存储"""
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)
unittest.main()


    # def test_store()_single_response(self):
    #     """测试单个答案会被妥善存储"""
    #     question = "你的母语是？"
    #     my_survey = AnonymousSurvey(question)
    #     my_survey.store_response('Chinese')
    #
    #     self.assertIn('Chinese',my_survey.responses)
    #
    # def test_store_three_response(self):
    #     """测试三个答案会被妥善的存储"""
    #     question = "你的母语是?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['Chinese','English','Spanish']
    #
    #     for response in responses:
    #         my_survey.store_response(response)
    #     for response in responses:
    #         self.assertIn(response,my_survey.responses)

unittest.main
