"""
streams-exercise.tests.py

This file is intentionally written without the benefit of the Python
unittest library. This can be used to demonstrate in-class that unit testing
is a simple concept which benefits from the use of a library, but does not
require it.

Run with `python tests.py`. The return code will be the number of test failures.
"""

import io

from stream_exercise import StreamProcessor


failures = 0


value = "234761640930110349378289194"
expected = 5
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "03050403020309060707070708"
expected = 10
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "3"
expected = 0
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "2347"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)


value = "23478"
expected = 2
my_stream_processor = StreamProcessor(io.StringIO(value))
result = my_stream_processor.process()

success = result == expected
failures += (not success)
message = "Testing \"{}\", expected {} got {}. ".format(value, expected, result)
message += "SUCCESS" if success else "FAILURE"
print(message)



print("\n\nTest failures: {} ".format(failures))
exit(failures)
