# ArrayOfVAppOperationInProgress

A boxed array of *VAppOperationInProgress*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppOperationInProgress]**](VAppOperationInProgress.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_operation_in_progress import ArrayOfVAppOperationInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppOperationInProgress from a JSON string
array_of_v_app_operation_in_progress_instance = ArrayOfVAppOperationInProgress.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppOperationInProgress.to_json()

# convert the object into a dict
array_of_v_app_operation_in_progress_dict = array_of_v_app_operation_in_progress_instance.to_dict()
# create an instance of ArrayOfVAppOperationInProgress from a dict
array_of_v_app_operation_in_progress_form_dict = array_of_v_app_operation_in_progress.from_dict(array_of_v_app_operation_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


