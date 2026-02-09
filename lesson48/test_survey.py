import pytest

from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak? "
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response("English")
    assert 'English' in language_survey.responses
    
def test_store_three_response(language_survey):
    responses = ['English', "Turkish", 'Germany']
    for res in responses:
        language_survey.store_response(res)

    for res in responses:
            assert res in language_survey.responses