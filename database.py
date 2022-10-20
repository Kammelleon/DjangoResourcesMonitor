import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect(r"C:\Users\kamil\PycharmProjects\resources_monitor_django\resources_usage.db")
        self.cur = self.con.cursor()

    def get_resources_usage(self):
        resources_usage = self.cur.execute("SELECT * FROM resources")
        resources_usage = resources_usage.fetchall()
        return resources_usage

    def send_resources_usage(self, cpu, ram, network_in, network_out, disk_capacity, disk_space_used):
        self.cur.execute(f"INSERT INTO resources(cpu, ram, network_in, network_out, disk_capacity, disk_space_used) "
                         f"VALUES({cpu},{ram},{network_in},{network_out},{disk_capacity},{disk_space_used})")
