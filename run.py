import sys


def run_rms():
    from tasks.rms import send_orders_to_rms_task


def run_sim_col():
    from tasks.sim import send_orders_to_sim_task_col

def run_sim_vzl():
    from tasks.sim import send_orders_to_sim_task_vzl


switcher = {

    "run_sim_col": run_sim_col,
    "run_rms": run_rms,
    "run_sim_vzl": run_sim_vzl
}


def execute_task(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()


execute_task(sys.argv[1])
