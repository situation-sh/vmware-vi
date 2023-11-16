# NotEnoughLogicalCpus

The host hardware does not have enough logical CPUs (hyperthreads) to support the number of virtual CPUs in the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.not_enough_logical_cpus import NotEnoughLogicalCpus

# TODO update the JSON string below
json = "{}"
# create an instance of NotEnoughLogicalCpus from a JSON string
not_enough_logical_cpus_instance = NotEnoughLogicalCpus.from_json(json)
# print the JSON string representation of the object
print NotEnoughLogicalCpus.to_json()

# convert the object into a dict
not_enough_logical_cpus_dict = not_enough_logical_cpus_instance.to_dict()
# create an instance of NotEnoughLogicalCpus from a dict
not_enough_logical_cpus_form_dict = not_enough_logical_cpus.from_dict(not_enough_logical_cpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


