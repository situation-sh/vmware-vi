# RemoveFailed

This fault is thrown when the client attempts to remove an object that has active related objects (for example, a role that has active permissions). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.remove_failed import RemoveFailed

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFailed from a JSON string
remove_failed_instance = RemoveFailed.from_json(json)
# print the JSON string representation of the object
print RemoveFailed.to_json()

# convert the object into a dict
remove_failed_dict = remove_failed_instance.to_dict()
# create an instance of RemoveFailed from a dict
remove_failed_form_dict = remove_failed.from_dict(remove_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


