# import os

# from airflow.decorators import dag, task

# dag_id = os.path.basename(__file__).split('.')[0]


# @dag(
#     dag_id=dag_id,
#     schedule=None,
# )
# def task_flow():
#     """
#     This dag contains two dependent tasks: the second task
#     will run only after the first task
#     """

#     @task(task_id='dependent_first_task')
#     def first_task():
#         print('First task')

#     @task(task_id='dependent_second_task')
#     def second_task():
#         print('Second task')

#     first_task() >> second_task()


# task_flow()

import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()