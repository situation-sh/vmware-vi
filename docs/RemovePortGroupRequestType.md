# RemovePortGroupRequestType

The parameters of *HostNetworkSystem.RemovePortGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pg_name** | **str** |  | 

## Example

```python
from vmware_vi.models.remove_port_group_request_type import RemovePortGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemovePortGroupRequestType from a JSON string
remove_port_group_request_type_instance = RemovePortGroupRequestType.from_json(json)
# print the JSON string representation of the object
print RemovePortGroupRequestType.to_json()

# convert the object into a dict
remove_port_group_request_type_dict = remove_port_group_request_type_instance.to_dict()
# create an instance of RemovePortGroupRequestType from a dict
remove_port_group_request_type_form_dict = remove_port_group_request_type.from_dict(remove_port_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


