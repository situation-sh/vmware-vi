# MoveDVPortRequestType

The parameters of *DistributedVirtualSwitch.MoveDVPort_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **List[str]** | The keys of the ports to be moved into the portgroup.  | 
**destination_portgroup_key** | **str** | The key of the portgroup to be moved into. If unset, the port will be moved under the switch.  | [optional] 

## Example

```python
from vmware_vi.models.move_dv_port_request_type import MoveDVPortRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveDVPortRequestType from a JSON string
move_dv_port_request_type_instance = MoveDVPortRequestType.from_json(json)
# print the JSON string representation of the object
print MoveDVPortRequestType.to_json()

# convert the object into a dict
move_dv_port_request_type_dict = move_dv_port_request_type_instance.to_dict()
# create an instance of MoveDVPortRequestType from a dict
move_dv_port_request_type_form_dict = move_dv_port_request_type.from_dict(move_dv_port_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


