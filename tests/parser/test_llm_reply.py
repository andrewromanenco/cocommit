from cocommit.parser.llm_reply import LLMReply, LLMReplyBuilder

def sample_input():
    return """
This is sample code: <SUMMARY>multi
line summary</SUMMARY>
and <NEW-COMMIT-MESSAGE>commit
message</NEW-COMMIT-MESSAGE>
<FIXES>f1\nf2</FIXES>
<STRENGTHS>s1\ns2\ns3</STRENGTHS>
<IMPROVE>i1</IMPROVE>
"""

def test_llm_reply_builder():
    reply = LLMReplyBuilder().with_llm_reply_as_text(sample_input()).build()
    assert reply.summary == "multi\nline summary"
    assert reply.commit_message == "commit\nmessage"
    assert reply.recommendations_list == ['f1', 'f2']
    assert reply.strengths_list == ['s1', 's2', 's3']
    assert reply.improvements_list == ['i1']

def test_llm_reply_static():
    reply = LLMReply.get(sample_input())
    assert reply.summary == "multi\nline summary"
    assert reply.commit_message == "commit\nmessage"
    assert reply.recommendations_list == ['f1', 'f2']
    assert reply.strengths_list == ['s1', 's2', 's3']
    assert reply.improvements_list == ['i1']