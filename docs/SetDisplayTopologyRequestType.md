# SetDisplayTopologyRequestType

The parameters of *VirtualMachine.SetDisplayTopology*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displays** | [**List[VirtualMachineDisplayTopology]**](VirtualMachineDisplayTopology.md) | The topology for each monitor that the virtual machine&#39;s display must span.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.set_display_topology_request_type import SetDisplayTopologyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetDisplayTopologyRequestType from a JSON string
set_display_topology_request_type_instance = SetDisplayTopologyRequestType.from_json(json)
# print the JSON string representation of the object
print SetDisplayTopologyRequestType.to_json()

# convert the object into a dict
set_display_topology_request_type_dict = set_display_topology_request_type_instance.to_dict()
# create an instance of SetDisplayTopologyRequestType from a dict
set_display_topology_request_type_form_dict = set_display_topology_request_type.from_dict(set_display_topology_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


