# VAppNotRunning

A virtual machine in a vApp cannot be powered on unless the parent vApp is running.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_app_not_running import VAppNotRunning

# TODO update the JSON string below
json = "{}"
# create an instance of VAppNotRunning from a JSON string
v_app_not_running_instance = VAppNotRunning.from_json(json)
# print the JSON string representation of the object
print VAppNotRunning.to_json()

# convert the object into a dict
v_app_not_running_dict = v_app_not_running_instance.to_dict()
# create an instance of VAppNotRunning from a dict
v_app_not_running_form_dict = v_app_not_running.from_dict(v_app_not_running_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


