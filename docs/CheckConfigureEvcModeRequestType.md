# CheckConfigureEvcModeRequestType

The parameters of *ClusterEVCManager.CheckConfigureEvcMode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evc_mode_key** | **str** | A key referencing the desired EVC mode.  | 
**evc_graphics_mode_key** | **str** | A key referencing the desired EVC Graphics mode *Capability.supportedEVCGraphicsMode*.  | [optional] 

## Example

```python
from vmware_vi.models.check_configure_evc_mode_request_type import CheckConfigureEvcModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckConfigureEvcModeRequestType from a JSON string
check_configure_evc_mode_request_type_instance = CheckConfigureEvcModeRequestType.from_json(json)
# print the JSON string representation of the object
print CheckConfigureEvcModeRequestType.to_json()

# convert the object into a dict
check_configure_evc_mode_request_type_dict = check_configure_evc_mode_request_type_instance.to_dict()
# create an instance of CheckConfigureEvcModeRequestType from a dict
check_configure_evc_mode_request_type_form_dict = check_configure_evc_mode_request_type.from_dict(check_configure_evc_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


