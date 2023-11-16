# UpdateProgressRequestType

The parameters of *Task.UpdateProgress*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent_done** | **int** | Percentage to set for this task  | 

## Example

```python
from vmware_vi.models.update_progress_request_type import UpdateProgressRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProgressRequestType from a JSON string
update_progress_request_type_instance = UpdateProgressRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateProgressRequestType.to_json()

# convert the object into a dict
update_progress_request_type_dict = update_progress_request_type_instance.to_dict()
# create an instance of UpdateProgressRequestType from a dict
update_progress_request_type_form_dict = update_progress_request_type.from_dict(update_progress_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


