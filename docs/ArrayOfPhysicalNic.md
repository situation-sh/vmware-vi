# ArrayOfPhysicalNic

A boxed array of *PhysicalNic*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNic]**](PhysicalNic.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic import ArrayOfPhysicalNic

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNic from a JSON string
array_of_physical_nic_instance = ArrayOfPhysicalNic.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNic.to_json()

# convert the object into a dict
array_of_physical_nic_dict = array_of_physical_nic_instance.to_dict()
# create an instance of ArrayOfPhysicalNic from a dict
array_of_physical_nic_form_dict = array_of_physical_nic.from_dict(array_of_physical_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


