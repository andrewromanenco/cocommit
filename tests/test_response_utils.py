from cocommit.response_utils import get_list_of_recommendations, get_updated_commit_message

def test_new_commit_message():
    assert get_updated_commit_message("123<NEW-COMMIT-MESSAGE>msg\nmsg</NEW-COMMIT-MESSAGE>456") == "msg\nmsg"

def test_no_new_commit_message():
    assert get_updated_commit_message("123456") == None

def test_recommendations():
    result = get_list_of_recommendations("123<FIXES>one\ntwo\nthree</FIXES>456")
    assert result == ['one', 'two', 'three']

def test_empty_recommendations():
    result = get_list_of_recommendations("123<FIXES></FIXES>456")
    assert result == []

def test_no_recommendations():
    result = get_list_of_recommendations("123456")
    assert result == []