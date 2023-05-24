#!/bin/bash

(
cd ..
pytest ./py_lab/my_time_date/current_time_test.py::test_it_should_return_the_current_time -sv
)

