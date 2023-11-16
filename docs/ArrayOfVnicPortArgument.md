# ArrayOfVnicPortArgument

A boxed array of *VnicPortArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VnicPortArgument]**](VnicPortArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vnic_port_argument import ArrayOfVnicPortArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVnicPortArgument from a JSON string
array_of_vnic_port_argument_instance = ArrayOfVnicPortArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfVnicPortArgument.to_json()

# convert the object into a dict
array_of_vnic_port_argument_dict = array_of_vnic_port_argument_instance.to_dict()
# create an instance of ArrayOfVnicPortArgument from a dict
array_of_vnic_port_argument_form_dict = array_of_vnic_port_argument.from_dict(array_of_vnic_port_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


