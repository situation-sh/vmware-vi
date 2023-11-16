# ArrayOfNoVirtualNic

A boxed array of *NoVirtualNic*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoVirtualNic]**](NoVirtualNic.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_virtual_nic import ArrayOfNoVirtualNic

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoVirtualNic from a JSON string
array_of_no_virtual_nic_instance = ArrayOfNoVirtualNic.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoVirtualNic.to_json()

# convert the object into a dict
array_of_no_virtual_nic_dict = array_of_no_virtual_nic_instance.to_dict()
# create an instance of ArrayOfNoVirtualNic from a dict
array_of_no_virtual_nic_form_dict = array_of_no_virtual_nic.from_dict(array_of_no_virtual_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


