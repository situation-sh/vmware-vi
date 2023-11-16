# RefreshDVPortStateRequestType

The parameters of *DistributedVirtualSwitch.RefreshDVPortState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_keys** | **List[str]** | The keys of the ports to be refreshed. If not specified, all port states are refreshed.  | [optional] 

## Example

```python
from vmware_vi.models.refresh_dv_port_state_request_type import RefreshDVPortStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshDVPortStateRequestType from a JSON string
refresh_dv_port_state_request_type_instance = RefreshDVPortStateRequestType.from_json(json)
# print the JSON string representation of the object
print RefreshDVPortStateRequestType.to_json()

# convert the object into a dict
refresh_dv_port_state_request_type_dict = refresh_dv_port_state_request_type_instance.to_dict()
# create an instance of RefreshDVPortStateRequestType from a dict
refresh_dv_port_state_request_type_form_dict = refresh_dv_port_state_request_type.from_dict(refresh_dv_port_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


