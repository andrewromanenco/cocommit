from cocommit.parser.response_utils import get_list_of_improvements, get_list_of_recommendations, get_list_of_strengths, get_summary, get_updated_commit_message

def test_new_commit_message():
    assert get_updated_commit_message("123<NEW-COMMIT-MESSAGE>msg\nmsg</NEW-COMMIT-MESSAGE>456") == "msg\nmsg"

def test_no_new_commit_message():
    assert get_updated_commit_message("123456") is None

def test_summary_message():
    assert get_summary("123<SUMMARY>msg\nmsg</SUMMARY>456") == "msg\nmsg"

def test_no_summary_message():
    assert get_summary("123456") is None

def test_recommendations():
    result = get_list_of_recommendations("123<FIXES>one\ntwo\nthree</FIXES>456")
    assert result == ['one', 'two', 'three']

def test_empty_recommendations():
    result = get_list_of_recommendations("123<FIXES></FIXES>456")
    assert result == []

def test_no_recommendations():
    result = get_list_of_recommendations("123456")
    assert result == []

def test_strengths():
    result = get_list_of_strengths("123<STRENGTHS>one\ntwo\nthree</STRENGTHS>456")
    assert result == ['one', 'two', 'three']

def test_empty_strengths():
    result = get_list_of_strengths("123<STRENGTHS></STRENGTHS>456")
    assert result == []

def test_no_strengths():
    result = get_list_of_strengths("123456")
    assert result == []

def test_improvements():
    result = get_list_of_improvements("123<IMPROVE>one\ntwo\nthree</IMPROVE>456")
    assert result == ['one', 'two', 'three']

def test_empty_improvements():
    result = get_list_of_improvements("123<IMPROVE></IMPROVE>456")
    assert result == []

def test_no_improvements():
    result = get_list_of_improvements("123456")
    assert result == []
