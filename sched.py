import requests
import pprint
from collections import OrderedDict

API_URL = "http://127.0.0.1:8000/"
VECHICLE_ORDERS = "vehicle_orders/vehicle_orders/"
VECHICLE_REQUEST_URL = ''.join([API_URL, VECHICLE_ORDERS])


WORK_CENTERS = "work-centers/workcenters/"
WORK_CENTER_REQUEST_URL = ''.join([API_URL, WORK_CENTERS])


class Scheduler:

    @classmethod
    def create_workcenter_list(cls):
        # Retrieve Vehicle order
        workcenter_req = requests.get(WORK_CENTER_REQUEST_URL)
        workcenter_req = (workcenter_req.json())

        work_center_list = []
        for item in workcenter_req:
            work_center_list.append(item)

        return sorted(work_center_list, key=lambda k: k['production_type'])

    @classmethod
    def create_task_pairs(cls):
        """
        Function to create a list of pairs of tasks from a sorted list of tasks.  The longest
        task is paired with the shortest, the next longest with the next shortest and so on
        :return: A list of tuples of task pairs
        """
        time_task_list = Scheduler.create_sorted_tasks()
        task_pairs = []
        for i in range(len(time_task_list) // 2):
            task_pairs.append((time_task_list[i], time_task_list[~i]))

        return task_pairs

    @classmethod
    def create_sorted_tasks(cls, descending=None):
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

    @classmethod
    def simple_scheduler(cls, parts, work_centers):
        """
        Function that will attempt to find an optimal schedule for given production tasks \
        and available compatible work centers

        Fewer longer tasks first will produce fewer parts per 'clock tick' and as more and \
        more shorter duration tasks can be added in 'parallel' the number of parts produced \
        per 'clock tick' will maximize toward the end of the production run.

        :param parts: List of vehicle components to be processed
        :param work_centers: List of work centers for parts processing
        :return:
        """

        ###########################################################################
        #
        # Dictionary for storing the solution,
        #
        # duration -- total steps or periods of time to complete tasks
        # production_steps -- list of tuples,
        #
        schedule_map = {
            "duration": 0,
            "production_steps": [],
            "solved": False
        }

        task_distribution_histogram = {}

        while len(parts):
            # Find the maximum duration task for remaining tasks
            current_max_task = max(parts, key=lambda x: x['process_time'])
            current_max = current_max_task.get('process_time')

            # Count occurrences of tasks with this duration
            task_count = 0      # sum of tasks with identical duration
            similar_tasks = []  # temporary list to store tasks of identical duration
            for part in parts:
                if part.get('process_time') == current_max:
                    similar_tasks.append(part)
                    task_count += 1

            if current_max not in task_distribution_histogram:
                task_distribution_histogram[current_max] = [task_count, similar_tasks]

            parts.pop(0)

        # Sort histogram by keys, in this case keys are the same as the duration
        task_distribution_histogram = OrderedDict(sorted(task_distribution_histogram.items(),
                                                         reverse=True))

        # Pretty print task_distribution_histogram
        pprint.pprint(task_distribution_histogram)

        return schedule_map


# Create sorted list of tasks,
tasks = Scheduler.create_sorted_tasks(True)

# Create list of workcenters
centers = Scheduler.create_workcenter_list()

# Invoke scheduler, (currently only creates histogram of tasks arranged by duration)
Scheduler.simple_scheduler(tasks, centers)

