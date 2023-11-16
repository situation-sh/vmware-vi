# ArrayOfHostPortGroupPort

A boxed array of *HostPortGroupPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPortGroupPort]**](HostPortGroupPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_port_group_port import ArrayOfHostPortGroupPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPortGroupPort from a JSON string
array_of_host_port_group_port_instance = ArrayOfHostPortGroupPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPortGroupPort.to_json()

# convert the object into a dict
array_of_host_port_group_port_dict = array_of_host_port_group_port_instance.to_dict()
# create an instance of ArrayOfHostPortGroupPort from a dict
array_of_host_port_group_port_form_dict = array_of_host_port_group_port.from_dict(array_of_host_port_group_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


