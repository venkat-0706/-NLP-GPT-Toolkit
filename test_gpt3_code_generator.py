import pytest
import builtins
from unittest.mock import patch
import gpt3_code_generator_with_key_v2 as gpt3

# Mock the openai.ChatCompletion.create method to avoid actual API calls during tests
class MockResponse:
    def __init__(self, content):
        self.choices = [type('obj', (object,), {'message': type('obj', (object,), {'content': content})})()]

def mock_create(*args, **kwargs):
    prompt = kwargs.get('messages')[0]['content']
    # Return a simple echo of the prompt for testing
    return MockResponse(f"Mocked response for prompt: {prompt}")

@patch('openai.ChatCompletion.create', side_effect=mock_create)
def test_exploratory_data_analysis(mock_api):
    dataset_desc = "columns: 'age', 'salary', 'department'"
    result = gpt3.exploratory_data_analysis(dataset_desc)
    assert "Mocked response" in result

@patch('openai.ChatCompletion.create', side_effect=mock_create)
def test_data_visualization(mock_api):
    dataset_desc = "columns: 'age', 'salary', 'department'"
    result = gpt3.data_visualization(dataset_desc)
    assert "Mocked response" in result

@patch('openai.ChatCompletion.create', side_effect=mock_create)
def test_generate_resume(mock_api):
    experience = "Experienced software engineer with Python skills."
    result = gpt3.generate_resume(experience)
    assert "Mocked response" in result

@patch('openai.ChatCompletion.create', side_effect=mock_create)
def test_generate_interview_questions(mock_api):
    result = gpt3.generate_interview_questions("Python", 3)
    assert "Mocked response" in result

@patch('openai.ChatCompletion.create', side_effect=mock_create)
def test_generate_meeting_summary(mock_api):
    notes = "Max: Profits up 50%"
    result = gpt3.generate_meeting_summary(notes)
    assert "Mocked response" in result

if __name__ == "__main__":
    pytest.main()
