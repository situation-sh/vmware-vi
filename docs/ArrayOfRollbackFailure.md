# ArrayOfRollbackFailure

A boxed array of *RollbackFailure*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RollbackFailure]**](RollbackFailure.md) |  | 

## Example

```python
from vmware_vi.models.array_of_rollback_failure import ArrayOfRollbackFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRollbackFailure from a JSON string
array_of_rollback_failure_instance = ArrayOfRollbackFailure.from_json(json)
# print the JSON string representation of the object
print ArrayOfRollbackFailure.to_json()

# convert the object into a dict
array_of_rollback_failure_dict = array_of_rollback_failure_instance.to_dict()
# create an instance of ArrayOfRollbackFailure from a dict
array_of_rollback_failure_form_dict = array_of_rollback_failure.from_dict(array_of_rollback_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


