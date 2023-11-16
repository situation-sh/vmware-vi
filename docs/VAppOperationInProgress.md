# VAppOperationInProgress

This fault is thrown when an operation is attempted on a target where a vApp operation is already in progress.  E.g. when trying to move a virtual machine from a vApp that is being powered on.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_app_operation_in_progress import VAppOperationInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of VAppOperationInProgress from a JSON string
v_app_operation_in_progress_instance = VAppOperationInProgress.from_json(json)
# print the JSON string representation of the object
print VAppOperationInProgress.to_json()

# convert the object into a dict
v_app_operation_in_progress_dict = v_app_operation_in_progress_instance.to_dict()
# create an instance of VAppOperationInProgress from a dict
v_app_operation_in_progress_form_dict = v_app_operation_in_progress.from_dict(v_app_operation_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


