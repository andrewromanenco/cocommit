import cocommit.parser.response_utils as utils

class LLMReply:

    @staticmethod
    def get(llm_reply_as_text):
        return LLMReplyBuilder().with_llm_reply_as_text(llm_reply_as_text).build()

    def __init__(self, llm_reply_builder):
        self.commit_message = llm_reply_builder.commit_message
        self.summary = llm_reply_builder.summary
        self.strengths_list = llm_reply_builder.strengths_list
        self.improvements_list = llm_reply_builder.improvements_list
        self.recommendations_list = llm_reply_builder.recommendations_list


class LLMReplyBuilder:
    def __init__(self):
        self.commit_message = None
        self.summary = None
        self.strengths_list = []
        self.improvements_list = []
        self.recommendations_list = []

    def build(self):
        return LLMReply(self)
    
    def with_llm_reply_as_text(self, llm_reply_as_text):
        self.commit_message = utils.get_updated_commit_message(llm_reply_as_text)
        self.summary = utils.get_summary(llm_reply_as_text)
        self.strengths_list = utils.get_list_of_strengths(llm_reply_as_text)
        self.improvements_list = utils.get_list_of_improvements(llm_reply_as_text)
        self.recommendations_list = utils.get_list_of_recommendations(llm_reply_as_text)
        return self
