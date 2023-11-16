# ArrayOfFailoverLevelRestored

A boxed array of *FailoverLevelRestored*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FailoverLevelRestored]**](FailoverLevelRestored.md) |  | 

## Example

```python
from vmware_vi.models.array_of_failover_level_restored import ArrayOfFailoverLevelRestored

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFailoverLevelRestored from a JSON string
array_of_failover_level_restored_instance = ArrayOfFailoverLevelRestored.from_json(json)
# print the JSON string representation of the object
print ArrayOfFailoverLevelRestored.to_json()

# convert the object into a dict
array_of_failover_level_restored_dict = array_of_failover_level_restored_instance.to_dict()
# create an instance of ArrayOfFailoverLevelRestored from a dict
array_of_failover_level_restored_form_dict = array_of_failover_level_restored.from_dict(array_of_failover_level_restored_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


