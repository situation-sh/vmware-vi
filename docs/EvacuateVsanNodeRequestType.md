# EvacuateVsanNodeRequestType

The parameters of *HostVsanSystem.EvacuateVsanNode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintenance_spec** | [**HostMaintenanceSpec**](HostMaintenanceSpec.md) |  | 
**timeout** | **int** | Time to wait for the task to complete in seconds. If the value is less than or equal to zero, there is no timeout. The operation fails with a Timedout exception if it timed out.  | 

## Example

```python
from vmware_vi.models.evacuate_vsan_node_request_type import EvacuateVsanNodeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EvacuateVsanNodeRequestType from a JSON string
evacuate_vsan_node_request_type_instance = EvacuateVsanNodeRequestType.from_json(json)
# print the JSON string representation of the object
print EvacuateVsanNodeRequestType.to_json()

# convert the object into a dict
evacuate_vsan_node_request_type_dict = evacuate_vsan_node_request_type_instance.to_dict()
# create an instance of EvacuateVsanNodeRequestType from a dict
evacuate_vsan_node_request_type_form_dict = evacuate_vsan_node_request_type.from_dict(evacuate_vsan_node_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


