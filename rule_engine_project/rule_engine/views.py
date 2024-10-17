from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Temporary store for test cases (in a real app, use the database)
test_cases = []

# Function to evaluate rules based on the provided data
def evaluate_rule(data):
    age = data.get('age')
    department = data.get('department')
    salary = data.get('salary', 0)
    experience = data.get('experience', 0)

    # Rule 1
    rule1 = (
        ((age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing')) and
        (salary > 50000 or experience > 5)
    )

    # Rule 2
    rule2 = (
        (age > 30 and department == 'Marketing') and
        (salary > 20000 or experience > 5)
    )

    return {
        'rule1': rule1,
        'rule2': rule2
    }

def index(request):
    # Passing the list of test cases to the template
    context = {
        'test_cases': test_cases
    }
    return render(request, 'index.html', context)

@csrf_exempt
def add_test_case(request):
    message = ""
    if request.method == 'POST':
        # Get data from the POST request
        description = request.POST.get('description')
        input_data = request.POST.get('input_data')
        expected_output_rule1 = request.POST.get('expected_output_rule1')
        expected_output_rule2 = request.POST.get('expected_output_rule2')

        try:
            # Convert input data from JSON format
            input_data_dict = json.loads(input_data)
            
            # Evaluate the rules using the input data
            evaluation_results = evaluate_rule(input_data_dict)
            actual_output_rule1 = 'True' if evaluation_results['rule1'] else 'False'
            actual_output_rule2 = 'True' if evaluation_results['rule2'] else 'False'

            # Append the test case to the list
            test_cases.append({
                'description': description,
                'input_data': input_data,
                'expected_output_rule1': expected_output_rule1,
                'actual_output_rule1': actual_output_rule1,
                'expected_output_rule2': expected_output_rule2,
                'actual_output_rule2': actual_output_rule2,
            })

            message = "Test case added successfully!"

        except json.JSONDecodeError:
            message = "Invalid input data format. Please provide valid JSON."

        except Exception as e:
            message = f"Error: {str(e)}"

    # Return a JSON response that contains the message
    return JsonResponse({'message': message})

