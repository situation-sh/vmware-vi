# ArrayOfHealthUpdate

A boxed array of *HealthUpdate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HealthUpdate]**](HealthUpdate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_health_update import ArrayOfHealthUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHealthUpdate from a JSON string
array_of_health_update_instance = ArrayOfHealthUpdate.from_json(json)
# print the JSON string representation of the object
print ArrayOfHealthUpdate.to_json()

# convert the object into a dict
array_of_health_update_dict = array_of_health_update_instance.to_dict()
# create an instance of ArrayOfHealthUpdate from a dict
array_of_health_update_form_dict = array_of_health_update.from_dict(array_of_health_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


