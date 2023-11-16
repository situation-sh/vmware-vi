# ArrayOfDVSRollbackCapability

A boxed array of *DVSRollbackCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSRollbackCapability]**](DVSRollbackCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_rollback_capability import ArrayOfDVSRollbackCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSRollbackCapability from a JSON string
array_of_dvs_rollback_capability_instance = ArrayOfDVSRollbackCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSRollbackCapability.to_json()

# convert the object into a dict
array_of_dvs_rollback_capability_dict = array_of_dvs_rollback_capability_instance.to_dict()
# create an instance of ArrayOfDVSRollbackCapability from a dict
array_of_dvs_rollback_capability_form_dict = array_of_dvs_rollback_capability.from_dict(array_of_dvs_rollback_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


