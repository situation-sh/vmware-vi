# RollbackFailure

Thrown if a Rollback operation fails  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The entity name on which rollback failed  ***Since:*** vSphere API 5.1  | 
**entity_type** | **str** | The entity type on which rollback failed  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.rollback_failure import RollbackFailure

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackFailure from a JSON string
rollback_failure_instance = RollbackFailure.from_json(json)
# print the JSON string representation of the object
print RollbackFailure.to_json()

# convert the object into a dict
rollback_failure_dict = rollback_failure_instance.to_dict()
# create an instance of RollbackFailure from a dict
rollback_failure_form_dict = rollback_failure.from_dict(rollback_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


