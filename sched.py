import requests
import pprint
import json

API_URL = "http://127.0.0.1:8000/"
VECHICLE_ORDERS = "vehicle_orders/vehicle_orders/"
VECHICLE_REQUEST_URL = ''.join([API_URL, VECHICLE_ORDERS])


def create_task_pairs():
    """
    Function to create a list of pairs of tasks from a sorted list of tasks.  The longest
    task is paired with the shortest, the next longest with the next shortest and so on
    :return: A list of tuples of task pairs
    """
    time_task_list = create_sorted_tasks()
    task_pairs = []
    for i in range(len(time_task_list) // 2):
        task_pairs.append((time_task_list[i], time_task_list[~i]))
        # print(time_task_list[i][1], time_task_list[~i][1])

    return task_pairs


def create_sorted_tasks(descending=None):
    """
    Function that creates a list of vehicle-components (tasks) and sorts them
    by processing time
    :param descending: boolean flag for sort order, default is ascending, set
    to True for descending
    :return: Sorted list of vehicle-components based on processing time.
    """
    if descending:
        reverse_it = True
    else:
        reverse_it = False

    # Retrieve Vehicle order
    vehicle_order_req = requests.get(VECHICLE_REQUEST_URL)
    vehicle_order_req = (vehicle_order_req.json())[0]

    # Retrieve the BOM (bill of materials) from the vehicle order
    the_bom_req = vehicle_order_req.get("bill_of_materials")
    the_bom_req = requests.get(the_bom_req).json()

    # Retrieve the list of vehicle components from the BOM
    vehicle_component_list = the_bom_req.get('vehicle_parts')

    time_task_list = []
    for i in vehicle_component_list:
        time_task_list.append((requests.get(i)).json())

    return sorted(time_task_list, key=lambda k: k['process_time'], reverse=reverse_it)


# for pair in create_task_pairs():
#     print(pair)


for task in create_sorted_tasks(descending=True):
    print(task)
