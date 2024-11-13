 import json

def handler(event, context):
    try:
        # Extract parameters from the query string
        operation = event.get('queryStringParameters', {}).get('operation')
        num1_str = event.get('queryStringParameters', {}).get('num1', '0')
        num2_str = event.get('queryStringParameters', {}).get('num2', '0')

        # Validate if 'num1' and 'num2' can be converted to floats
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid number format for num1 or num2'})
            }

        # Perform the calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Cannot divide by zero'})
                }
            result = num1 / num2
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid operation'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
