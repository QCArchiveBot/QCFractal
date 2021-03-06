import fireworks
import qcfractal

lpad = fireworks.LaunchPad.from_file("fw_lpad.yaml") 
server = qcfractal.FractalServer(port=7777, storage_project_name="qca_fw_testing_server", queue_socket=lpad)

# Uncomment and run to blow away all server state
lpad.reset(None, require_password=False)
server.storage.client.drop_database("qca_fw_testing_server")
server.storage.init_database()

server.start()
