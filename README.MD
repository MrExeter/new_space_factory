# Space Factory

###  Python 3.6
### _install requirements from requirements.txt_

### _install a virtual environment in the root directory_

This is an initial prototype of a factory scheduling system.  The item being manufactured is irrelevant as the model could be changed to produce "widgets" or "doohickies".  For this example, I am assembling space vehicles.

An order is a workorder for a new vehicle.

The order contains a BOM (bill of materials) or a parts list.

The BOM is a list of parts or components that are to be assembled into a finished craft.  Each line item lists the vehicle component and quantity.

Vehicle components are the individual parts.  Components require a certain amount of time to process or duration as well as requiring a "type" of processing e.g., (electrical, machining, painting, assembly)

Work centers accept components for processing and similarly they can only perform certain types of processing e.g. (electrical, machining, painting, assembly).  In addition, a work center can only process one component at a time and requires the time duration specified by the particular component.  For example a component that requires 3 time units and "electrical" processing can only go to an "electrical" type work center and will occupy that work center for 3 time units.


In this example, the schedule of the production of a vehicle order is such that all of the parts arrive at the last operation at nearly the same time for final integration.  Components requiring longer processing duration are scheduled first and systematically and increasing number of shorter duration processes are added so as to achieve the maximum number of parts nearest the end of production.


A more sophisticated approach could maximize groups of parts to be produced at various deadlines during the production.


To run, start the flask server, either use the existing vehicle order or create a new one.

To create a schedule, execute sched.py (located in the scheduler directory).

The output shows the sequence of components being processed.  It is in the form of a dictionary with the key representing the time step and the value being parts or tasks completed during that time step.


### Additional browser based documentation is available in /documents/_build/html/


_open index.html in your browser_


