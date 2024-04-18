shell mpremote mip install unittest
rsync -m tests/ /pyboard/tests/
shell mpremote run tools/run_tests_on_hardware.py
rm -r /pyboard/tests
rm -r /pyboard/lib/unittest
