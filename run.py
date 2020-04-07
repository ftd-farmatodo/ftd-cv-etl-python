import sys

def run_rms():
    from tasks.rms import send_orders_to_rms_task

def run_sim():
    from tasks.sim import send_orders_to_sim_task

switcher = {

    "run_sim": run_sim,
    "run_rms": run_rms
}


def execute_task(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()

execute_task(sys.argv[1])

