# InsufficientPerCpuCapacity

The host does not have enough per CPU capacity.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_per_cpu_capacity import InsufficientPerCpuCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientPerCpuCapacity from a JSON string
insufficient_per_cpu_capacity_instance = InsufficientPerCpuCapacity.from_json(json)
# print the JSON string representation of the object
print InsufficientPerCpuCapacity.to_json()

# convert the object into a dict
insufficient_per_cpu_capacity_dict = insufficient_per_cpu_capacity_instance.to_dict()
# create an instance of InsufficientPerCpuCapacity from a dict
insufficient_per_cpu_capacity_form_dict = insufficient_per_cpu_capacity.from_dict(insufficient_per_cpu_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


