# ArrayOfDVPortStatus

A boxed array of *DVPortStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVPortStatus]**](DVPortStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dv_port_status import ArrayOfDVPortStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVPortStatus from a JSON string
array_of_dv_port_status_instance = ArrayOfDVPortStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVPortStatus.to_json()

# convert the object into a dict
array_of_dv_port_status_dict = array_of_dv_port_status_instance.to_dict()
# create an instance of ArrayOfDVPortStatus from a dict
array_of_dv_port_status_form_dict = array_of_dv_port_status.from_dict(array_of_dv_port_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


