### Issue1
`$ python3 issue1.py`
###Issue2
`$ pytest -v issue2.py`
```
====================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3.6
cachedir: .pytest_cache
rootdir: /home/konstantin/PycharmProjects/mai_python/testing_tools
collected 3 items                                                                                                                                                                                                               

issue2.py::test_decode[-- .- ..-MAI] PASSED                                                                                                                                                                               [ 33%]
issue2.py::test_decode[.... . .-.. .-.. ----HELLO] PASSED                                                                                                                                                                 [ 66%]
issue2.py::test_decode[-- . ... ... .- --. .-MESSAGE] PASSED                                                                                                                                                              [100%]

======================================================================================================= 3 passed in 0.01s =======================================================================================================
```
###Issue3
`$ python3 issue1.py`
```
Ran 5 tests in 0.009s

OK
```
###Issue4
`$ pytest -v issue4.py`
```
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3.6
cachedir: .pytest_cache
rootdir: /home/konstantin/PycharmProjects/mai_python/testing_tools
collected 5 items                                                                                                                                                                                                               

issue4.py::test_args[input_data0-expected0] PASSED                                                                                                                                                                        [ 20%]
issue4.py::test_empty_arg PASSED                                                                                                                                                                                          [ 40%]
issue4.py::test_empty_arglist PASSED                                                                                                                                                                                      [ 60%]
issue4.py::test_not_string_input PASSED                                                                                                                                                                                   [ 80%]
issue4.py::test_res_type PASSED                                                                                                                                                                                           [100%]

======================================================================================================= 5 passed in 0.02s =======================================================================================================
```
###Issue5
`python -m pytest issue5.py --cov=testing_tools.what_is_year_now --cov-report html`
