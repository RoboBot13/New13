from ncclient import manager

m = manager.connect (
    host="ios-xe-mgmt-latest.cisco.com",
    port=10000,
    username="developer",
    password="C1csco12345",
    hostkey_verify=False
)

print ("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)

