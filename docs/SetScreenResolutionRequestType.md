# SetScreenResolutionRequestType

The parameters of *VirtualMachine.SetScreenResolution*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | The screen width that should be set.  | 
**height** | **int** | The screen height that should be set.  | 

## Example

```python
from vmware_vi.models.set_screen_resolution_request_type import SetScreenResolutionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetScreenResolutionRequestType from a JSON string
set_screen_resolution_request_type_instance = SetScreenResolutionRequestType.from_json(json)
# print the JSON string representation of the object
print SetScreenResolutionRequestType.to_json()

# convert the object into a dict
set_screen_resolution_request_type_dict = set_screen_resolution_request_type_instance.to_dict()
# create an instance of SetScreenResolutionRequestType from a dict
set_screen_resolution_request_type_form_dict = set_screen_resolution_request_type.from_dict(set_screen_resolution_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


