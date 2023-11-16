# PowerDownHostToStandByRequestType

The parameters of *HostSystem.PowerDownHostToStandBy_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_sec** | **int** | The task completes when the host successfully enters standby mode and stops sending heartbeat signals. If heartbeats are still coming after timeoutSecs seconds, the host is declared timedout, and the task is assumed failed.  | 
**evacuate_powered_off_vms** | **bool** | This is a parameter used only by VirtualCenter. If set to true, for a DRS disabled cluster, the task will not succeed unless all powered-off virtual machines have been manually reregistered; for a DRS enabled cluster, VirtualCenter will automatically reregister powered-off virtual machines and a powered-off virtual machine may remain at the host only for two reasons: (a) no compatible host found for reregistration, (b) DRS is disabled for the virtual machine.  | [optional] 

## Example

```python
from vmware_vi.models.power_down_host_to_stand_by_request_type import PowerDownHostToStandByRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PowerDownHostToStandByRequestType from a JSON string
power_down_host_to_stand_by_request_type_instance = PowerDownHostToStandByRequestType.from_json(json)
# print the JSON string representation of the object
print PowerDownHostToStandByRequestType.to_json()

# convert the object into a dict
power_down_host_to_stand_by_request_type_dict = power_down_host_to_stand_by_request_type_instance.to_dict()
# create an instance of PowerDownHostToStandByRequestType from a dict
power_down_host_to_stand_by_request_type_form_dict = power_down_host_to_stand_by_request_type.from_dict(power_down_host_to_stand_by_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


