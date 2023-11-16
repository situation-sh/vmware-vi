# HostSnmpDestination

Defines a receiver for SNMP Notifications 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | A system listening for SNMP notifications.  These must be a IPv4 unicast address or resolvable dns name.  | 
**port** | **int** | UDP port to Notification receiver is listening on.  udp/162 is the reserved port  | 
**community** | **str** |  | 

## Example

```python
from vmware_vi.models.host_snmp_destination import HostSnmpDestination

# TODO update the JSON string below
json = "{}"
# create an instance of HostSnmpDestination from a JSON string
host_snmp_destination_instance = HostSnmpDestination.from_json(json)
# print the JSON string representation of the object
print HostSnmpDestination.to_json()

# convert the object into a dict
host_snmp_destination_dict = host_snmp_destination_instance.to_dict()
# create an instance of HostSnmpDestination from a dict
host_snmp_destination_form_dict = host_snmp_destination.from_dict(host_snmp_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


