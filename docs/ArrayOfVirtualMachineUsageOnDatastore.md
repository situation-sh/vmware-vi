# ArrayOfVirtualMachineUsageOnDatastore

A boxed array of *VirtualMachineUsageOnDatastore*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineUsageOnDatastore]**](VirtualMachineUsageOnDatastore.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_usage_on_datastore import ArrayOfVirtualMachineUsageOnDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineUsageOnDatastore from a JSON string
array_of_virtual_machine_usage_on_datastore_instance = ArrayOfVirtualMachineUsageOnDatastore.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineUsageOnDatastore.to_json()

# convert the object into a dict
array_of_virtual_machine_usage_on_datastore_dict = array_of_virtual_machine_usage_on_datastore_instance.to_dict()
# create an instance of ArrayOfVirtualMachineUsageOnDatastore from a dict
array_of_virtual_machine_usage_on_datastore_form_dict = array_of_virtual_machine_usage_on_datastore.from_dict(array_of_virtual_machine_usage_on_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


