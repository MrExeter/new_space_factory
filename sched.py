import requests
from pprint import pprint
from collections import Counter

API_URL = "http://127.0.0.1:8000/"
VECHICLE_ORDERS = "vehicle_orders/vehicle_orders/"
VECHICLE_REQUEST_URL = ''.join([API_URL, VECHICLE_ORDERS])


WORK_CENTERS = "work-centers/workcenters/"
WORK_CENTER_REQUEST_URL = ''.join([API_URL, WORK_CENTERS])


class Scheduler:

    @classmethod
    def create_workcenter_list(cls):
        """Create list of available workcenters"""
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
    def create_task_duration_histogram(cls, parts):
        """
        Function that creates a histogram of task durations

        :param parts: List of vehicle components to be processed
        :param work_centers: List of work centers for parts processing
        :return: A sorted dictionary (descending order by key value) and the mapped
        value contains a list of tasks with that duration
        """

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
                task_distribution_histogram[current_max] = similar_tasks

            parts.pop(0)

        return task_distribution_histogram

    @classmethod
    def create_workcenter_histogram(cls, work_centers):
        """
        Create histogram of work-centers based on facility type and frequency
        :param work_centers: list of available work centers
        :return: histogram of work-centers
        """
        wc_histogram = {}
        x = Counter(wc['production_type'] for wc in work_centers)
        x_keys = dict(x).keys()

        for key in x_keys:
            similar_work_centers = []
            for element in work_centers:
                if element.get('production_type') == key:
                    similar_work_centers.append(element)

            wc_histogram[key] = similar_work_centers

        return wc_histogram

    @classmethod
    def scheduler(cls, task_histogram, work_centers):
        """
        Calculates a schedule for a given set of tasks and durations
        :param task_histogram: histogram of tasks based on duration
        :return: dictionary with following stucture
        {
            duration: total duration time,
            "production_steps": detail of units produced at each time step,
            "solved": boolean flag indicates if a solution was reached.
        }
        """
        ###########################################################################
        #
        # Dictionary for storing the solution,
        # of the form
        # { time step: [list of completed activities] }
        #
        # Each completed activity represents a part or vehicle component paired with a compatible
        # facility, with a start time and finish time.
        # ( Vehicle component, work center, start, finish)
        #
        #
        schedule_map = {}

        task_duration_keys = list(task_histogram.keys())

        total_time_steps = 0
        current_time_step = 0
        delta_time_step = 0
        current_activities = []

        while task_duration_keys:
            # While there are tasks to schedule

            ###################################################################
            # Get longest and next longest duration tasks
            #
            current_duration = task_duration_keys[0]
            next_duration = task_duration_keys[1] if len(task_duration_keys) > 1 else 0

            delta_time_step = current_duration - next_duration
            current_tasks = task_histogram.get(current_duration)

            ###################################################################
            # Clear out any activities that are finished, free up the work center
            # and add to the solution
            completed_activities = [x for x in current_activities if x[2].get('finish') <= current_time_step]
            schedule_map[current_time_step] = completed_activities

            ###################################################################
            # Reset facilities in completed activities to is_avaiable = True
            #
            for activity in completed_activities:
                activity[1]['is_available'] = True

            ###################################################################
            # match current tasks with available work centers
            # set 'taken' work centers to not available
            for task in current_tasks:
                required_type = task.get('facility_required')

                work_centers_of_type = work_centers.get(required_type)

                for work_center in work_centers_of_type:
                    if work_center.get('is_available') and not task.get('is_assigned'):
                        work_center['is_available'] = False
                        task['is_assigned'] = True
                        activity = (task, work_center,
                                    {'start': current_time_step,
                                     'finish': current_time_step + current_duration})

                        # Add new activity to the list of current activities
                        current_activities.append(activity)

            if len(task_duration_keys) <= 1:
                completed_activities = [x for x in current_activities]
                schedule_map[current_time_step] = completed_activities

            task_duration_keys.pop(0)
            current_time_step += (current_duration - next_duration)

        return schedule_map


# Create sorted list of tasks,
tasks = Scheduler.create_sorted_tasks(True)

# Create list of workcenters
centers = Scheduler.create_workcenter_list()

# Get task histogram
task_histogram = Scheduler.create_task_duration_histogram(tasks)

# Get work center histogram
work_center_histogram = Scheduler.create_workcenter_histogram(centers)

schedule = Scheduler.scheduler(task_histogram, work_center_histogram)

pprint(schedule)
