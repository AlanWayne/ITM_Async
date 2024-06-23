task_1: cls
	@/bin/python3 src/task_1.py

task_2: cls
	@/bin/python3 src/task_2.py

task_3: cls
	@/bin/python3 src/task_3.py

task_4: cls
	@/bin/python3 src/task_4.py

test: cls
	@/bin/python3 -m pytest -vv tests/

profile_time_1:
	@/bin/python3 profiler_time/profile_time_task_1.py

profile_time_2:
	@/bin/python3 profiler_time/profile_time_task_2.py

profile_time_3:
	@/bin/python3 profiler_time/profile_time_task_3.py

profile_time_4:
	@/bin/python3 profiler_time/profile_time_task_4.py

profile_time: profile_time_1 profile_time_2 profile_time_3 profile_time_4

clean: cls
	@rm -rf text
	@rm -rf log

cls:
	@clear